import pygame
from pygame.draw import *
from numpy import cos, sin, pi, abs
import matplotlib.pyplot as plt

pygame.init()

FPS = 200
t = 0
dt = 0.001
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

blue = (0, 184, 217)
grey = (133, 150, 150)
white = (255, 255, 255)
green = (153, 255, 153)
dark_green = (80, 200, 120)
yellow = (255, 255, 0)
purple = (128, 0, 255)
black = (0, 0, 0)


class pendulum:
    def __init__(self, l0, l, k, A, s, alpha, v, w, mu_m, A4, B, C, D, E):
        self.l0 = l0
        self.l = l
        self.k = k
        self.A = A
        self.s = s
        self.alpha = alpha
        self.v = v
        self.w = w
        self.mu_m = mu_m
        self.A4 = A4
        self.B = B
        self.C = C
        self.D = D
        self.E = E


def read_parameters_of_pendulum_from_file(input_filename, pend):
    with open(input_filename) as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # pass empty lines and lines with commits
            else:
                parse_parameters(line, pend)
    return pend


def parse_parameters(line, pend):
    """Read data of pendulum from line. Line must have next view:
    <l0> <l> <k> <A> <s> <alpha> <v> <w> <mu/m> <A4> <B> <C> <D> <E>

    l0 - length of spring without deformation (=const)
    l - length of spring at the moment. l may be changed. Initially l = start-up length of the spring
    k - asperity of spring
    A - amplitude of motor fluctuations
    s - coordinate of the motor at the moment
    alpha - the deflection angle. Initially alpha = alpha0 - the start-up angle
    v - speed of body along the rod. Initially v = v0 - start-up speed
    w - angular speed of body. Initially w = w0 - start-up angular speed
    mu/m - ratio coefficient of friction to mass
    A4 - coefficient at t^4
    B - coefficient at t^3
    C - coefficient at t^2
    D - coefficient at t
    E - free member. It specifies the start-up coordinate of the motor
    fi is function of time. fi specifies phase change of motor. fi is polynomial of degree 4. fi = A_4t^4 + Bt^3 + Ct^2 + Dt + E 
    
    Parameters of function:

    **line** — line with description of pendulum's parameters
    **pend** - object of class pendulum
    """
    line_prepared = line.strip()
    line_internals = line_prepared.split()

    pend.l0 = int(line_internals[0])
    pend.l = int(line_internals[1])
    pend.k = int(line_internals[2])
    pend.A = int(line_internals[3])
    pend.s = int(line_internals[4])
    pend.alpha = float(line_internals[5])
    pend.v = float(line_internals[6])
    pend.w = float(line_internals[7])
    pend.mu_m = float(line_internals[8])
    pend.A4 = float(line_internals[9])
    pend.B = float(line_internals[10])
    pend.C = float(line_internals[11])
    pend.D = float(line_internals[12])
    pend.E = float(line_internals[13])


def draw_pendulum(s, l, alpha):
    '''
    This function draws pendulum at the moment
    Parameteres:
    s - displacement of the motor along the rod
    l - length of the spring at the moment
    alpha - angle of deflection of the rod from the vertical
    '''
    x = (l + s) * sin(alpha)
    y = (l + s) * cos(alpha)    #coordinates of the spring's end
    x1 = 650 * sin(alpha)
    y1 = 650 * cos(alpha)     #coordinates of the rod's end
    h = (300 / l) * 30   #height of the triangles which make up the spring
    if l < 75:
        h = 120
    line(screen, grey, [screen_width/2, 40], [screen_width/2 + x1, y1 + 40], 4)    #draw the rod
    line(screen, white, [screen_width/8, 40], [screen_width*7/8, 40], 4)   #draw ceiling. 40 is the ceiling's displacement from the top
    spring = []   #list of coordinates of the ends of the spring links
    n = 18   #number of the spring's links. Number of their ends is (n+1)
    spring.append([s * sin(alpha) + screen_width/2, s * cos(alpha) + 40])
    spring.append([h * cos(alpha) + (s + 0.5/(n-1)*l) * sin(alpha) + screen_width/2, -h * sin(alpha) + (s + 0.5/(n-1)*l) * cos(alpha) + 40])
    for i in range(n-2):
        spring.append([(-1)**(i+1) * h * cos(alpha) + (s + (i+1.5)/(n-1)*l) * sin(alpha) + screen_width/2, (-1)**i * h * sin(alpha) + (s + (i+1.5)/(n-1)*l) * cos(alpha) + 40])
    spring.append([x + screen_width/2, y + 40]) 
    lines(screen, blue, False, spring, 3)      #draw the spring
    circle(screen, green, [(s + l + 20) *  sin(alpha) + screen_width/2, (s + l + 20) *  cos(alpha) + 40], 20)   #draw the pendulum's body


pend = pendulum(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
read_parameters_of_pendulum_from_file('Desktop/Labs Python/Modeling-of-fluctuations/input.txt', pend)

"""
Here the gravitational constant 
(meters per second) is defined
"""
g = 10000

def Euler_equations(pend, t, dt):
    """
    In this function we calculate values of x and alpha on the
    next step
    """
    phi = pend.A4*t**4 + pend.B*t**3 + pend.C*t**2 + pend.D*t + pend.E
    phi_prime = 4*pend.A4*t**3 + 3*pend.B*t**2 + 2*pend.C*t + pend.D
    pend.s = pend.A*abs(sin(phi))
    pend.l += dt*pend.v 
    if pend.l <= 0:
        pend.l = -pend.l
        pend.v = -pend.v
    pend.alpha += dt*pend.w

def RK_4(pend, t, dt):
    """
    Here we calculate the value of velocity and angle-velocity
    on the next iteration
    1) phi is a function of time in the argument of motor-coordinate sinus-function
    2) phi_prime is the first prime of phi function of time
    3) phi_dprime is the second prime of phi function of time
    4) v - velocity; w - angle-velocity; aplha - angle; l - length of spring
    """
    phi = pend.A4*t**4 + pend.B*t**3 + pend.C*t**2 + pend.D*t + pend.E
    phi_prime = 4*pend.A4*t**3 + 3*pend.B*t**2 + 2*pend.C*t + pend.D 
    phi_dprime = 12*pend.A4*t**2 + 6*pend.B*t + 2*pend.C
    pend.s = pend.A*abs(sin(phi))
    pend.v += dt*(-pend.mu_m*pend.v + pend.A*(sin(phi)*(phi_prime**2) - cos(phi)*phi_dprime) + pend.w**2*(pend.l + pend.s) 
    + g*cos(pend.alpha) - pend.k*(pend.l - pend.l0))
    pend.w += dt*(-pend.mu_m*pend.w - (g*sin(pend.alpha) + 2*pend.w)/(pend.l + pend.s))

clock = pygame.time.Clock()
finished = False

t_sol = []
x_sol = []
y_sol = []

while not finished:                   # This is the main cycle. It will visualize fluctuations, recalculate parameters, and fill lists for further plotting
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
    draw_pendulum(pend.s, pend.l, pend.alpha)
    pygame.display.update()
    Euler_equations(pend, t, dt)
    RK_4(pend, t, dt)
    screen.fill(black)
    t_sol.append(t)
    x_sol.append((pend.s + pend.l) * sin(pend.alpha))
    y_sol.append((pend.s + pend.l) * cos(pend.alpha))
    t += dt
pygame.quit()

#subplot 1
sp = plt.subplot(2, 1, 1) 
plt.plot(t_sol, x_sol)
plt.grid(True)
plt.title(r'$x(t)$')
plt.ylabel(r'$x$')

#subplot 2
sp = plt.subplot(2, 1, 2)
plt.plot(t_sol, y_sol)
plt.grid(True)
plt.title(r'$y(t)$')
plt.xlabel(r'$t$')
plt.ylabel(r'$y$')

plt.show()