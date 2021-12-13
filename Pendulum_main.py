import pygame
from pygame.draw import *
import numpy as np
pygame.init()

from pendulum_vis import *
from pendulum_model import *
from pendulum_input import *
from pendulum_objects import *


objects = []
"""Список объектов в системе."""

def main():
    FPS = 30
    

    ended = False
    finished = False

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



if not started_already:
            screen.fill(black)
            clicked = False

while not finished:
    clicked.tick(dt) (t += dt)
    {vis}
    Euler_equations(pend, t, dt)
    RK_4(pend, t, dt)
     pygame.display.update()

pygame.quit()

if __name__ == "__main__":
    main()


