import random
def dicerolling(int):

    dicenumber = []
    for val in range(int):
        i = random.randint(1,6)
        dicenumber.append(i)

    for num in dicenumber:

        if (num ==1):
            print("┌─────────┐\n"
                "│         │\n"
                "│    ●    │\n"
                "│         │\n"
                "└─────────┘")

        elif (num == 2):
            print("┌─────────┐\n"
                "│  ●      │\n"
                "│         │\n"
                "│      ●  │\n"
                "└─────────┘")

        elif (num == 3):
            print("┌─────────┐\n"
                "│  ●      │\n"
                "│    ●    │\n"
                "│      ●  │\n"
                "└─────────┘")

        elif (num == 4):
            print("┌─────────┐\n"
                "│  ●   ●  │\n"
                "│         │\n"
                "│  ●   ●  │\n"
                "└─────────┘")

        elif (num == 5):
            print("┌─────────┐\n"
                "│  ●   ●  │\n"
                "│    ●    │\n"
                "│  ●   ●  │\n"
                "└─────────┘")

        else:
            print("┌─────────┐\n"
                "│  ●   ●  │\n"
                "│  ●   ●  │\n"
                "│  ●   ●  │\n"
                "└─────────┘")

dicerolling(int(input("How many dice do you want to roll? ")))