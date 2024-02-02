import random as rand
player_choice = input("Enter rock, paper, or scissors: ")
arr = ["rock", "paper", "scissors"]
computer_choice = rand.choice(arr)
if player_choice not in ["rock", "paper", "scissors"]:
    print("please input a choice of rock, paper or scissors")
elif computer_choice == "rock" and player_choice == "paper":
    print("computer chose rock")
    print("you win!")
elif computer_choice == "rock" and player_choice == "scissors":
    print("computer chose rock")
    print("you lose. LOL")
elif computer_choice == "paper" and player_choice == "scissors":
    print("computer chose paper")
    print("you lose. LOL")
elif computer_choice == "paper" and player_choice == "rock":
    print("computer chose paper")
    print("you win!")
elif computer_choice == "scissors" and player_choice == "rock":
    print("computer chose scissors")
    print("you win!")
elif computer_choice == "scissors" and player_choice == "paper":
    print("computer chose scissors")
    print("you lose. LOL")
elif computer_choice == player_choice:
    print(f"computer chose {computer_choice}")
    print("A fucking drawwww!!!")
else:
    print("play again?")