import random
import tkinter as tk
from tkinter import simpledialog, messagebox

def start_game():
    top_of_range = simpledialog.askstring("Input", "Type a number:")
    if top_of_range and top_of_range.isdigit():
        top_of_range = int(top_of_range)
        if top_of_range <= 0:
            messagebox.showwarning("Invalid input", "Please type a number larger than 0 next time.")
            return
    else:
        messagebox.showwarning("Invalid input", "Please type a number next time.")
        return

    random_number = random.randint(0, top_of_range)
    guesses = 0

    def make_guess():
        nonlocal guesses
        nonlocal random_number
        user_guess = entry.get()
        if user_guess.isdigit():
            user_guess = int(user_guess)
        else:
            messagebox.showwarning("Invalid input", "Please type a number next time.")
            return

        guesses += 1
        if user_guess == random_number:
            messagebox.showinfo("Result", f"You got it in {guesses} guesses!")
            root.quit()
        elif user_guess > random_number:
            result_label.config(text="You were above the number!")
        else:
            result_label.config(text="You were below the number!")

    root = tk.Tk()
    root.title("Number Guessing Game")

    prompt_label = tk.Label(root, text="Make a guess:")
    prompt_label.pack()

    entry = tk.Entry(root)
    entry.pack()

    guess_button = tk.Button(root, text="Guess", command=make_guess)
    guess_button.pack()

    result_label = tk.Label(root, text="")
    result_label.pack()

    root.mainloop()

if __name__ == "__main__":
    start_game()
