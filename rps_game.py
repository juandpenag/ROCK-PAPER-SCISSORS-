"""ROCK-PAPER-SCISSORS"""
import random

print("*" * 20)
print("ROCK-PAPER-SCISSORS!!!")
print("*" * 20)
print("Welcome!")
print("*" * 20)

# Variables:
option = ("rock", "paper", "scissors")
ROUND= 1
USU = 0
COM = 0

# Fundamental condition
while USU or COM <= 2:
    computer = random.choice(option)
    print("ROUND",ROUND)
    print("*" * 20)
    print("User: ", USU, "Computer: ", COM)
    print("*" * 20)
# User variable:
    user = (input("¿What's your choice? ").lower())
    print("*" * 20)
    if user in option:
# If draw
        if user in computer:
            print("Draw.")
            print("*" * 20)
# If user wins:
        elif user == "rock" and computer == "scissors" == True:
            print("You WIN!")
            print("*" * 20)
            USU = USU + 1
        elif user == "paper" and computer == "rock" == True:
            print("You WIN!")
            print("*" * 20)
            USU = USU + 1
        elif user == "scissors" and computer == "paper" == True:
            print("You WIN!")
            print("*" * 20)
            USU = USU + 1
# If computer wins:
        else:
            print("You lose.")
            print("*" * 20)
            COM = COM + 1
    print(f"User: {user}. Computer: {computer}.")
    print("*" * 20)
    ROUND += 1

# Result
    if (USU or COM) == 2:
        break

if USU == 2:
    print("YOU ARE THE WINNER!")
    print("*" * 20)
    print(f"Resultado: {USU} vs. {COM}.")
    print("*" * 20)

else:
    print("You lose.")
    print("*" * 20)
    print(f"Result: {USU} vs. {COM}.")
    print("*" * 20)
