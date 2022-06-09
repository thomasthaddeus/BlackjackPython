"""Hard Hand decision table"""

import random
import os

cards_hh = {
    5: {
        2: "H",
        3: "H",
        4: "H",
        5: "H",
        6: "H",
        7: "H",
        8: "H",
        9: "H",
        10: "H",
        11: "H",
    },
    6: {
        2: "H",
        3: "H",
        4: "H",
        5: "H",
        6: "H",
        7: "H",
        8: "H",
        9: "H",
        10: "H",
        11: "H",
    },
    7: {
        2: "H",
        3: "H",
        4: "H",
        5: "H",
        6: "H",
        7: "H",
        8: "H",
        9: "H",
        10: "H",
        11: "H",
    },
    8: {
        2: "H",
        3: "H",
        4: "H",
        5: "Dh",
        6: "Dh",
        7: "H",
        8: "H",
        9: "H",
        10: "H",
        11: "H",
    },
    9: {
        2: "Dh",
        3: "Dh",
        4: "Dh",
        5: "Dh",
        6: "Dh",
        7: "H",
        8: "H",
        9: "H",
        10: "H",
        11: "H",
    },
    10: {
        2: "Dh",
        3: "Dh",
        4: "Dh",
        5: "Dh",
        6: "Dh",
        7: "Dh",
        8: "Dh",
        9: "Dh",
        10: "H",
        11: "H",
    },
    11: {
        2: "Dh",
        3: "Dh",
        4: "Dh",
        5: "Dh",
        6: "Dh",
        7: "Dh",
        8: "Dh",
        9: "Dh",
        10: "Dh",
        11: "Dh",
    },
    12: {
        2: "H",
        3: "H",
        4: "S",
        5: "S",
        6: "S",
        7: "H",
        8: "H",
        9: "H",
        10: "H",
        11: "H",
    },
    13: {
        2: "S",
        3: "S",
        4: "S",
        5: "S",
        6: "S",
        7: "H",
        8: "H",
        9: "H",
        10: "H",
        11: "H",
    },
    14: {
        2: "S",
        3: "S",
        4: "S",
        5: "S",
        6: "S",
        7: "H",
        8: "H",
        9: "H",
        10: "H",
        11: "H",
    },
    15: {
        2: "S",
        3: "S",
        4: "S",
        5: "S",
        6: "S",
        7: "H",
        8: "H",
        9: "H",
        10: "H",
        11: "H",
    },
    16: {
        2: "S",
        3: "S",
        4: "S",
        5: "S",
        6: "S",
        7: "H",
        8: "H",
        9: "H",
        10: "H",
        11: "H",
    },
    17: {
        2: "S",
        3: "S",
        4: "S",
        5: "S",
        6: "S",
        7: "S",
        8: "S",
        9: "S",
        10: "S",
        11: "S",
    },
    18: {
        2: "S",
        3: "S",
        4: "S",
        5: "S",
        6: "S",
        7: "S",
        8: "S",
        9: "S",
        10: "S",
        11: "S",
    },
    19: {
        2: "S",
        3: "S",
        4: "S",
        5: "S",
        6: "S",
        7: "S",
        8: "S",
        9: "S",
        10: "S",
        11: "S",
    },
    20: {
        2: "S",
        3: "S",
        4: "S",
        5: "S",
        6: "S",
        7: "S",
        8: "S",
        9: "S",
        10: "S",
        11: "S",
    },
    21: {
        2: "S",
        3: "S",
        4: "S",
        5: "S",
        6: "S",
        7: "S",
        8: "S",
        9: "S",
        10: "S",
        11: "S",
    },
}


DEALER_A = random.randint(2, 12)


def main():
    """opens the dictionary prints the results"""
    print_block()


def hard_hand(card1, card2):
    """Hard Hand decision table"""
    comb = card1 + card2
    result = print(f"\n{cards_hh[comb].get(DEALER_A)}\n")
    if card1 == card2:
        print(f"First Card is: {card1}")
        print(f"Second Card is: {card2}")
    else:
        return result


def soft_hand(card1, card2):
    """Soft Hand decision table
    To Be a soft hand an Ace has to be present."""
    comb = card1 + card2


def split_hand(card1, card2):
    """"""


def print_block():
    """Prints the card block"""
    clear = lambda: os.system("cls")
    clear()
    hard_hand(DEALER_A, DEALER_B)


if __name__ == "__main__":
    main()
