import random

import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        print("Invalid option")
        continue

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]  
    print("Computer picked", computer_pick + ".")  

    if user_input == "rock" and computer_pick == "scissors":
        print(Fore.GREEN + "You win!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print(Fore.GREEN + "You win!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print(Fore.GREEN + "You win!")
        user_wins += 1

    elif user_input == computer_pick:
        print("Draw!")

    else:
        print(Fore.RED + "You lost!")
        computer_wins += 1

print("You won", user_wins, "time(s).")
print("The computer won", computer_wins, "time(s).")  
print("Goodbye!")