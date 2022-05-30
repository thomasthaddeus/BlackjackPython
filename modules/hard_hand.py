"""Hard Hand decision table"""

import os
import random
DEALER = random.randint(2, 12)


def hard_hand(card1, card2):
    """Hard Hand decision table"""
    comb = card1 + card2
    result = print(f"\n{cards[comb].get(DEALER)}\n")
    return result

def print_block():
    clear = lambda: os.system("cls")
    clear()
    hard_hand(DEALER, DEALER)

if __name__ == '__main__':
    main()
