import pygame
from pygame.draw import *
from numpy import cos, sin, pi, abs
from Pendulum_objects import pendulum
from Pendulum_vis import *
from Pendulum_input import *
from Pendulum_model import *

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


pend = pendulum(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
read_parameters_of_pendulum_from_file('Desktop\Labs Python\Modeling-of-fluctuations\input.txt', pend)
g = 10000

clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
    draw_pendulum(pend.s, pend.l, pend.alpha)
    pygame.display.update()
    Euler_equations(pend, t, dt)
    RK_4(pend, t, dt)
    t += dt
    screen.fill(black)
pygame.quit()