"""Builds a deck of cards from a list of cards."""

###############################################
#               Thaddeus Thomas               #
#                June 10, 2022                #
#               Blackjack Deck                #
###############################################

import random


def main():
    """Main"""
    deck = Deck()
    deck.shuffle()
    guy = Player('Guy')
    guy.draw(deck)
    card = deck.draw_card()
    card.print_card()


class Card:
    """Defines the individual cards_per_deck."""

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def print_card(self):
        """Prints the individual cards_per_deck."""
        print(f"The {self.value} of {self.suit}'s")


class Deck:
    """Blackjack deck object."""

    def __init__(self):
        self.cards = []
        self.build_cards()

    def build_cards(self):
        """Iterates a deck of cards"""
        val = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        suit = ["Clubs", "Diamonds", "Hearts", "Spades"]
        self.cards = [[s for s in suit] for v in val]

    def print_card(self):
        """Prints the deck of cards."""
        for i in self.cards:
            return i.print_card()

    def shuffle(self):
        """Shuffles the deck of cards"""
        for i in range(len(self.cards)):
            ran = random.randint(0, i)
            self.cards[i], self.cards[ran] = self.cards[ran], self.cards[i]

    def draw_card(self):
        """Draws the card from cards list."""
        return self.cards.pop()


class Player:
    """A player class"""

    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        """Adds the card to the hand."""
        self.hand.append(deck.draw_card())
        return self

    def print_card(self):
        """Prints the players hand."""
        for card in self.hand:
            card.print_card()


if __name__ == "__main__":
    main()
