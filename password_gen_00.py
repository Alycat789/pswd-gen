from random import randint

class PasswordGenerator:
    """generates weak, medium, or strong passwords based on user input"""

    def __init__(self, strength):
        self.strength = strength
        self.pswd = ""

    def __str__(self):
        return self.pswd
        
    def generate(self):
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        symbol = ['!', '@', '#', '$', '%', '^', '&', '*']
        if self.strength == 'weak':
            pick = randint(0, 6)
            words = ["Password", "Keyboard", "Computer", "Printer", "Work", "Puppy", "Kitty"]
            self.pswd = words[pick]
        elif self.strength == 'medium':
            pswd = []
            l = randint(10, 14)
            for _ in range(1, l):
                if _ % 2 == 0:
                    pick = randint(0, len(alphabet))
                    cap = randint(0, 1)
                    if cap == 0:
                        pswd.append(alphabet[pick])
                    else:
                        pswd.append(alphabet[pick].title())
                else:
                    num = randint(0, 9)
                    pswd.append(str(num))
            self.pswd = "".join(pswd)
        else:
            pswd = []
            l = randint(15, 22)
            if l > 18:
                a, b, c, d = 5, 11, 17, 19
            else:
                a, b, c, d = 3, 9, 13, 15
            for _ in range(1, l):
                if _ % 2 == 0:
                    pick = randint(0, len(alphabet))
                    cap = randint(0, 1)
                    if cap == 0:
                        pswd.append(alphabet[pick])
                    else:
                        pswd.append(alphabet[pick].title())
                elif _ == a or _ == b or _ == c or _ == d:
                    pick = randint(0, len(symbol))
                    pswd.append(symbol[pick])
                else:
                    num = randint(0, 9)
                    pswd.append(str(num))
            result = "".join(pswd)
            flip = randint(0, 1)
            if flip:
                self.pswd = result[::-1]
            else:
                self.pswd = result


def main():
    strength = input("How strong do you want your password? (weak, medium, strong): ")
    passW = PasswordGenerator(strength.strip())
    passW.generate()
    print(f"Your password is {passW.pswd}")

if __name__ == "__main__":
    main()
