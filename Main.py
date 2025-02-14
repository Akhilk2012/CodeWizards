import pygame , sys 
import os
from itertools import zip_longest
pygame.init()
pygame.font.init()

clock = pygame.time.Clock()
fps = 60
run = True

saved_file = "tasks.txt"
points_file = "points.txt"
 
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
font_Y = 100
points_count = 0
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
view_img = pygame.image.load("View_button.png").convert_alpha()
set_img = pygame.image.load("Set_button.png").convert_alpha()
shop_img = pygame.image.load("Shop_button.png").convert_alpha()
delete_img = pygame.image.load("Del_button.png").convert_alpha()

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
    point_counter = count.render(f"Points : {points_count}" , True , ("#879CEB"))
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
points = load_tasks(points_file)
exit_button = Button( 525, 0 , exit_img , 0.25)
exit_button_1 = Button( 525, 0 , exit_img , 0.25)
exit_button_2 = Button( 525, 0 , exit_img , 0.25)

struct_button = Button( 0, 0 , struct_img, 0.15)
start_button = Button( 225 , 290 , start_button , 0.30)
text_input_1 = Text_box(50, 400, 550, 30)
text_input_2 = Text_box(50, 250, 550, 30)
text_input_3 = Text_box(50, 250, 550, 30)
add_button = Button(60 ,500, add_img , 0.25)
view_button = Button(225, 500 , view_img , 0.25)
set_button = Button(250,500, set_img , 0.25)
shop_button = Button(0, 100 , shop_img , 0.25)
delete_button = Button(550 , 150 , delete_img , 0.15)

def view_screen():
    while True:
         while True:
            screen.fill("#0476D0")
            y_offset = 50
            draw_text("Tasks and Points:", 50, y_offset - 30 , black , font_sub)
            counter(font_X, font_Y, font_counter)
            for idx, (task, point) in enumerate(zip_longest(tasks, points), start=1):
                task_text = f"{idx}. {task}" if task else ""
                point_text = f"{point}" if point else ""
                                 
                draw_text(f"{task_text} - Points: {point_text}", 50, y_offset , black , font)
                y_offset += 30
                if y_offset > 600:
                    break  # Limit to showing a few lines
            for event in pygame.event.get():
                text_input_3.handle_events(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if delete_button.draw() == True:
                        if text_input_3.text.isdigit():  # Check if the text is a number
                            num_t_del = int(text_input_3.text)
                            if 1 <= num_t_del <= len(tasks):
                                removed_task = tasks.pop(num_t_del - 1)
                                removed_point = points.pop(num_t_del - 1)
                                print(f"Task '{removed_task}' has been deleted. Points '{removed_point}' have been deleted.")
                                save_tasks(saved_file, tasks)
                                save_tasks(points_file, points)
                            else:
                                print("Invalid task number.")
                            text_input_3.text = ""  # Clear input after processing
                        else:
                            print("Please enter a valid number.")
                    if exit_button.draw() == True:
                        return  
            text_input_3.draw()
            delete_button.draw()       
            exit_button.draw()
            pygame.display.update()
def point_screen():
    while True:
         while True:
            screen.fill("#87EBD6")
            for event in pygame.event.get():
                text_input_2.handle_events(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if set_button.draw() == True:
                        points_typed = text_input_2.text 
                        if points_typed :
                            points.append(points_typed)
                            text_input_2.text = ""
                            save_tasks(points_file, points)
                            return
            set_button.draw()
            text_input_2.draw()
            pygame.display.update()
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
                        point_screen()
                        task_typed = text_input_1.text 
                        if task_typed :
                            tasks.append(task_typed)
                            text_input_1.text = ""
                            save_tasks(saved_file, tasks)
                        
                    if view_button.draw() == True:
                        view_screen()
                    if exit_button_1.draw() == True:
                        return  # Exit struct_screen() and go back to main screen by return
            draw_text("Function Page", 250, 30, white,font_sub)
            text_input_1.draw()
            exit_button_1.draw()
            add_button.draw()
            view_button.draw() 
            pygame.display.update()

def shop_screen():
    while True:
         while True:
            screen.fill(black)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if exit_button.draw() == True:
                        return  
            draw_text("Exampler usage of points", 180, 30, white,font_sub)
            
            exit_button.draw()

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
    struct_button.draw()
    shop_button.draw()
    start_button.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if struct_button.draw() == True :
                struct_screen()
            if shop_button.draw() == True :
                shop_screen()
            if start_button.draw() == True :
                main_screen()
    draw_text("Task Manager", 186, 100, black , font_1)
    draw_text("Welcome to the task manager !" , 175 , 180, black , font_2) 
    draw_text("The button in the middle of the screen will take you to the" , 115 , 450, black , font) 
    draw_text("main page with our functions" , 115 , 470, black , font)
    draw_text("The button at the top left corner of the screen will show the " , 115 , 490, black , font) 
    draw_text("instructions on how to use the code," , 115 , 510, black , font)
    pygame.display.flip()
    pygame.display.update()

pygame.quit()
sys.exit()
