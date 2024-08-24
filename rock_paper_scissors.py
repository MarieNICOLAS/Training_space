import random

player_wins = 0
computer_wins = 0

while player_wins <2 or player_wins <2:
    print("Let's play rock, paper or scissors")
    player_choice = input("Choose rock, paper, scissors: ").lower()

    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    print(f"Computer choose: {computer_choice}")

    if (player_choice == "rock" and computer_choice == "scissors") or (
    player_choice == "scissors" and computer_choice == "paper") or (player_choice == "paper" and computer_choice == "rock"):
        winner = "player"

    elif player_choice == computer_choice:
        winner = "tie"

    else:
        winner = "computer"

    if winner == "player":
        print("You won!")
        player_wins += 1
        print(f"Current Score - Player: {player_wins}, Computer: {computer_wins}")
    elif winner == "computer":
        print("Computer won")
        computer_wins += 1
        print(f"Current Score - Player: {player_wins}, Computer: {computer_wins}")
    else:
        print("It's tie")
        print(f"Current Score - Player: {player_wins}, Computer: {computer_wins}")

if player_wins > computer_wins:
    print("Congratulation! You won!!")
else:
    print("Computer won...")