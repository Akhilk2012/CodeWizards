import pygame , sys 
import os

pygame.init()
pygame.font.init()

clock = pygame.time.Clock()
fps = 60
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
font_sub = pygame.font.SysFont('Arial',27,bold= True)
font_1 = pygame.font.Font("freesansbold.ttf" , 40)
font_2 = pygame.font.Font("freesansbold.ttf" , 20)
font_counter = pygame.font.Font("freesansbold.ttf" , 28 )
font_X = 446
font_Y = 10
points = 0
screen_width = 640
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Task Manager")

diplay_icon = pygame.image.load("Windows_icon.png").convert_alpha()
pygame.display.set_icon(diplay_icon)

exit_img = pygame.image.load("Exit_button.png").convert_alpha()
struct_img = pygame.image.load("Struct_button.png").convert_alpha()
start_button = pygame.image.load("Start_button.png").convert_alpha()

def draw_text(text, x, y, color,font):
    use = font 
    screen.blit(use.render(text, True, color), (x, y))
    
def counter(x,y,font):
    count = font
    point_counter = count.render(f"Points : {points}" , True , ("#879CEB"))
    screen.blit(point_counter, (x,y))

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
class Text_box():
    def __init__(self,x,y,w,h):
        self.rect = pygame.Rect(x,y,w,h)
        self.text = ""
        self.active = False 

exit_button = Button( 525, 0 , exit_img , 0.25)
exit_button_1 = Button( 525, 0 , exit_img , 0.25)
struct_button = Button( 0, 0 , struct_img, 0.15)
start_button = Button( 225 , 290 , start_button , 0.30)

def main_screen():
    while True:
         while True:
            screen.fill("#1A7499")
        
            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if exit_button_1.draw() == True:
                        return  # Exit struct_screen() and go back to main screen by return
    
            exit_button_1.draw() # Second exit button for second screen 

            pygame.display.update()
def struct_screen():
    while True:
         while True:
            screen.fill(black)
        
            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if exit_button.draw() == True:
                        return  # Exit struct_screen() and go back to main screen by return

            # Draw text and exite button on the instruction menu
            draw_text("Instructions", 250, 30, white,font_sub)
            draw_text("Our software is a task manager that helps in gathering and ", 30, 80, white,font)
            draw_text( "recording tasks we need to complete.", 30, 100, white,font)
            draw_text("Features we have in our product are:", 30, 150, white,font)
            draw_text("  1.Add: The add button lets you mention what tasks you have", 30, 190, white,font)
            draw_text("  and enter them into the sofware...every task you add will", 30, 210, white,font)
            draw_text("  always be saved when the sofware is closed.", 30, 230, white,font)
            draw_text("  2.Delete: The delete button lets you delete a specific tasks you", 30, 270, white,font)
            draw_text("  mentioned in the sofware.", 30, 290, white,font)
            exit_button.draw()

            pygame.display.update()

while run :
    clock.tick(fps)
    screen.fill(bg_color)
    counter(font_X, font_Y, font_counter)
    struct_button.draw()
    start_button.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if struct_button.draw() == True :
                struct_screen()
            if start_button.draw() == True :
                main_screen()
    draw_text("Task Manager", 185.67, 100, black , font_1)
    pygame.display.flip()
    pygame.display.update()

pygame.quit()
sys.exit()
