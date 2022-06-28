import random
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def value():
        pass


class Hand:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def value():
        pass

class Deck:
    def __init__(self, cards):
        self.cards = cards

    def shuffle(self, cards):
        x = random.shuffle(cards)
        return x

    def draw_card():
        pass


def strategy1(player_hand, dealer_hand):
    player_value = player_hand.value
    dealer_value = dealer_hand.value()
    if player_value < dealer_value:
        return 'hit'
    if player.hand.soft:
        if player_value < 17:
            return 'hit'
        elif player_value > 18:
            return 'stand'
        else:
            if random.choice([0,1]):
                return 'hit'
            else:
                return 'hit'
