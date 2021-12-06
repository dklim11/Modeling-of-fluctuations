import tkinter
from tkinter.filedialog import *
from pendulum_vis import *
from pendulum_model import *
from pendulum_input import *

perform_execution = False
"""Флаг цикличности выполнения расчёта"""

physical_time = 0
"""Физическое время от начала расчёта.
Тип: float"""

displayed_time = None
"""Отображаемое на экране время.
Тип: переменная tkinter"""

time_step = None
"""Шаг по времени при моделировании.
Тип: float"""

objects = []
"""Список объектов в системе."""


def execution():
    """Функция исполнения -- выполняется циклически, вызывая обработку всех объектов,
    а также обновляя их положение на экране.
    Цикличность выполнения зависит от значения глобальной переменной perform_execution.
    При perform_execution == True функция запрашивает вызов самой себя по таймеру через от 1 мс до 100 мс.
    """
    global physical_time
    global displayed_time
    if objects != []:
        recalculate_objects_positions(objects, time_step.get()) 

        """ из pendulum_model:
        def recalculate_objects_positions(objects, dt):
    Пересчитывает координаты объектов objects.
    Параметры:
     **objects** — список объектов, для которых нужно пересчитать координаты.
     **dt** — шаг по времени"""

        save_objects_positions(objects, physical_time)

        """из pendulum_input:
        def save_objects_positions(objects, time):
    
    Сохраняет данные о положении тел в файл phys_model.txt   в формате
        <Физическое время с начала симуляции в секундах>
        <...>
        
    Параметры:
        **objects** — список объектов планет и звёзд
        **physical_time** — время с начала симуляции
        """
    for body in pendulum_objects:
        update_object_position(space, body)
        """ из vis:
        def update_object_position(space, body):
    Перемещает отображаемый объект на холсте.
    Параметры:
     **space** — холст для рисования.
     **body** — тело, которое нужно переместить.
    x = scale_x(body.x)
    y = scale_y(body.y)
        """
    physical_time += time_step.get()
    displayed_time.set("%.1f" % physical_time + " seconds gone")

    if perform_execution:
        space.after(101 - int(time_speed.get()), execution)


def start_execution():
    """Обработчик события нажатия на кнопку Start.
    Запускает циклическое исполнение функции execution.
    """
    global perform_execution
    perform_execution = True
    start_button['text'] = "Pause"
    start_button['command'] = stop_execution

    clear_stats(objects)

    """из pendulum_input:
    def clear_stats(objects):
    
    Очищает файл phys_model.txt
    Сохраняет информацию о типах существующих тел в формате:

        <...>
    
        #End of the header
        
    Параметры:
        **objects** — список физических объектов в системе
        **physical_time** — время с начала симуляции
    """
    execution()
    print('Started execution...')


def stop_execution():
    """Обработчик события нажатия на кнопку Start.
    Останавливает циклическое исполнение функции execution.
    """
    global perform_execution
    perform_execution = False
    start_button['text'] = "Start"
    start_button['command'] = start_execution
    print('Paused execution.')

"""def open_diagram():
    Запускает считывание информации и отображает графики
    stop_execution()
    legend, t, r, v = get_data_for_plots()
    draw_plots(legend, t, r, v)
"""

def open_file_dialog():
    """Открывает диалоговое окно выбора имени файла и вызывает
    функцию считывания параметров системы физических объектов из данного файла.
    Считанные объекты сохраняются в глобальный список objects
    """
    global objects
    global perform_execution
    global physical_time
    stop_execution()
    for obj in objects:
        space.delete(obj.image)  # удаление старых изображений физ. тел
    in_filename = askopenfilename(filetypes=(("Text file", ".txt"),))
    if in_filename != '':
        objects = read_space_objects_data_from_file(in_filename)
        """из input:
        def read_objects_data_from_file(input_filename):
    Cчитывает данные о физических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов
    Параметры:
     **input_filename** — имя входного файла
        """
        max_distance = max([max(abs(obj.x), abs(obj.y)) for obj in objects])
        calculate_scale_factor(max_distance)

        """из pendulum_vis:
        def calculate_scale_factor(max_distance):
     Вычисляет значение глобальной переменной **scale_factor** по данной характерной длине
    global scale_factor
    scale_factor = 0.4*min(window_height, window_width)/max_distance
    print('Scale factor:', scale_factor)"""

        for obj in pendulum_objects:
            if obj.type == 'ball':
                create_ball_image(space, obj)
            if obj.type == 'kernel':
                create_kernel_image(space,obj)
            if   obj.type == 'spring':
                create_spring_image(space,obj) 
            if   obj.type == 'ceiling':
                create_ceiling_image(space,obj) 
            if   obj.type == 'point':
                create_point_image(space,obj)
            else:
                raise AssertionError()
        physical_time = 0


def save_file_dialog():
    """Открывает диалоговое окно выбора имени файла и вызывает
    функцию считывания параметров системы небесных тел из данного файла.
    Считанные объекты сохраняются в глобальный список space_objects
    """
    stop_execution()
    out_filename = asksaveasfilename(filetypes=(("Text file", ".txt"),))
    write_objects_data_to_file(out_filename, objects)

    """из pendulum_input:
    def write_space_objects_data_to_file(output_filename, space_objects):
    Сохраняет данные о космических объектах в файл.
    Строки должны иметь следующий формат:
    <...> 
    l0 - length of pendulum
    k - asperity of spring
    fi - function of time
    A - amplitude of motor fluctuations
    alpha0 - the start-up angle
    Параметры:
    **output_filename** — имя входного файла
    **objects** — список физ объектов
    """

def main():
    """Главная функция главного модуля.
    Создаёт объекты графического дизайна библиотеки tkinter: окно, холст, фрейм с кнопками, кнопки.
    """
    global physical_time
    global displayed_time
    global time_step
    global time_speed
    global space
    global start_button

    print('Modelling started!')
    physical_time = 0

    root = tkinter.Tk()
    root.title("Kepler's laws of motion")
    root.geometry(window_size)
    # пространство отображается на холсте типа Canvas
    space = tkinter.Canvas(root, width= window_width, height = window_height, bg="white")
    space.pack(side=tkinter.TOP)
    # нижняя панель с кнопками
    frame = tkinter.Frame(root)
    frame.pack(side=tkinter.BOTTOM)

    start_button = tkinter.Button(frame, text="Start", command=start_execution, width=6)
    start_button.pack(side=tkinter.LEFT)

    time_step = tkinter.DoubleVar()
    time_step.set(1)
    time_step_entry = tkinter.Entry(frame, textvariable=time_step)
    time_step_entry.pack(side=tkinter.LEFT)

    time_speed = tkinter.DoubleVar()
    scale = tkinter.Scale(frame, variable=time_speed, orient=tkinter.HORIZONTAL)
    scale.pack(side=tkinter.LEFT)

    load_file_button = tkinter.Button(frame, text="Open file...", command=open_file_dialog)
    load_file_button.pack(side=tkinter.LEFT)
    save_file_button = tkinter.Button(frame, text="Save to file...", command=save_file_dialog)
    save_file_button.pack(side=tkinter.LEFT)
    """ open_diagram_button = tkinter.Button(frame, text="View stats", command=open_diagram)
    open_diagram_button.pack(side=tkinter.LEFT) """

    displayed_time = tkinter.StringVar()
    displayed_time.set(str(physical_time) + " seconds gone")
    time_label = tkinter.Label(frame, textvariable=displayed_time, width=30)
    time_label.pack(side=tkinter.RIGHT)

    root.mainloop()
    print('Modelling finished!')

if __name__ == "__main__":
    main()
