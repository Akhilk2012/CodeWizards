import random
import tkinter as tk
from tkinter import scrolledtext

# Dictionary of chores categorized
chores = {
    "cleaning": ["Vacuum the living room", "Wipe down kitchen counters", "Dust the shelves", "Mop the floors", "Clean the windows", "Organize the bookshelf"],
    "laundry": ["Wash clothes", "Fold laundry", "Sort socks", "Iron clothes", "Wash bed sheets"],
    "kitchen": ["Do the dishes", "Take out the trash", "Organize the fridge", "Scrub the sink", "Wipe the stove"],
    "general": ["Water the plants", "Feed the pets", "Declutter your workspace", "Clean your room", "Walk your pets", "Help in cooking", "Make your bed"]
}

def suggest_chore(query):
    """Finds a relevant chore based on user input."""
    query = query.lower()

    for category, tasks in chores.items():
        if category in query:
            return f"You can do this: {random.choice(tasks)}"

    return "I don't have chores for that. Try asking about Cleaning, Laundry, Kitchen, or General tasks.\n"

def send_message(event=None):
    """Handles user input, sends messages, and displays responses."""
    user_input = entry.get().strip()
    if not user_input:
        return

    chat_box.insert(tk.END, f"You: {user_input}\n", "user")
    entry.delete(0, tk.END)

    if user_input.lower() in ["exit", "bye", "quit"]:
        chat_box.insert(tk.END, "ChoreBot: Goodbye! Have a productive day. 👋\n", "bot")
        root.after(1000, root.destroy)  # Close the window after 1 second
    else:
        response = suggest_chore(user_input)
        chat_box.insert(tk.END, f"ChoreBot: {response}\n\n", "bot")

def clear_chat():
    """Clears the chat window."""
    chat_box.delete("1.0", tk.END)
    chat_box.insert(tk.END, welcome_message, "bot")

# UI setup
root = tk.Tk()
root.title("ChoreBot - AI Chatbox")
root.geometry("450x500")
root.resizable(False, False)
root.configure(bg="#f4f4f4")

# Chat box with scrolling
chat_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=55, height=20, font=("Arial", 12))
chat_box.pack(padx=10, pady=10)
chat_box.tag_config("bot", foreground="blue", font=("Arial", 12, "italic"))
chat_box.tag_config("user", foreground="black", font=("Arial", 12, "bold"))

# Welcome message
welcome_message = "ChoreBot: Hello! Ask me what chores you can do. Type 'exit' to quit.\n\n" \
                  "Questions to ask about:\n- Cleaning\n- Laundry\n- Kitchen\n- General\n\n"
chat_box.insert(tk.END, welcome_message, "bot")

# User input field
entry = tk.Entry(root, width=50, font=("Arial", 12))
entry.pack(pady=5)
entry.bind("<Return>", send_message)  # Allows Enter key to send message

# Buttons
button_frame = tk.Frame(root, bg="#f4f4f4")
button_frame.pack()

send_button = tk.Button(button_frame, text="Send", command=send_message, font=("Arial", 12), bg="#4CAF50", fg="white", width=10)
send_button.grid(row=0, column=0, padx=5, pady=5)

clear_button = tk.Button(button_frame, text="Clear", command=clear_chat, font=("Arial", 12), bg="#f44336", fg="white", width=10)
clear_button.grid(row=0, column=1, padx=5, pady=5)

# Run the application
root.mainloop()
