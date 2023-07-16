"""Blackjack random function"""

import random


def main():
    print("This program simulates a bunch of blackjack games.")
    num = getInputs()
    score = simOneGame()
    holds, busts = simNGames(num)
    printSummary(holds, busts)


def getInputs():
    while True:
        game = int(input("How many games should be simulated? "))
        if game <= 0:
            print("You must enter a number greater than zero!")
        else:
            break
    return game


def simOneGame():
    score = 0
    blacklist = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    while not gameOver(score):
        black_score = blacklist[random.choice(blacklist)]
        score = score + black_score
        if score >= 17: 
            break
        if black_score == 11 and (score >= 6 and score <= 10): 
            score += 11
        else:
            score += 1
    return score


def simNGames(num):
    holds = 0
    busts = 0
    for i in range(num):
        score = simOneGame()
        if score >= 22:
            busts = busts + 1
        else:
            holds = holds + 1
    return holds, busts


def gameOver(score):
    return score >= 22 or score >= 17


def printSummary(holds, busts):
    num = holds + busts
    print(f"Number of holds and busts: Holds: {holds} Busts: {busts}")
    print(f"Percentage of holds and busts: Holds: {holds / num}%", end = " ")
    print(f"Busts: {busts / num}%")


if __name__ == "__main__":
    main()
