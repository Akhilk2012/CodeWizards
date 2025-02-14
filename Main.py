import pygame
import os

pygame.init()

run = True

screen_width = 640
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Task Manager")

#diplay_icon = pygame.image.load("")
#pygame.display.set_icon(diplay_icon)

while run :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()