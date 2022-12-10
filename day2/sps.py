#!/usr/bin/python3
import random

player1 = input("Select rock, paper, or scissor :").lower()
player2 = random.choice(["Rock", "Paper", "Scissor"]).lower()
print("Player 1 selected : ", player1)
print("Player 2 selected : ", player2)

if player1 == "rock" and player2 == "paper":
    print("Player 2 Won")
elif player1 == "paper" and player2 == "scissor":
    print("Player 2 Won")
elif player1 == "scissor" and player2 == "rock":
    print("Player 2 Won")
elif player1 == player2:
    print("Tie")
else:
    print("Player 1 Won")
