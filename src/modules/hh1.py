"""Hard Hand decision table"""

import random
import json

D = 52
T = 10
J = 10
Q = 10
K = 10
A = 11
ALT_A = 1
deck = [2, 3, 4, 5, 6, 7, 8, 9, T, J, Q, K, A,
        2, 3, 4, 5, 6, 7, 8, 9, T, J, Q, K, A,
        2, 3, 4, 5, 6, 7, 8, 9, T, J, Q, K, A,
        2, 3, 4, 5, 6, 7, 8, 9, T, J, Q, K, A]

deck_suit = ["2c", "3c", "4c", "5c", "6c", "7c", "8c", "9c", "Tc", "Jc", "Qc", "Kc", "Ac",
        "2s", "3s", "4s", "5s", "6s", "7s", "8s", "9s", "Ts", "Js", "Qs", "Ks", "As",
        "2h", "3h", "4h", "5h", "6h", "7h", "8h", "9h", "Th", "Jh", "Qh", "Kh", "Ah",
        "2d", "3d", "4d", "5d", "6d", "7d", "8d", "9d", "Td", "Jd", "Qd", "Kd", "Ad"]
used_cards = []


def main():
    """opens the dictionary prints the results"""
    count = 0
    card1 = random.choice(deck)
    card2 = random.choice(deck)
    dealer1 = random.choice(deck)
    dealer2 = random.choice(deck)
    while count <= 1000:
        card_rand(card1, card2)
        count += 2
        card_rand(dealer1, dealer2)
        count += 2
        comb = card1 + card2
        print(f"\nCard1 {card1} & Card2 {card2}\n")
        print(f"Total = {comb}\n")
        if comb == 21:
            print("Blackjack")
        elif card1 + card2 > 21:
            print("Soft Hand")
            soft_hand(comb)
        elif card1 == card2:
            if card1 is A:
                card2 = ALT_A
            print("Split Hand")
            split_hand(card1)
        elif card1 != 11 and card2 != 11:
            print("Hard Hand")
            hard_hand(comb)
        elif deck is not deck:
            deck.extend(used_cards)
            random.shuffle(used_cards)
        else:
            print("Invalid error")
    print(used_cards)



def my_list(j_list):
    """Returns a list of cards"""
    for key, value in j_list.items():
        value = list(map(int, j_list))
        return key, value


def hard_hand(comb):
    """Hard Hand decision table"""
    filename = "hard_hands_dict.json"
    with open(filename, "r", encoding="utf-8") as file:
        cards_hh = json.load(file)
    result = cards_hh[str(comb)]
    my_list(result)
    return result


def soft_hand(comb):
    """Soft Hand decision table
    To Be a soft hand an Ace has to be present."""
    filename = "soft_hands_dict.json"
    with open(filename, "r", encoding="utf-8") as file:
        cards_sh = json.load(file)
    move = cards_sh[str(comb)]
    print(move)
    return move


def split_hand(card1):
    """Splits the hand if its a pair."""
    filename = "split_hands_dict.json"
    with open(filename, "r", encoding="utf-8") as file:
        cards_split = json.load(file)
    for card1 in cards_split:
        print(card1, card1)
        return cards_split[card1]


if __name__ == "__main__":
    main()
