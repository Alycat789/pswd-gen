from learning_example_0 import PassGen

def main():
    pg = PassGen()
    # print(pg.__cant_see)
    print(pg._PassGen__cant_see)
    print(pg.__dict__)

if __name__ == "__main__":
    main()

#  mangled __cant_see generates error if we try to call it
