# Cool cat just for effect

print(" ")
cat = '''
                       /)
              /\___/\ ((
              \`@_@'/  ))
              {_:Y:.}_//
    ----------{_}^-'{_}----------
'''

print (cat)
print(" ")
print(" ")
print("Welcome to RPS! Let's have a blast! :) ")
print(" ")

# Import library
import random

# Define constants

ROCK = 1
PAPER = 2
SCISSORS = 3

# Get user input + validation

def onActionGetUserChoice():
    while True:
        try:
            choice = int(input("Make your pick: Rock (1), Paper (2), or Scissors (3): "))
            if choice in (ROCK, PAPER, SCISSORS):
                return choice
            else:
                print("Entry is invalid! Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter 1, 2, or 3.")

# Determine results of the game

def onActionGetResult(user_choice, cpuChoice):
    if userChoice == cpuChoice:
        return "Looks like a draw."
    elif (
        # Win conditions
        (userChoice == ROCK and cpuChoice == SCISSORS)
        or (userChoice == SCISSORS and cpuChoice == PAPER)
        or (userChoice == PAPER and cpuChoice == ROCK)
    ):
        return "Congrats! You won! :)"
    else:
        return "Oh no! You lost! :("

# Mechanics loop (do i add lizard/spock here??)

while True:
    cpuChoice = random.choice([ROCK, PAPER, SCISSORS])
    userChoice = onActionGetUserChoice()

    if cpuChoice == ROCK:
        cpuChoiceName = "Rock"
    elif cpuChoice == PAPER:
        cpuChoiceName = "Paper"
    else:
        cpuChoiceName = "Scissors"

    if userChoice == ROCK:
        userChoiceName = "Rock"
    elif userChoice == PAPER:
        userChoiceName = "Paper"
    else:
        userChoiceName = "Scissors"

# Final output

    print(f"I chose {cpuChoiceName} and you chose {userChoiceName}. {onActionGetResult(userChoice, cpuChoice)}")

    playAgain = input("Would you like to play again? Enter 'Y' or 'y' to continue (or press any other key to exit): ")
    if playAgain.lower() != 'y':
        break