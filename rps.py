
"""
    This script will play rock paper scissors with you!
"""

import random

def evaluateHand(playerHand, sysHand):

    if playerHand == sysHand:
        # Matching hands are ties, regardless of values

        return "null"

    elif playerHand == 'r':
        # Player played his hardest rock

        print("Player chooses rock...")

        if sysHand == 's':

            print("System chooses scissors!")
            return "player"

        elif sysHand == 'p':

            print("System chooses paper!")
            return "sys"

    elif playerHand == 'p':
        # Player played his flattest paper

        print("Player chooses paper...")

        if sysHand == 'r':

            print("System chooses rock!")
            return "player"

        elif sysHand == 's':

            print("System chooses scissors!")
            return "sys"

    elif playerHand == 's':
        # Player played his sharpest pair of scissors

        print("Player chooses scissors...")

        if sysHand == 'p':
            print("System chooses paper!")
            return "player"

        elif sysHand == 'r':
            print("System chooses rock!")
            return "sys"


def play(playerHand):

    sysHand = random.choice("rps")
    winner = evaluateHand(playerHand, sysHand)

    if winner == "player":
        print()
        print("You win!")

    else:
        print()
        print("You lose :(")

def main():
    print("**************************************")
    print("*    LETS PLAY ROCK PAPER SCISSORS!  *")
    print("**************************************")

    print("\n")
    print("Choose 'r' for rock, 'p' for paper, or 's' for scissors!")
    playerHand = input("What's your move?: ")
    print()

    # Check if the player hand is accurate.
    validHands = ["r", "p", "s"]
    if playerHand not in validHands:
        print("invalid input")
        exit(1)

    # print("Your move is : " + playerHand)

    play(playerHand)


if __name__ == '__main__':
    main()