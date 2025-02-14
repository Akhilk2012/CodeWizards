import random
import tkinter as tk
from tkinter import scrolledtext

chores = {
    "cleaning": ["Vacuum the living room", "Wipe down kitchen counters", "Dust the shelves"],
    "laundry": ["Wash clothes", "Fold laundry", "Sort socks"],
    "kitchen": ["Do the dishes", "Take out the trash", "Organize the fridge"],
    "general": ["Water the plants", "Feed the pets", "Declutter your workspace"],
    "chores" : ["Clean your room", "Walk your pets", "Help in cooking"]
}

def suggest_chore(query):
    """Find a relevant chore based on user input."""
    query = query.lower()
    
    for category in chores.keys():
        if category in query:
            return f"You can do this: {random.choice(chores[category])}"
    
    return "I don't have chores for that. Try asking about cleaning, laundry, kitchen, genral tasks.\n"

def send_message():
    """Handles sending user messages and displaying AI responses."""
    user_input = entry.get().strip()
    if not user_input:
        return
    
    chat_box.insert(tk.END, f"You: {user_input}\n")
    entry.delete(0, tk.END)

    if user_input.lower() in ["exit", "bye", "quit"]:
        chat_box.insert(tk.END, "ChoreBot: Goodbye! Have a productive day.\n")
        root.after(1000, root.destroy)  # Close the window after a delay
    else:
        response = suggest_chore(user_input)
        chat_box.insert(tk.END, f"ChoreBot: {response}\n")

def clear_chat():
    """Clears the chat window."""
    chat_box.delete("1.0", tk.END)

# ui gen for the chat window
root = tk.Tk()
root.title("ChoreBot - AI Chatbox")
root.geometry("400x500")

# rendor the bot on the screen
chat_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20)
chat_box.pack(padx=10, pady=10)
chat_box.insert(tk.END, "ChoreBot: Hello! Ask me what chores you can do. Type 'exit' to quit.\n")
chat_box.insert(tk.END, 'Questons to ask about: \n')
chat_box.insert(tk.END, '\nCleaning \nlaundry \nkitchen \ngeneral \nchores')

# Create input for user area
entry = tk.Entry(root, width=40)
entry.pack(pady=5)

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack()

clear_button = tk.Button(root, text="Clear", command=clear_chat)
clear_button.pack()

# run loop function
root.mainloop()