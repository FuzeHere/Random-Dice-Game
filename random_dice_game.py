port random

while True:
    ask = input("Do you want roll the dice? (y/n): ").lower()
    if ask == "y":
        roll_1 = random.randint(1, 6)
        roll_2 = random.randint(1, 6)
        total = roll_1 + roll_2
        print(f"The dice shows ({roll_1}, {roll_2}) and you got in total: {total}")
    elif ask == "n":
        print("Okay see u next game ^^")
        break
    else:
        print("Invalid Choice, Try Again With y/n!")
