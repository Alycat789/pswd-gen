from random import randint
from secrets import choice
# choice is more secure than using shuffle
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
        return self.pswd
    
    def get_char(self) -> str:
        if self.strength[0].lower() == "w":
            s = list(PasswordGen.letters)
            self.length = 8
            return [choice(s) for _ in range(self.length)]
        elif self.strength[0].lower() == "m":
            s = list(PasswordGen.letters + PasswordGen.digits)
            self.length = randint(9, 14)
            return [choice(s) for _ in range(self.length)]
        elif self.strength[0].lower() == "s":
            s = list(PasswordGen.letters + PasswordGen.digits + PasswordGen.symbols)
            self.length = randint(15, 20)
            return [choice(s) for _ in range(self.length)]
        
    def generate(self) -> str:
        self.pswd = "".join(self.get_char())
        if self.strength[0].lower() == 'w':
            self.pswd = self.pswd.lower()


def main():
    message = "weak   = 8 lowercase letters\nmedium = 9-14 uppercase/lowercase letters and numbers\nstrong = 15-20 uppercase/lowercase letters, numbers, and symbols"
    strength = input(f"{message}\n\nHow strong do you want your password? (weak, medium, strong): ")
    passW = PasswordGen(strength.strip())
    passW.generate()
    print(f"Your password is {passW}")

if __name__ == "__main__":
    main()
