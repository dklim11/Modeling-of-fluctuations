import pygame
from pygame.draw import *
import numpy as np

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
    x = (l + s) * np.sin(alpha)
    y = (l + s) * np.cos(alpha)    #coordinates of the spring's end
    x1 = 500 * np.sin(alpha)
    y1 = 500 * np.cos(alpha)     #coordinates of the rod's end
    h = (300 / l) * 30   #height of the triangles which make up the spring
    line(screen, grey, [screen_width/2, 40], [screen_width/2 + x1, y1 + 40], 4)    #draw the rod
    line(screen, white, [screen_width/8, 40], [screen_width*7/8, 40], 4)   #draw ceiling
    lines(screen, blue, False, [[s * np.sin(alpha) + screen_width/2, s * np.cos(alpha) + 40], 
                                [h * np.cos(alpha) + (s + 0.1*l) * np.sin(alpha) + screen_width/2, -h * np.sin(alpha) + (s + 0.1*l) * np.cos(alpha) + 40],
                                [-h * np.cos(alpha) + (s + 0.3*l) * np.sin(alpha) + screen_width/2, h * np.sin(alpha) + (s + 0.3*l) * np.cos(alpha) + 40],
                                [h * np.cos(alpha) + (s + 0.5*l) * np.sin(alpha) + screen_width/2, -h * np.sin(alpha) + (s + 0.5*l) * np.cos(alpha) + 40],
                                [-h * np.cos(alpha) + (s + 0.7*l) * np.sin(alpha) + screen_width/2, h * np.sin(alpha) + (s + 0.7*l) * np.cos(alpha) + 40],
                                [h * np.cos(alpha) + (s + 0.9*l) * np.sin(alpha) + screen_width/2, -h * np.sin(alpha) + (s + 0.9*l) * np.cos(alpha) + 40],
                                [x + screen_width/2, y + 40]], 3)      #draw the spring
    circle(screen, green, [(s + l + 20) * np.sin(alpha) + screen_width/2, (s + l + 20) * np.cos(alpha) + 40], 20)   #draw the pendulum's body

draw_pendulum(100, 350, 0)
draw_pendulum(0, 500, np.pi/6)
draw_pendulum(30, 300, -np.pi/8)

pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:        
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()