def card_value(card):
    """Returns the integer value of a single card."""

    rank = card[0]
    if rank in ranks[0:-4]:
        return int(rank)
    elif rank is 'ACE':
        return 11
    else:
        return 10

def hand_value(hand):
    """Returns the integer value of a set of cards."""

    # Naively sum up the cards in the deck.
    tmp_value = sum(card_value(_) for _ in hand)
    # Count the number of Aces in the hand.
    num_aces = len([_ for _ in hand if _[0] is 'ACE'])

    # Aces can count for 1, or 11. If it is possible to bring the value of 
    #the hand under 21 by making 11 -> 1 substitutions, do so.
    while num_aces > 0:

        if tmp_value > 21 and 'ACE' in ranks:
            tmp_value -= 10
            num_aces -= 1
        else:
            break

    # Return a string and an integer representing the value of the hand. If 
    # the hand is bust, return 100.
    if tmp_value < 21:
        return [str(tmp_value), tmp_value]
    elif tmp_value == 21:
        return ['Blackjack!', 21]
    else:
        return ['Bust!', 100]
