import string
from random import shuffle

class PassGen:
    l = string.ascii_letters
    d = string.digits
    # p = string.punctuation

    # l = [chr(i) for i in range(ord("a"), ord("z") + 1)] + [chr(i) for i in range(ord("A"), ord("Z") + 1)]
    # d = [str(i) for i in range(10)]
    p = [c for c in "~!@$%^&*()-_}][{|/?\\>.<,"]

    def __init__(self):
        # print(string.digits)
        self.pwd = ""
        self.__cant_see = "I'm hidden!"

    def __repr__(self):
        # "represent" like __str__ but more versatile
        return self.pwd

    def _get_chars(self, strength="strong"):
        if strength == "strong":
            s = list(PassGen.l + PassGen.d + str(PassGen.p))
            shuffle(s)
            return s

    def generate(self, strength="strong"):
        return "".join(self._get_chars(strength)[:16])
    
def main():
    pg = PassGen()
    print(pg.generate())

if __name__ == "__main__":
    main()
