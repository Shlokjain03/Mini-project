import tkinter as tk
from tkinter import messagebox

class AdventureGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Adventure Game")
        self.name = ""
        
        self.label = tk.Label(root, text="Type your name:")
        self.label.pack()
        
        self.entry = tk.Entry(root)
        self.entry.pack()
        
        self.start_button = tk.Button(root, text="Start", command=self.start_adventure)
        self.start_button.pack()
    
    def start_adventure(self):
        self.name = self.entry.get()
        if not self.name:
            messagebox.showerror("Error", "Please enter your name.")
            return
        
        self.label.config(text=f"Welcome {self.name} to this adventure!")
        self.entry.pack_forget()
        self.start_button.pack_forget()
        
        self.label.config(text="You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go?")
        self.left_button = tk.Button(root, text="Left", command=self.go_left)
        self.left_button.pack(side=tk.LEFT)
        self.right_button = tk.Button(root, text="Right", command=self.go_right)
        self.right_button.pack(side=tk.RIGHT)
    
    def go_left(self):
        self.clear_buttons()
        self.label.config(text="You come to a river, you can walk around it or swim across? Type walk to walk around and swim to swim across:")
        self.walk_button = tk.Button(root, text="Walk", command=self.walk)
        self.walk_button.pack(side=tk.LEFT)
        self.swim_button = tk.Button(root, text="Swim", command=self.swim)
        self.swim_button.pack(side=tk.RIGHT)
    
    def go_right(self):
        self.clear_buttons()
        self.label.config(text="You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)?")
        self.cross_button = tk.Button(root, text="Cross", command=self.cross)
        self.cross_button.pack(side=tk.LEFT)
        self.back_button = tk.Button(root, text="Back", command=self.back)
        self.back_button.pack(side=tk.RIGHT)
    
    def walk(self):
        self.clear_buttons()
        messagebox.showinfo("Result", "You walked for many miles, ran out of water and you lost the game.")
        self.end_game()
    
    def swim(self):
        self.clear_buttons()
        messagebox.showinfo("Result", "You swam across and were eaten by an alligator.")
        self.end_game()
    
    def cross(self):
        self.clear_buttons()
        self.label.config(text="You cross the bridge and meet a stranger. Do you talk to them (yes/no)?")
        self.yes_button = tk.Button(root, text="Yes", command=self.talk)
        self.yes_button.pack(side=tk.LEFT)
        self.no_button = tk.Button(root, text="No", command=self.ignore)
        self.no_button.pack(side=tk.RIGHT)
    
    def back(self):
        self.clear_buttons()
        messagebox.showinfo("Result", "You go back and lose.")
        self.end_game()
    
    def talk(self):
        self.clear_buttons()
        messagebox.showinfo("Result", "You talk to the stranger and they give you gold. You WIN!")
        self.end_game()
    
    def ignore(self):
        self.clear_buttons()
        messagebox.showinfo("Result", "You ignore the stranger and they are offended and you lose.")
        self.end_game()
    
    def clear_buttons(self):
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Button):
                widget.pack_forget()
    
    def end_game(self):
        self.label.config(text=f"Thank you for trying, {self.name}")
        self.restart_button = tk.Button(root, text="Restart", command=self.restart)
        self.restart_button.pack()
    
    def restart(self):
        self.clear_buttons()
        self.label.config(text="Type your name:")
        self.entry.pack()
        self.start_button.pack()

root = tk.Tk()
game = AdventureGame(root)
root.mainloop()
