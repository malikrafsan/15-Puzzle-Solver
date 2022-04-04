from CLI import CLI
from GUI import GUI


def main():
    """Main program
    """
    
    print("What interface do you want to use?")
    print("1. GUI")
    print("2. CLI")

    inp = int(input("Input: "))
    while (True):
        if (inp >= 1 and inp <= 2):
            break
        else:
            print("Wrong format, please enter 1 or 2")

    if (inp == 1):
        GUI().mainloop()
    else:
        CLI()


if __name__ == "__main__":
    main()
