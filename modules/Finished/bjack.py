"""Defines the probability function for getting a blackjack."""

#########################################
##                                     ##
##      Written by Thad Thomas         ##
##          d. May 29, 2022            ##
##                                     ##
#########################################

from tabulate import tabulate
# cut = float(random.randint(40, 80))
ACES = 4 / 52  # First Card


def main():
    """Main function"""
    print("""
\nProbability of getting a blackjack
using 1 to 8 - 52 card decks
without a cut in the deck is:\n""")
    print_block()


def chance(decks):
    """Defines the probability function for being dealt a blackjack
        based on the number of decks being used in the shoe"""
    mult_deck = float(f"{((2*(ACES)*(16 * decks/(52*decks-1))) * 100):.4f}")
    return mult_deck


def print_block():
    """Lists the probabilities from 1 - 8 decks"""
    table = [
                ['# of decks', 'Odds %'],
                ['1 Deck', chance(1)],
                ['2 Deck', chance(2)],
                ['3 Deck', chance(3)],
                ['4 Deck', chance(4)],
                ['5 Deck', chance(5)],
                ['6 Deck', chance(6)],
                ['7 Deck', chance(7)],
                ['8 Deck', chance(8)]
            ]
    tab = print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
    # 32 / 663 - single deck probability
    return tab


if __name__ == '__main__':
    main()
