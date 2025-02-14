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

bg_color = (135,206,235)

font = pygame.font.SysFont('Arial', 20)

screen_width = 640
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Task Manager")

diplay_icon = pygame.image.load("Windows_icon.png").convert_alpha()
pygame.display.set_icon(diplay_icon)

exit_img = pygame.image.load("Exit_button.png").convert_alpha()

def draw_text(text, x, y, color=black):
    screen.blit(font.render(text, True, color), (x, y))

class Button():
    def __init__(self,x,y,image,scale) :
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image,(int(width * scale),int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False
    def draw(self):
        action = False
        # Getting the mouse position
        pos = pygame.mouse.get_pos()
        # Checking if the mouse is over the button

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True 
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        # This will draw the button on the screen
        screen.blit(self.image, (self.rect.x , self.rect.y))

        return action

exit_button = Button( 525, 0 , exit_img , 0.25)

while run :
    screen.fill(bg_color)

    if exit_button.draw() == True :
        run = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.flip()

    pygame.display.update()

pygame.quit()
