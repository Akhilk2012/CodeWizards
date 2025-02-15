import pygame , sys 
import os
from itertools import zip_longest
import random
#import time
#import threading
from datetime import date  

today = date.today()

items = ["Stationary" , "Candy" , "Books" , "Chocolate" , "Outside Food" , "Makeup" , "Sport" , "Clothes" , "Accessories" , "Video Games"]
prices = [25 , 30 , 50 , 30 , 115 , 60 , 50 , 50 , 55 , 35 , 95]

chores = {
    "cleaning": ["Vacuum the living room", "Wipe down kitchen counters", "Dust the shelves", "Mop the floors", "Clean the windows", "Organize the bookshelf"],
    "laundry": ["Wash clothes", "Fold laundry", "Sort socks", "Iron clothes", "Wash bed sheets"],
    "kitchen": ["Do the dishes", "Take out the trash", "Organize the fridge", "Scrub the sink", "Wipe the stove"],
    "general": ["Water the plants", "Feed the pets", "Declutter your workspace", "Clean your room", "Walk your pets", "Help in cooking", "Make your bed"]
}

#Stationary: 25", 30, 100, black,font_tiny)
#            draw_text("      Candy: 30", 30, 120,black,font_tiny)
#            draw_text("      Books: 50", 30, 140, black,font_tiny)
#            draw_text("      Chocolate: 30", 30, 160, black, font_tiny)
#            draw_text("      Outside Food: 115", 30, 180, black, font_tiny)
#            draw_text("      Makeup: 60", 30, 200, black, font_tiny)
#            draw_text("      Sports: 50", 30, 220, black, font_tiny)
#            draw_text("      Clothes: 55", 30, 240, black, font_tiny)
#            draw_text("      Accessories: 35", 30, 260, black, font_tiny)
#            draw_text("      Video Games: 95", 30, 280, black, font_tiny)

            
pygame.init()
pygame.font.init()

clock = pygame.time.Clock()
fps = 60
run = True

saved_file = "tasks.txt"
points_file = "points.txt"

# These are some colors we can use later on in the program to create our software
white = (255,255,255)

gold = (255, 215, 0)  
silver = (192, 192, 192)  
bronze = (205, 127, 50) 
gray = (180, 180, 180)
black = (0, 0, 0)


red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)

bg_color = (135,206,235)

font_board = pygame.font.Font(None, 40)
font = pygame.font.SysFont('Arial', 20)
font_tiny = pygame.font.SysFont('Arial', 15)
input_font = pygame.font.Font(None,28)
font_sub = pygame.font.SysFont('Arial',27,bold= True)
font_1 = pygame.font.Font("freesansbold.ttf" , 40)
font_2 = pygame.font.Font("freesansbold.ttf" , 20)
font_counter = pygame.font.Font("freesansbold.ttf" , 28 )
font_X = 446
font_Y = 100
screen_width = 640
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Point Manager")

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
complete_img = pygame.image.load("Complete_button.png").convert_alpha()
clear_img = pygame.image.load("Clear_button.png").convert_alpha()
board_img = pygame.image.load("Board_button.png").convert_alpha()
mart_img = pygame.image.load("Mart_button.png").convert_alpha()
buy_img = pygame.image.load("Buy_button.png").convert_alpha()
chat_img = pygame.image.load("Chat_button.png").convert_alpha()
score_file = "Members"
# The peice of code below make sure the user's input is in the correct format
#def parse_time(user_input):
#    try:
#        hours, minutes, seconds = map(int, user_input.split(":"))
#        return hours, minutes, seconds
#    except ValueError:
#        print("Invalid time format. Please enter in HH:MM:SS format.")
#        return None
    
#def start_timer(hours, minutes, seconds):
#    total_seconds = hours * 3600 + minutes * 60 + seconds
#    print(f"Task will be deleted in {hours} hours, {minutes} minutes, and {seconds} seconds.")

#    time.sleep(total_seconds)
    
#    delete_task()

#def delete_task():
#    print("Task has been deleted.")

#def timer_thread(user_input):
#    time_parts = parse_time(user_input)
#    if time_parts:
#        hours, minutes, seconds = time_parts
#        timer_thread = threading.Thread(target=start_timer, args=(hours, minutes, seconds))
#        timer_thread.start()
#        timer_thread.join() 
#    else:
#        print("Error in input. Cannot start timer.")

# Load scores from file
chat_history = ["ChoreBot: Hello! Ask me what chores you can do. Type 'exit' to quit.",
                "Questions to ask about: Cleaning, Laundry, Kitchen, General"]
user_input = ""

def suggest_chore(query):
    query = query.lower()
    for category, tasks in chores.items():
        if category in query:
            return f"You can do this: {random.choice(tasks)}"
    return "I don't have chores for that. Try asking about Cleaning, Laundry, Kitchen, or General tasks."
def load_scores():
    scores = []
    if os.path.exists(score_file):
        try:
            with open(score_file, "r") as file:
                for line in file:
                    name, score = line.strip().split(",")
                    scores.append((name, int(score)))
        except Exception as e:
            print(f"Error while reading the file: {e}")
    else:
        print(f"File '{score_file}' does not exist. Creating a new one.")
        # Create the file if it doesn't exist
        try:
            with open(score_file, "w") as file:
                pass  # Create an empty file
        except Exception as e:
            print(f"Error while creating the file: {e}")
    return sorted(scores, key=lambda x: x[1], reverse=True) 

def save_scores(scores):
    try:
        with open(score_file, "w") as file:
            for name, score in scores:
                file.write(f"{name},{score}\n")
        print(f"Scores saved successfully to '{score_file}'")
    except Exception as e:
        print(f"Error while saving the file: {e}")

def add_score(name, score):
    scores = load_scores()
    scores.append((name, score))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)[:5]  # Keep top 5
    save_scores(scores)

# Draw leaderboard with a cool style
def draw_leaderboard():
    screen.fill((0, 50, 100))  # Dark blue background

    # Title
    title_text = font_board.render("🏆 Point Leaderboard 🏆", True, white)
    screen.blit(title_text, (screen_width // 2 - title_text.get_width() // 2, 20))


    scores = load_scores()
    rank_colors = [gold, silver, bronze, white , gray]  # Different colors for ranking

    for i, (name, score) in enumerate(scores[:5]):  # Display up to 5 scores
        color = rank_colors[i] if i < len(rank_colors) else white  # Assign color
        text = font_board.render(f"{i + 1}. {name} - {score}", True, color)
        screen.blit(text, (150, 80 + i * 50))

add_score("Alice", 150)
add_score("Bob", 200)
add_score("Charlie", 180)
add_score("David", 170)
add_score("Eve", 160)

#save_scores("Members.txt")
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
total_points_file = 'total_points.txt'


#Testing clear files
#if os.path.exists(saved_file):
#    os.remove(saved_file)
#if os.path.exists(points_file):
#    os.remove(points_file)
#if os.path.exists(total_points_file):
#    os.remove(total_points_file)


points_count = sum(map(int, load_tasks(points_file)))
if os.path.exists(total_points_file):
    with open(total_points_file, 'r') as file:
        points_count = int(file.read().strip())
else:
    points_count = 0
exit_button = Button( 525, 0 , exit_img , 0.25)
exit_button_1 = Button( 525, 0 , exit_img , 0.25)
exit_button_2 = Button( 525, 0 , exit_img , 0.25)
exit_button_3 = Button( 525, 0 , exit_img , 0.25)
exit_button_4 = Button( 525, 0 , exit_img , 0.25)
exit_button_5 = Button( 525, 0 , exit_img , 0.25)
exit_button_6 = Button( 525, 0 , exit_img , 0.25)
struct_button = Button( 0, 0 , struct_img, 0.15)
start_button = Button( 225 , 290 , start_button , 0.30)
text_input_1 = Text_box(50, 400, 550, 30)
text_input_2 = Text_box(460, 250, 150, 30)
text_input_3 = Text_box(50, 250, 550, 30)
text_input_4 = Text_box(460, 400, 150, 30)
text_input_5 = Text_box(375 , 280 , 250 , 30)
add_button = Button(60 ,500, add_img , 0.25)
view_button = Button(225, 485 , view_img , 0.25)
set_button = Button(250,500, set_img , 0.25)
set_button_1 = Button(250,500, set_img , 0.25)
shop_button = Button(0, 100 , shop_img , 0.25)
delete_button = Button(550 , 150 , delete_img , 0.15)
complete_button = Button(475 , 300 , complete_img , 0.30)
clear_button = Button(375 , 480 , clear_img , 0.30)
board_button = Button(0, 170 , board_img , 0.40)
mart_button = Button(0,550,mart_img,0.40)
buy_button = Button(445 , 350 , buy_img , 0.2)
chat_button = Button(535 , 535 , chat_img , 0.5)

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
                       
                draw_text(f"{task_text} - Points: {point_text} - Date: {today.strftime('%d-%m-%Y')}", 50, y_offset , black , font)
                y_offset += 30
                if y_offset > 600:
                    break  # Limit to showing a few lines
            for event in pygame.event.get():
                text_input_4.handle_events(event)
                text_input_2.handle_events(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if delete_button.draw() == True:
                        
                        if text_input_2.text.isdigit():  # Check if the text is a number
                            num_t_del = int(text_input_2.text)
                            if 1 <= num_t_del <= len(tasks):
                                removed_task = tasks.pop(num_t_del - 1)
                                removed_point = points.pop(num_t_del - 1)
                                print(f"Task '{removed_task}' has been deleted.Points '{removed_point}' have been deleted.")

                                save_tasks(saved_file, tasks)
                                save_tasks(points_file, points)
                            else:
                                print("Invalid task number.")
                        else:
                            print("Please enter a valid number.")
                    if complete_button.draw() == True:
                        if text_input_4.text.isdigit():  # Check if the text is a number
                            task_t_com = int(text_input_4.text)
                            if 1 <= task_t_com <= len(tasks):
                                complete_task = tasks.pop(task_t_com - 1)
                                complete_point = points.pop(task_t_com - 1)
                                if complete_point.isdigit():
                                    global points_count
                                    points_count += int(complete_point)
                                    print(f"Points after addition: {points_count}")
                                        
                                    with open(total_points_file, 'w') as file:
                                        file.write(str(points_count))
                                print(f"Good job you completed : '{complete_task}'.Points '{complete_point}' have been acquired")

                                save_tasks(saved_file, tasks)
                                save_tasks(points_file, points)
                            text_input_2.text = ""  # Clear input after processing
                        else:
                            print("Please enter a valid number.")
                    if exit_button_2.draw() == True:
                        return  
            text_input_2.draw()
            text_input_4.draw()
            complete_button.draw()
            delete_button.draw()       
            exit_button_2.draw()
            pygame.display.update()
def point_screen():
    while True:
         while True:
            screen.fill("#87EBD6")
            for event in pygame.event.get():
                text_input_3.handle_events(event)

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if set_button.draw() == True:
                        points_typed = text_input_3.text 
                        if points_typed :
                            points.append(points_typed)
                            text_input_3.text = ""
                            save_tasks(points_file, points)
                            return  
                            
            draw_text("Points for the task :", 50, 200 , white,font_sub)
            set_button.draw()
            text_input_3.draw()
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
                    if clear_button.draw() == True:
                        tasks.clear()
                        points.clear()
                        text_input_1.text = ""
                        text_input_2.text = ""
                        text_input_3.text = ""
                        text_input_4.text = ""
                        save_tasks(saved_file, tasks)
                        save_tasks(points_file, points)
                    if exit_button_1.draw() == True:
                        return  # Exit struct_screen() and go back to main screen by return
            draw_text("Function Page", 250, 30, white,font_sub)
            draw_text("The function page includes different functions starting with the ability to", 30, 80, white,font)
            draw_text("add a task and specify properites including the amount of points its worth and ", 30, 100, white,font)
            draw_text("it will also be able to let us delete or complete tasks. This will let us ", 30, 120, white,font)
            draw_text("claim points from tasks and manage them.", 30, 140, white,font)
            draw_text("It is mandatory to fill in the points worth for the task !", 30, 160, white,font)
            draw_text("Task :", 50, 350, white,font_sub)
            text_input_1.draw()
            exit_button_1.draw()
            clear_button.draw()
            add_button.draw()
            view_button.draw() 
            pygame.display.update()
def mart_screen():
    while True:
         while True:
            screen.fill("#CCCCFF")
            counter(font_X, font_Y, font_counter)
            for event in pygame.event.get():
                text_input_5.handle_events(event)

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if buy_button.draw() == True:
                        object_choice = text_input_5.text
                        if object_choice :
                            global items
                            if object_choice in items:
                                global prices
                                global points_count
                                index = items.index(object_choice)
                                corresponding_prices = prices[index]
                                if points_count >= corresponding_prices:
                                    points_count -= corresponding_prices
                                    object_choice = ""
                                else :
                                    print("You do not have enough points to get this item.")


                    
                    if exit_button_5.draw() == True:
                        return  
            draw_text("Average prices for usable items using points :", 30, 75, black,font)
            draw_text("      Stationary: 25", 30, 100, black,font_tiny)
            draw_text("      Candy: 30", 30, 120,black,font_tiny)
            draw_text("      Books: 50", 30, 140, black,font_tiny)
            draw_text("      Chocolate: 30", 30, 160, black, font_tiny)
            draw_text("      Outside Food: 115", 30, 180, black, font_tiny)
            draw_text("      Makeup: 60", 30, 200, black, font_tiny)
            draw_text("      Sports: 50", 30, 220, black, font_tiny)
            draw_text("      Clothes: 55", 30, 240, black, font_tiny)
            draw_text("      Accessories: 35", 30, 260, black, font_tiny)
            draw_text("      Vedio Games: 95", 30, 280, black, font_tiny)
            draw_text("Please make sure you are using the correct exact replica of the items written",30, 320,black, font_tiny)
            draw_text("in the list as they are the different items that are part of our list and will",30, 340,black, font_tiny)
            draw_text("not work without the proper syntax , the syntax is the name only with the first",30, 360,black, font_tiny)
            draw_text("letter of each word which is an item name",30, 380,black, font_tiny)
            draw_text("Items to buy:", 375 , 250 , black , font_sub )

            text_input_5.draw()
            buy_button.draw()
            exit_button_5.draw()

            pygame.display.update()
def board_screen():
    while True:
         while True:
            
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if exit_button_4.draw() == True:
                        return  
            draw_leaderboard()

            exit_button_4.draw()

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
            draw_text("Your points can be used for various things.", 30, 100, white,font_tiny)
            draw_text("Depending on how many points your adding in a task, parents can let their", 30, 120, white,font_tiny)
            draw_text("children buy something they want for a set of points. For example if you add a lot of points for each task...like", 30, 140, white,font_tiny)
            draw_text("a 100 points just for dishwashing then your item could be expensive, else it could be cheap", 30, 160, white,font_tiny)


            draw_text("A few examples of things you can buy are:", 30, 200, white,font)
            draw_text("      1.Stationary: 5 - 50", 30, 240, white,font_tiny)
            draw_text("      2.Candy: 10 - 50", 30, 280,white,font_tiny)
            draw_text("      3.Books: 20 - 80", 30, 320, white,font_tiny)
            draw_text("      4.Chocolate: 10 - 50", 30, 360, white, font_tiny)
            draw_text("      5.Outside Food: 80 - 150", 30, 400, white, font_tiny)
            draw_text("      6.Makeup: 40-80", 30, 440, white, font_tiny)
            draw_text("      7.Sports: 40-60", 30, 480, white, font_tiny)
            draw_text("      8.Clothes: 40-70", 30, 520, white, font_tiny)
            draw_text("      9.Accessories: 20-50", 30, 560, white, font_tiny)
            draw_text("      10.Vedio Games: 70-120", 30, 600, white, font_tiny)
            
            exit_button.draw()

            pygame.display.update()
def chat_screen():
    running = True
    while running:
        screen.fill("#6082B6")
        global chat_history
        global user_input

            # Display chat history
        y_offset = 20
        for line in chat_history[-10:]:  # Show last 10 messages
            text_surface = font.render(line, True, blue if "ChoreBot:" in line else black)
            screen.blit(text_surface, (20, y_offset))
            y_offset += 25
    
        # Display user input
        input_surface = input_font.render(user_input, True, black)
        pygame.draw.rect(screen, (200, 200, 200), (20, screen_height - 50, screen_width - 130, 30))
        screen.blit(input_surface, (25, screen_height - 45))
    
        # Draw buttons
        send_button = pygame.draw.rect(screen, green, (screen_width- 100, screen_height - 50, 80, 30))
        clear_button = pygame.draw.rect(screen, red, (screen_width- 190, screen_height - 50, 80, 30))
    
        send_text = font.render("Send", True, white)
        screen.blit(send_text, (screen_width - 75, screen_height - 42))
        clear_text = font.render("Clear", True, white)
        screen.blit(clear_text, (screen_width - 165, screen_height - 42))
        pygame.display.flip()
    
            # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and user_input:
                    chat_history.append(f"You: {user_input}")
                    if user_input.lower() in ["exit", "bye", "quit"]:
                        chat_history.append("ChoreBot: Goodbye! Have a productive day. 👋")
                        pygame.time.delay(1000)
                        running = False
                    else:
                        chat_history.append(f"ChoreBot: {suggest_chore(user_input)}")
                    user_input = ""
                elif event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                else:
                    user_input += event.unicode
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if send_button.collidepoint(event.pos) and user_input:
                    chat_history.append(f"You: {user_input}")
                    chat_history.append(f"ChoreBot: {suggest_chore(user_input)}")
                    user_input = ""
                elif clear_button.collidepoint(event.pos):
                    chat_history = ["ChoreBot: Hello! Ask me what chores you can do. Type 'exit' to quit.",
                                "Questions to ask about: Cleaning, Laundry, Kitchen, General"]
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
    mart_button.draw()
    board_button.draw()
    struct_button.draw()
    chat_button.draw()
    shop_button.draw()
    start_button.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mart_button.draw() == True :
                mart_screen()
            if struct_button.draw() == True :
                struct_screen()
            if chat_button.draw() == True :
                chat_screen()
            if board_button.draw() == True :
                board_screen()
            if shop_button.draw() == True :
                shop_screen()
            if start_button.draw() == True :
                main_screen()
    draw_text("Point Manager", 186, 100, black , font_1)
    draw_text("Welcome to the point manager !" , 175 , 180, black , font_2) 
    draw_text("The button in the middle of the screen will take you to the" , 115 , 450, black , font) 
    draw_text("main page with our functions" , 115 , 470, black , font)
    draw_text("The button at the top left corner of the screen will show the " , 115 , 490, black , font) 
    draw_text("instructions on how to use the code," , 115 , 510, black , font)
    draw_text("ChoreBot - AI" , 475 , 520 , black , font_sub)
    pygame.display.flip()
    with open(total_points_file, 'w') as file:
        file.write(str(points_count))
    pygame.display.update()

pygame.quit()
sys.exit()
