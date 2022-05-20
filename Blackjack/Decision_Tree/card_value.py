    def card_counter(self, card_value):
        """Returns the value of the card in Blackjack."""
        self.card_value = {'Ace-Lo':   1,
                           'Deuce':    2,
                           'Three':    3,
                           'Four':     4,
                           'Five':     5,
                           'Six':      6,
                           'Seven':    7,
                           'Eight':    8,
                           'Nine':     9,
                           'Ten':      10,
                           'Jack':     10,
                           'Queen':    10,
                           'King':     10,
                           'Ace-High': 11}
        for key in card_value:
            return card_value[key]