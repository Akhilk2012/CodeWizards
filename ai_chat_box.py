import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Set up the window
WIDTH, HEIGHT = 640, 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ChoreBot - AI Chatbox")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (50, 100, 255)
GREEN = (76, 175, 80)
RED = (244, 67, 54)

# Fonts
font = pygame.font.Font(None, 24)
input_font = pygame.font.Font(None, 28)

# Chore categories
chores = {
    "cleaning": ["Vacuum the living room", "Wipe down kitchen counters", "Dust the shelves", "Mop the floors", "Clean the windows", "Organize the bookshelf"],
    "laundry": ["Wash clothes", "Fold laundry", "Sort socks", "Iron clothes", "Wash bed sheets"],
    "kitchen": ["Do the dishes", "Take out the trash", "Organize the fridge", "Scrub the sink", "Wipe the stove"],
    "general": ["Water the plants", "Feed the pets", "Declutter your workspace", "Clean your room", "Walk your pets", "Help in cooking", "Make your bed"]
}

# Function to suggest a chore
def suggest_chore(query):
    query = query.lower()
    for category, tasks in chores.items():
        if category in query:
            return f"You can do this: {random.choice(tasks)}"
    return "I don't have chores for that. Try asking about Cleaning, Laundry, Kitchen, or General tasks."

# Chat history
chat_history = ["ChoreBot: Hello! Ask me what chores you can do. Type 'exit' to quit.",
                "Questions to ask about: Cleaning, Laundry, Kitchen, General"]
user_input = ""

running = True
while running:
    screen.fill(WHITE)
    
    # Display chat history
    y_offset = 20
    for line in chat_history[-10:]:  # Show last 10 messages
        text_surface = font.render(line, True, BLUE if "ChoreBot:" in line else BLACK)
        screen.blit(text_surface, (20, y_offset))
        y_offset += 25
    
    # Display user input
    input_surface = input_font.render(user_input, True, BLACK)
    pygame.draw.rect(screen, (200, 200, 200), (20, HEIGHT - 50, WIDTH - 130, 30))
    screen.blit(input_surface, (25, HEIGHT - 45))
    
    # Draw buttons
    send_button = pygame.draw.rect(screen, GREEN, (WIDTH - 100, HEIGHT - 50, 80, 30))
    clear_button = pygame.draw.rect(screen, RED, (WIDTH - 190, HEIGHT - 50, 80, 30))
    
    send_text = font.render("Send", True, WHITE)
    screen.blit(send_text, (WIDTH - 75, HEIGHT - 42))
    clear_text = font.render("Clear", True, WHITE)
    screen.blit(clear_text, (WIDTH - 165, HEIGHT - 42))
    
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

pygame.quit()
sys.exit()
clear_button.grid(row=0, column=1, padx=5, pady=5)

root.mainloop()
