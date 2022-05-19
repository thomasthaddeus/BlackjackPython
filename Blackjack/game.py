"""This is where the game is played."""


class Game(object):
    """Class for managing the game."""
    def __init__(self, hand, hit):
        self.hand = hand
        self.hit = hit

    def pre_game(self):
        """Print modules before the game starts."""
        quit_game = ['n', 'N', 'no', 'No', 'nO', 'NO', 'q', 'quit', 'exit']
        keep_playing = []
        print('Welcome to the casino game!')
        print('Would you like to play the game of blackjack?')
        response = input("Yes or no: ")
        if response in quit_game:
            break
        elif response in keep_playing:
            start_game()
        else:
            print('Please type "yes" or "no"')

        print("Hand: " + str(self.hand))

    def start_game(self):
        """Start the game."""
        pass

    def dealer():
        """Actions for the dealer."""
        pass

    def player():
        """Actions for the player to make a move."""
        pass

    def card_count():
        """Counts the number of cards left in the game."""
        pass
