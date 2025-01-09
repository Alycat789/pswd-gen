from random import randint
from random import shuffle
import string

class PasswordGen:
    """generates weak, medium, or strong passwords based on user input"""
    l = string.ascii_letters
    d = string.digits
    syms = [c for c in "~`! @#$%^&*()_-+={[}]|\:;\"'<,>.?/"]
    s = "".join(syms)

    def __init__(self, strength):
        self.strength = strength
        self.pswd = ""

    def __repr__(self):
        return self.pswd
    
    def get_char(self):
        if self.strength.lower() == "weak":
            s = list(PasswordGen.l)
            shuffle(s)
            length = 8
            pswd = s[:length]
            return pswd
        elif self.strength.lower() == "medium":
            s = list(PasswordGen.l + PasswordGen.d)
            shuffle(s)
            length = randint(9, 14)
            pswd = s[:length]
            return pswd
        elif self.strength.lower() == "strong":
            s = list(PasswordGen.l + PasswordGen.d + PasswordGen.s)
            shuffle(s)
            length = randint(15, 20)
            pswd = s[:length]
            return pswd
        
        
        
    def generate(self):
        self.pswd = "".join(self.get_char())
        if self.strength.lower() == 'weak':
            self.pswd = self.pswd.lower()


def main():
    message = "weak   = 8 lower case letters\nmedium = 9-14 uppercase/lowercase letters and numbers\nstrong = 15-20 uppercase/lowercase letters, numbers, and symbols"
    strength = input(f"{message}\n\nHow strong do you want your password? (weak, medium, strong): ")
    passW = PasswordGen(strength.strip())
    passW.generate()
    print(f"Your password is {passW.pswd}")

if __name__ == "__main__":
    main()
