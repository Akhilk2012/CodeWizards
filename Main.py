import pygame
import os

pygame.init()

run = True

saved_file = "tasks.txt"

# These are some colors we can use later on in the program to create our software
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,255,0)
green = (0,0,255)

font = pygame.font.SysFont('Arial', 20)

screen_width = 640
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Task Manager")

diplay_icon = pygame.image.load("Windows_icon.png").convert_alpha()
pygame.display.set_icon(diplay_icon)

exit_button = pygame.image.load("Exit_button.png").convert_alpha()

def draw_text(text, x, y, color=black):
    screen.blit(font.render(text, True, color), (x, y))

class Button():
    def __init__(self,x,y,image) :
        self.image = image 
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
    def draw(self):
        screen.blit(self.image, (self.rect.x , self.rect.y))

exit_button = Button(100 , 200 , exit_button)

while run :
    screen.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.flip()

    pygame.display.update()

pygame.quit()
