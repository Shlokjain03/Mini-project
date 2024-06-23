import tkinter as tk
from tkinter import messagebox

# Function to check the answers and show the result
def check_answers():
    score = 0
    if entry1.get().lower() == "python":
        score += 1
    if entry2.get().lower() == "central processing unit":
        score += 1
    if entry3.get().lower() == "graphic processing unit":
        score += 1
    if entry4.get().lower() == "random access memory":
        score += 1
    messagebox.showinfo("Results", f"You got {score} questions correct!\nYou got {(score / 4) * 100} %.")

# Function to quit the game
def quit_game():
    root.destroy()

# Function to start the game
def start_game():
    label1.pack()
    entry1.pack()
    label2.pack()
    entry2.pack()
    label3.pack()
    entry3.pack()
    label4.pack()
    entry4.pack()
    submit_button.pack()

# Create the main window
root = tk.Tk()
root.title("Computer Quiz Game")

# Create widgets
welcome_label = tk.Label(root, text="Welcome to my computer game!")
question_label = tk.Label(root, text="Do you want to play?")
start_button = tk.Button(root, text="Yes", command=start_game)
quit_button = tk.Button(root, text="No", command=quit_game)

# Create question widgets
label1 = tk.Label(root, text="Which language is this code written in?")
entry1 = tk.Entry(root)

label2 = tk.Label(root, text="What does CPU stand for?")
entry2 = tk.Entry(root)

label3 = tk.Label(root, text="What does GPU stand for?")
entry3 = tk.Entry(root)

label4 = tk.Label(root, text="What does RAM stand for?")
entry4 = tk.Entry(root)

submit_button = tk.Button(root, text="Submit", command=check_answers)

# Pack the welcome widgets
welcome_label.pack()
question_label.pack()
start_button.pack()
quit_button.pack()

# Run the main event loop
root.mainloop()
