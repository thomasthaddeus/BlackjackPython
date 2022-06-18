"""Probabilities for Blackjack"""

import random
from random import choice
import numpy as np

aces = np.random.choice
deck_rem = 52
A = 11
J = 10
Q = 10
K = 10
TEN = (10 or J or Q or K)
mult_deck = float(f"{((2*(aces)*(16*8/((51*8)-1))) * 100):.4f}")

deck = np.array(["2c","3c","4c","5c","6c","7c","8c","9c","10c","Jc","Qc","Kc","Ac"],
                ["2s","3s","4s","5s","6s","7s","8s","9s","10s","Js","Qs","Ks","As"],
                ["2h","3h","4h","5h","6h","7h","8h","9h","10h","Jh","Qh","Kh","Ah"],
                ["2d","3d","4d","5d","6d","7d","8d","9d","10d","Jd","Qd","Kd","Ad"])
np.random.choice(deck)


deck_played = []
card1, card2 = choice, choice
dealer1, dealer2 = choice, choice
card3 = int(choice(deck(random(i))))
card1 = int(card1) / deck_rem
card2 = int(card2) / (deck_rem - 1)
card3 = int(choice(deck())) / (deck_rem - 1)


third_card = {
    12: {{2,TEN}, {3,9}, {4,8}, {5,7}, {6,6}},
    13: {{3,TEN}, {4,9}, {5,8}, {6,7}},
    14: {{4,TEN}, {5,9}, {7,7}, {6,8}},
    15: {{5,TEN}, {6,9}, {7,8}},
    16: {{6,TEN}, {7,9}, {8,8}},
    17: {{7,TEN}, {8,9}},
    18: {{8,TEN}, {9,9}},
    19: { 9,TEN},
    20: {TEN,TEN},  #16 / 51 * 16 / 52
    21: {TEN, A} # 100% chance of failure
    }

soft_hand = {
12:(A,A),
13:{A,2},
14:{A,3},
15:{A,4},
16:{A,5},
17:{A,6},
18:{A,7},
19:{A,8},
20:{A,9},
21:{A,TEN}
}


def probability_function(i, j, k):
    """
    Determines the odds of going over 21 if a third card is drawn

    Args:
        i (int): first card/integer in the pair
        j (int): second integer in the pair

    Returns:
        int: random card drawn from the dictionary after i and j have been chosen
    """

prob_1 = probability_function(card1, card2)
print(prob_1)
