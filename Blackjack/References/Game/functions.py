import random


def check_ace(hand):
    """Checks if there's an ace in the hand in case total went over 21"""
    if 'A' in hand:
        hand[hand.index('A')] = 'A.'
        return True
    else:
        return False


def hand_total(hand):
    """Calculates sum total values from a list of strings using a dictionary"""
    d_val = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
             '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11, 'A.': 1}
    return sum(d_val[i] for i in hand)


def deal_card(hand, deck, num_of_cards=1):
    """Deals a card, defaulted to one card"""
    for _ in range(num_of_cards):
        hand.append(deck.pop())
    return hand


def create_deck(num_of_decks=1):
    """Creates a standard playing card deck, defaulted to one deck"""
    deck = ['2', '3', '4', '5', '6', '7', '8', '9',
            '10', 'J', 'Q', 'K', 'A']*4*num_of_decks
    random.shuffle(deck)
    return deck


def player_print(hand, total):
    """Prints player's current hand and total"""
    print("\nYour hand: ", hand, "\nYour total: ", total)


def dealer_print(hand, total):
    """Prints dealer's current hand and total"""
    print("\nDealer hand: ", hand, "\nDealer total: ", total)


def play_again():
    """Loops the game"""
    while True:
        # Asking the player to play again or not
        ans = input("Play again? \n").lower()
        if ans == 'yes' or ans == 'y':
            print("\n------------ Another Round of Blackjack -------------")
            return True
        elif ans == 'no' or ans == 'n':
            return False
        else:
            print("Yes or no? ")
            continue
