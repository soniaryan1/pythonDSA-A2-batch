"""

rock paper scissors

computer choice = rock / paper /scissors

user_choice = input() rock/papaer/scissors

if
elif
elif

you won
you lost , the computer choose rock / paper/ scissors
you tied

"""

import random

options = ["rock", "paper", "scissors"]

computer_choice = random.choice(options)
user_choice = input("enter rock/paper/scissors = ")

if user_choice != "rock" and user_choice != "paper" and user_choice != "scissors":
    print("invalid")
elif user_choice == "rock" and computer_choice == "scissors":
    print("you won")
elif user_choice == "paper" and computer_choice == "rock":
    print("you won")
elif user_choice == "scissors" and computer_choice == "paper":
    print("you won")
elif user_choice == computer_choice:
    print("you tied")
else:
    print(f"you lost , computer choose {computer_choice}")
