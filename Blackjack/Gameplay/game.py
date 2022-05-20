"""This is where the game is played."""

class Game:
    """Class for managing the game."""
    def __init__(self, hand, hit, card_value):
        self.hand = hand
        self.hit = hit
        self.card_value = card_value

    def pre_game(self):
        """Print modules before the game starts."""
        quit_game = ['n', 'N', 'no', 'No', 'nO', 'NO', 'q', 'quit', 'exit']
        keep_playing = []
        print('Welcome to the casino game!')
        print('Would you like to play the game of blackjack?')
        response = input("Yes or no: ")
        while True:
            if response in quit_game:
                break
            elif response in keep_playing:
                start_game()
            else:
                print('Please type "yes" or "no"')


    def start_game(self):
        """Start the game."""
        print("Hand: " + str(self.hand))

    def dealer():
        """Actions for the dealer."""
        pass

    def car_point_value(self, card_value):
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


class Player_Actions:
    def __init__(self, hit, stand, split):
        self.hit = hit
        self.stand = stand
        self.split = split

    def player(self, action):
        """Actions for the player to make a move."""
        for self in self.actions:
            if self.hit(action):
                # add card
            elif self.stand(action):
                # change position
            elif self.split(action):
                split()
            elif














