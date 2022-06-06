"""Hard Hand decision table"""

import os
import random

with open("modules/hard_hand.txt", 'r', encoding = 'utf-8') as f:
    data = f.readlines()

DEALER = random.randint(2, 12)


def main():
    """opens the dictionary prints the results"""
    print_block()
    print()


def hard_hand(card1, card2):
    """Hard Hand decision table"""
    comb = card1 + card2
    result = print(f"\n{data[comb].get(DEALER)}\n")
    return result


def print_block():
    """Prints the card block"""
    clear = lambda: os.system("cls")
    clear()
    hard_hand(DEALER, DEALER)


if __name__ == '__main__':
    main()
