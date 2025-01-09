# now add a GUI
# think about adding extra options for personalizing the password
from tkinter import *
from random import randint
from secrets import choice
import string

class PasswordGen:
    """generates weak, medium, or strong passwords based on user input"""
    letters = string.ascii_letters
    digits = string.digits
    symbols = "~`!@#$%^&*_-+=()[]}{|\:;\"'<,>.?/"

    def __init__(self, strength: str):
        self.strength = strength
        self.pswd = ""
        self.length = 0

    def __repr__(self):
        return self.generate()
    
    def get_char(self) -> str:
        if self.strength == 1:
            s = list(PasswordGen.letters)
            self.length = 8
            return [choice(s) for _ in range(self.length)]
        elif self.strength == 2:
            s = list(PasswordGen.letters + PasswordGen.digits)
            self.length = randint(9, 14)
            return [choice(s) for _ in range(self.length)]
        elif self.strength == 3:
            s = list(PasswordGen.letters + PasswordGen.digits + PasswordGen.symbols)
            self.length = randint(15, 20)
            return [choice(s) for _ in range(self.length)]
        
    def generate(self) -> str:
        self.pswd = "".join(self.get_char())
        if self.strength == 1:
            self.pswd = self.pswd.lower()
        return self.pswd


def main():
    def on_click_button(event):
        if v.get() == 1:
            pg = PasswordGen(1)
        elif v.get() == 2:
            pg = PasswordGen(2)
        elif v.get() == 3:
            pg = PasswordGen(3)
        p_label = Label(root, text = "Password: ")
        p_label.grid(row = 3, column = 0)
        pswd = Entry(root)
        pswd.grid(row = 3, column = 1, columnspan = 2)
        pswd.insert(0, pg)
    root = Tk()
    root.title("Password Generator")
    msg = Label(root, text = "    How strong do you want your password? :    ")
    msg.grid(row = 0, columnspan = 3)
    v = IntVar()
    Radiobutton(root, text = "weak", variable = v, value = 1).grid(row = 1, column = 0)
    Radiobutton(root, text = "medium", variable = v, value = 2).grid(row = 1, column = 1)
    Radiobutton(root, text = "strong", variable = v, value = 3).grid(row = 1, column = 2)
    run = Button(root, text = "Create", activebackground = "blue", activeforeground = "gray")
    run.grid(row = 2, column = 1)
    
    run.bind("<Button-1>", on_click_button)
    mainloop()

if __name__ == "__main__":
    main()