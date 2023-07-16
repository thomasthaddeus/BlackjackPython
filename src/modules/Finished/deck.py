import random

deck = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "A", "J", "Q", "K"]

def get_deck():
    """Return a list of (rank, suit) tuples for all 52 cards."""
    deck_a = []
    for suit in ("clubs", "diamonds", "hearts", "spades"):
        for rank in range(2, 11):
            deck_a.append((str(rank), suit))  # Add the numbered cards.
        for rank in ("J", "Q", "K", "A"):
            deck_a.append((rank, suit))  # Add the face and ace cards.
    random.shuffle(deck)
    return deck_a


def get_deck_list():
    """Get a list of cards values"""
    value = 0
    num_of_aces = 0
    for card in deck:
        rank = card[0]
        if rank == 'A':
            num_of_aces += 1
        else:
            value += int(rank)
    value += num_of_aces
    for card in range(num_of_aces):
        if value + 10 <= 21:
            value += 10
    return value
