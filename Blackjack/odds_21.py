"""Defines the probability function for getting a blackjack."""
# Each variant of blackjack offers different odds
#   of winning for the dealer as well as the player.
# In blackjack, the odds are represented in percentage and
#   they determine the probability of winning
#   or going bust in a particular situation.
# Knowledge of this blackjack probability
#   of winning or going bust, in turn,
#   helps players make better playing decisions and strategic moves.
# Blackjack is a very strategic casino card game
#   that is best played with a mathematical
#   approach involving probabilities.
# Blackjack odds refer to the percentage of the chances
#   of winning for the player or the dealer.
# But what are the odds of getting blackjack?
# Depending on the number of decks being played and the side bets placed,
#   the odds and probabilities vary, as discussed in detail here.
# Blackjack Odds for Single Shoe


# It is simpler to calculate the blackjack odds and probabilities
#   for the dealer and the player in a single-deck game
#   though the calculations depend on the hands of both.

# Accordingly, the odds of being dealt blackjack for the player are about 4.8%.
# The odds of a No Bust, a Standing Hand (17-20)
#   and a Decision Hand (1-16) are
#   26.5%, 30%, and 38.7% respectively.

# The odds for the final hands that the dealer will make, on the other hand,
#     are 4.82% for a Natural 21 and
#     between 17.58%% to 28.36%
#         for hands between 20 and 16.

# The odds of busting for the player in a single shoe game will be:
# 1. 100% for 21 and
# 2. gradually come down to 0%
#     - if the card in hand is <11.
# Odds of getting blackjack with a single deck
class Odds:
    """Class for calculating blackjack probabilities"""

    def dealt21():
        """Returns the probability of getting blackjack for a single deck."""
        ace = 4 / 52  # Aces
        ten = 16 / 51  # Face cards and tens
        probability = float((ace * ten) * 2)
        prob = print(f"\nThe probability of getting blackjack with a 52 card deck is: {probability:.4f}")
        return prob

    dealt21()

    def bust():
        """Returns the probability of going bust."""
        