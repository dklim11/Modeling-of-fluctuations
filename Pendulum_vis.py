import pygame
from pygame.draw import *
from numpy import sin, cos, pi

pygame.init()

FPS = 60
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
    x1 = 500 * sin(alpha)
    y1 = 500 * cos(alpha)     #coordinates of the rod's end
    h = (300 / l) * 30   #height of the triangles which make up the spring
    line(screen, grey, [screen_width/2, 40], [screen_width/2 + x1, y1 + 40], 4)    #draw the rod
    line(screen, white, [screen_width/8, 40], [screen_width*7/8, 40], 4)   #draw ceiling
    spring = []
    spring.append([s * sin(alpha) + screen_width/2, s * cos(alpha) + 40])
    n = 20
    for i in range(n-1):
        spring.append([(-1)**i * h * cos(alpha) + (s + (i+1)/n*l) * sin(alpha) + screen_width/2, (-1)**(i+1) * h * sin(alpha) + (s + (i+1)/n*l) * cos(alpha) + 40])
    spring.append([x + screen_width/2, y + 40]) 
    lines(screen, blue, False, spring, 3)      #draw the spring
    circle(screen, green, [(s + l + 20) *  sin(alpha) + screen_width/2, (s + l + 20) *  cos(alpha) + 40], 20)   #draw the pendulum's body

draw_pendulum(100, 350, 0)
draw_pendulum(0, 500,  pi/6)
draw_pendulum(30, 300, - pi/8)

pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:        
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()