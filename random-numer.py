import random


def computer_guess_the_number(x):

    print("////////////////////////////////////////")
    print(" Welcome to the game. ")
    print("////////////////////////////////////////")
    print(f"You need to select a number between 1 and {x} for the computer to guess...")

    inferior_limit = 1
    superior_limit = x

    answer = ""
    while answer != "c":
        if inferior_limit != superior_limit:
            prediction = random.randint(inferior_limit, superior_limit)
        else:
            prediction = superior_limit

        answer = input(f"My prediction is {prediction}. If its too high, type (A). If its too low type (B). If its right type (C)").lower()

        if answer == "a":
            superior_limit = prediction - 1
        elif answer == "b":
            inferior_limit = prediction + 1

    print(f"The computer has guessed the number {prediction} correctly.")


computer_guess_the_number(10)