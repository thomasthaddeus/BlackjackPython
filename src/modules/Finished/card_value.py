"""Module for handling card counter."""

def card_counter(self, card_value):
    """Returns the value of the card in Blackjack."""
    self.card_value = {'2': 2,
                       '3': 3,
                       '4': 4,
                       '5': 5,
                       '6': 6,
                       '7': 7,
                       '8': 8,
                       '9': 9,
                       '10':10,
                       'J': 10,
                       'Q': 10,
                       'K': 10,
                       'A': 11}
    for key, value in card_value:
        if key in self.card_value:
            return card_value[value]
