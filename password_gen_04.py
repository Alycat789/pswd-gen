# think about adding extra options for personalizing the password
from tkinter import *
from random import randint
from secrets import choice
import string

"""A Password Generator

An application, run through a GUI, that provides options to create any kind of password that you would like. 
Choose strong, medium, weak, or custom."""

class PasswordGen:
    """generates weak, medium, or strong passwords based on user input"""
    letters = string.ascii_letters
    digits = string.digits
    symbols = "~`!@#$%^&*_-+=()[]}{|\:;\"'<,>.?/"

    def __init__(self, strength: str, length = 0, l_case = 0, letters = False, digits = False, symbols = False):
        self.strength = strength
        self.pswd = ""
        self.length = length
        # below are only used if strength == custom
        self.l_case = l_case
        self.letter = letters
        self.digit = digits
        self.symbol = symbols

    def __repr__(self):
        """returns a password string specific to the current settings in the UI"""
        return self.generate()
    
    def custom(self) -> str:
        """returns a custom pswd as a list, dependent on current selected settings. 
        first compiles a list of all possible characters, then randomly selects characters to fill the desired length"""
        c = []
        if self.letter:
            for l in PasswordGen.letters:
                c.append(l)
        if self.digit:
            for d in PasswordGen.digits:
                c.append(d)
        if self.symbol:
            for s in PasswordGen.symbols:
                c.append(s)
        return [choice(c) for _ in range(int(self.length))]

    def case(self, string) -> str:
        """changes the case of letters in the object depending on current settings"""
        if self.l_case == 1:
            return string.upper()
        if self.l_case == 2:
            return string.lower()
    
    def get_char(self) -> str:
        """returns the pswd of a specific strength type as a list. 
        generates a list of all possible characters, randomly selects from that list to desired length"""
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
        """calls custom() or get_char() and converts the returned list pswd to a string
        returns final pswd in string form"""
        if self.strength == 4:
            self.pswd = "".join(self.custom())
            if self.l_case != 0:
                self.pswd = self.case(self.pswd)
        else:
            self.pswd = "".join(self.get_char())
            if self.strength == 1:
                self.pswd = self.pswd.lower()
        return self.pswd

class Interface:
    """creates a GUI environment for a user to interact with the PasswordGen class"""

    def __init__(self):
        self.root = Tk()
        self.strength = IntVar()

    def custom(self):
        """creates and operates a separate window for custom strength level options: 
        character type, length, and case
        event for button creates error or sends created pswd back to the root window"""
        custom = Toplevel()
        custom.title("Custom Password Options")
        opt = Label(custom, text = "Options: ")
        opt.grid(row = 0, column = 0, columnspan = 5)
        include = Label(custom, text = "Include: ")
        include.grid(row = 1, column = 0)
        digits = IntVar()
        letters = IntVar()
        symbols = IntVar()
        Checkbutton(custom, text = "digits", variable = digits).grid(row = 2, column = 2)
        Checkbutton(custom, text = "letters", variable = letters).grid(row = 2, column = 3)
        Checkbutton(custom, text = "symbols", variable = symbols).grid(row = 2, column = 4)
        length_label = Label(custom, text = "Length (>5): ")
        length_label.grid(row = 3, column = 0)
        length = Spinbox(custom, from_ = 5, to = 25, width = 10)
        length.grid(row = 4, column = 1)

        # learn how to gray out the case options until letters checkbox has been ticked
        case_label = Label(custom, text = "Case: ")
        case_label.grid(row = 5, column = 0)
        case = IntVar()
        Radiobutton(custom, text = "both", variable= case, value = 0).grid(row = 6, column = 2)
        Radiobutton(custom, text = "upper", variable= case, value = 1).grid(row = 6, column = 3)
        Radiobutton(custom, text = "lower", variable= case, value = 2).grid(row = 6, column = 4)

        run_custom = Button(custom, text = "Create", activebackground = "blue", activeforeground = "gray")
        run_custom.grid(row = 8, column = 2)
        spacer = Label(custom, text = "  ")
        spacer.grid(row = 8, column = 4)

        run_custom.bind("<Button-1>", lambda event: self.on_custom_create(event, digits.get(), letters.get(), symbols.get(), length.get(), case.get()))


    def on_custom_create(self, event, dig, let, sym, len, case):
        """event reaction to the create button in the custom window
        generates an error message if no character type is selected in the custom window OR
        creates the custom pswd object and displays it on the root window"""
        if dig == False and let == False and sym == False:
            err = Toplevel()
            err.title("Error")
            err_label = Label(err, text = "Password must include one of the following:\nletters, digits, symbols")
            err_label.pack()
        else:
            pg = PasswordGen(4, length = len, l_case = case, letters = let, digits = dig, symbols = sym)
            p_label = Label(self.root, text = "Password: ")
            p_label.grid(row = 3, column = 0)
            pswd = Entry(self.root, width = 30)
            pswd.grid(row = 3, column = 1, columnspan = 3)
            pswd.insert(0, pg)

    def on_click_create(self, event):
        """event for create button on root window
        creates a pswd object of desired strength 
        displays created pswd at bottom of window"""
        if self.strength.get() == 4:
            self.custom()
        else:
            if self.strength.get() == 1:
                pg = PasswordGen(1)
            elif self.strength.get() == 2:
                pg = PasswordGen(2)
            elif self.strength.get() == 3:
                pg = PasswordGen(3)
            p_label = Label(self.root, text = "Password: ")
            p_label.grid(row = 3, column = 0)
            pswd = Entry(self.root, width = 30)
            pswd.grid(row = 3, column = 1, columnspan = 3)
            pswd.insert(0, pg)

    def build(self):
        """creates root window
        includes strength options, 'create' button, and event for button to run program"""
        self.root.title("Password Generator")
        msg = Label(self.root, text = "    How strong do you want your password? : (custom opens a new window, result will be shown below.)   ")
        msg.grid(row = 0, columnspan = 5)
        Radiobutton(self.root, text = "weak", variable = self.strength, value = 1).grid(row = 1, column = 1)
        Radiobutton(self.root, text = "medium", variable = self.strength, value = 2).grid(row = 1, column = 2)
        Radiobutton(self.root, text = "strong", variable = self.strength, value = 3).grid(row = 1, column = 3)
        Radiobutton(self.root, text = "custom", variable = self.strength, value = 4).grid(row = 1, column = 4)
        run = Button(self.root, text = "Create", activebackground = "blue", activeforeground = "gray")
        run.grid(row = 2, column = 2)
        
        run.bind("<Button-1>", self.on_click_create)
        mainloop()

def main():
    window = Interface()
    window.build()

if __name__ == "__main__":
    main()