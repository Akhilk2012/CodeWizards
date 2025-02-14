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
add_img = pygame.image.load("Add_button.png").convert_alpha()

def load_tasks(filename):
    if not os.path.exists(filename):
        return []
    with open(filename, 'r') as file:
        tasks = file.readlines()
    return [task.strip() for task in tasks]

def save_tasks(filename, tasks):
    with open(filename, 'w') as file:
        for task in tasks :
            file.write(task + '\n')
        
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
    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.rect.collidepoint(event.pos)
        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_RETURN:
                return self.text
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode
        return None
    def draw(self):
        color = green if self.active else black
        pygame.draw.rect(screen, color, self.rect, 2)
        draw_text(self.text, self.rect.x + 5, self.rect.y + 5, white, font_2)

tasks = load_tasks(saved_file)
exit_button = Button( 525, 0 , exit_img , 0.25)
exit_button_1 = Button( 525, 0 , exit_img , 0.25)
struct_button = Button( 0, 0 , struct_img, 0.15)
start_button = Button( 225 , 290 , start_button , 0.30)
text_input_1 = Text_box(50, 400, 550, 30)
add_button = Button(60 ,500, add_img , 0.25)
def main_screen():
    while True:
         while True:
            screen.fill("#1A7499")
        
            # Event handling
            for event in pygame.event.get():
                text_input_1.handle_events(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if add_button.draw() == True:
                        task_typed = text_input_1.text 
                        if task_typed :
                            tasks.append(task_typed)
                            text_input_1.text = ""
                            save_tasks(saved_file, tasks)
                    if exit_button_1.draw() == True:
                        return  # Exit struct_screen() and go back to main screen by return
            
            text_input_1.draw()
            exit_button_1.draw() # Second exit button for second screen 
            add_button.draw()
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
            draw_text("recording tasks we need to complete.", 30, 100, white,font)
            draw_text("Features we have in our product are:", 30, 150, white,font)
            draw_text("  1.Add: The add button lets you mention what tasks you have and", 30, 190, white,font)
            draw_text("  how many points its worth, and enter them into the sofware. Every", 30, 210, white,font)
            draw_text("  task you add will always be saved when the sofware is closed.", 30, 230, white,font)
            draw_text("  2.Delete: The delete button lets you delete a specific tasks you", 30, 270, white,font)
            draw_text("  mentioned in the sofware.", 30, 290, white,font)
            draw_text("  3.View: The view button lets you see what tasks you have yet,", 30, 330, white,font)
            draw_text("  to complete and mark a task if you have completed it.", 30, 350, white, font )
            draw_text("  Once a task is marked completed the pointes mentioned for", 30, 370, white, font )
            draw_text("  the task will be added to your points counter.", 30, 390, white, font)
            draw_text("Points system:", 30, 430 , white, font)
            draw_text("For every task you add, you will have to give a certain amount", 30, 470 , white, font)
            draw_text("of points. Theese points can be used by kids to buy gifts or", 30, 490, white, font)
            draw_text("rewards they want. For example if you have 50 points and you",30, 510, white, font)
            draw_text("bought a book worth 10 points, you will subtract 10 points from",30, 530, white, font)
            draw_text("your current amount of points. If you don't have enough points", 30, 550, white, font)
            draw_text("it will not let you subtract the points thus you can't buy the item.", 30, 570, white, font)
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
