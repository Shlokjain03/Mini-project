import tkinter as tk
import random

# Function to determine the winner
def determine_winner(user_input):
    global user_wins, computer_wins, draws
    options = ["rock", "paper", "scissors"]
    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    result = ""

    if user_input == "rock" and computer_pick == "scissors":
        result = "You won!"
        user_wins += 1
    elif user_input == "paper" and computer_pick == "rock":
        result = "You won!"
        user_wins += 1
    elif user_input == "scissors" and computer_pick == "paper":
        result = "You won!"
        user_wins += 1
    elif user_input == computer_pick:
        result = "It's a draw!"
        draws += 1
    else:
        result = "You lost!"
        computer_wins += 1

    result_label.config(text=f"Computer picked {computer_pick}. {result}")
    score_label.config(text=f"You: {user_wins} | Computer: {computer_wins} | Draws: {draws}")

# Function to handle button clicks
def on_button_click(choice):
    determine_winner(choice)

# Function to quit the game
def quit_game():
    root.quit()

# Initialize win counts
user_wins = 0
computer_wins = 0
draws = 0

# Create the main window
root = tk.Tk()
root.title("Rock Paper Scissors")

# Create and place widgets
instructions_label = tk.Label(root, text="Choose Rock, Paper, or Scissors:")
instructions_label.pack()

rock_button = tk.Button(root, text="Rock", command=lambda: on_button_click("rock"))
rock_button.pack()

paper_button = tk.Button(root, text="Paper", command=lambda: on_button_click("paper"))
paper_button.pack()

scissors_button = tk.Button(root, text="Scissors", command=lambda: on_button_click("scissors"))
scissors_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

score_label = tk.Label(root, text="You: 0 | Computer: 0 | Draws: 0")
score_label.pack()

quit_button = tk.Button(root, text="Quit", command=quit_game)
quit_button.pack()

# Start the main event loop
root.mainloop()
