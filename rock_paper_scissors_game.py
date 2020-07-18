from random import randint

choice = ["rock", "paper", "scissors"]

computer = choice[randint(0,2)]

print("Welcome to the Rock, Paper, Scissors game\n")

while True:
    player = input("Your Choice: \n").lower()
    print("Computer choose: \n"  +computer)

    if player == computer:
        print("Draw\n")
    elif player == "rock" and computer == "paper":
        print("Computer wins\n")
    elif player == "rock" and computer == "scissors":
        print("Player wins\n")
    elif player == "paper" and computer == "rock":
        print("Player wins\n")
    elif player == "paper" and computer == "scissors":
        print("Computer wins\n")
    elif player == "scissors" and computer == "rock":
        print("Computer wins\n")
    elif player == "scissors" and computer == "paper":
        print("Player wins\n") 
    else:
        print("You don't choose right. the game will be exit")
        exit(0)