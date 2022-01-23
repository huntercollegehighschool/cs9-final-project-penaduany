import os
Player = input("What is your name? ")
Playerwins = 0
CPUwins = 0
Rounds = int(input("How many rounds would you like to play? "))
Roundsplayed = 0
import time
while Rounds > Roundsplayed:
  PlayerChoice = input("Rock, Paper, or Scissors? ")
  if PlayerChoice != "Rock" and PlayerChoice != "rock" and PlayerChoice != "Paper" and PlayerChoice != "paper" and PlayerChoice != "Scissors" and PlayerChoice != "scissors":
    print("That is not a valid choice. ")
    PlayerChoice = input("Rock, Paper, or Scissors? ")
  if PlayerChoice == "Rock" or PlayerChoice == "rock" or PlayerChoice == "Paper" or PlayerChoice == "paper" or PlayerChoice == "Scissors" or PlayerChoice == "scissors":
    import random
  possible_actions = ["rock", "paper", "scissors"]
  ComputerChoice = random.choice(possible_actions)
  if PlayerChoice == "Rock" or PlayerChoice == "rock" and ComputerChoice == "scissors":
    print("The Computer selected", ComputerChoice, ".")
    print(Player, "Wins!")
    Playerwins = Playerwins + 1
    Roundsplayed = Roundsplayed + 1
  elif PlayerChoice == "Rock" or PlayerChoice == "rock" and ComputerChoice == "rock":
    print("The Computer selected", ComputerChoice, ".")
    print("Tie!")
    Roundsplayed = Roundsplayed + 1
  elif PlayerChoice == "Rock" or PlayerChoice == "rock" and ComputerChoice == "paper":
    print("The Computer selected", ComputerChoice,".")
    print("Cpu Wins!")
    CPUwins = CPUwins + 1
    Roundsplayed = Roundsplayed + 1
  elif PlayerChoice == "Paper" or PlayerChoice == "paper" and ComputerChoice == "scissors":
    print("The Computer selected", ComputerChoice,".")
    print("Cpu Wins!")
    CPUwins = CPUwins + 1
    Roundsplayed = Roundsplayed + 1
  elif PlayerChoice == "Paper" or PlayerChoice == "paper" and ComputerChoice == "rock":
    print("The Computer selected", ComputerChoice,".")
    print(Player, "Wins!")
    Playerwins = Playerwins + 1
    Roundsplayed = Roundsplayed + 1
  elif PlayerChoice == "Paper" or PlayerChoice == "paper" and ComputerChoice == "paper":
    print("The Computer selected", ComputerChoice,".")
    print("Tie!")
    Roundsplayed = Roundsplayed + 1
  elif PlayerChoice == "Scissors" or PlayerChoice == "scissors" and ComputerChoice == "scissors":
    print("The Computer selected", ComputerChoice,".")
    print("Tie!")
    Roundsplayed = Roundsplayed + 1
  elif PlayerChoice == "Scissors" or PlayerChoice == "scissors" and ComputerChoice == "rock":
    print("The Computer selected", ComputerChoice,".")
    print("Cpu wins!")
    CPUwins = CPUwins + 1
    Roundsplayed = Roundsplayed + 1
  elif PlayerChoice == "Scissors" or PlayerChoice == "scissors" and ComputerChoice == "paper":
    print("The Computer selected", ComputerChoice,".")
    print(Player, "Wins!")
    Playerwins = Playerwins + 1
    Roundsplayed = Roundsplayed + 1
if Rounds == Roundsplayed:
  if Playerwins > CPUwins:
    print("The games are over. And the winner is, ")
    time.sleep(3)
    print(Player, ", with a final score of", Playerwins, "to", CPUwins, "!")
  elif Playerwins < CPUwins:
    print("The games are over. And the winner is, ")
    time.sleep(3)
    print("CPU, with a final score of", CPUwins, "to", Playerwins, "!")
  elif Playerwins == CPUwins:
    print("The games are over. And the winner is, ")
    time.sleep(3)
    print("There is no winner! It's a tie! The final score was", Playerwins, "to", CPUwins, "!")
