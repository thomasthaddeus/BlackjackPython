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

# As long as the player remains in the game, ask them if they'd  like to hit 
# for another card, or stay with their current hand.
while player_in:
    # Display the player's current hand, as well as its value.
    current_score_str = '''\nYou are currently at %s\nwith the hand %s\n'''
    print current_score_str % (hand_value(player_hand)[0], player_hand)
    # If the player's hand is bust, don't ask them for a decision.
    if hand_value(player_hand)[1] == 100:
        break

    if player_in:
        response = int(raw_input('Hit or stay? (Hit = 1, Stay = 0)'))
        # If the player asks to be hit, take the first card from the top of
        # deck and add it to their hand. If they ask to stay, change
        # player_in to false, and move on to the dealer's hand.
        if response:
            player_in = True
            new_player_card = deck.pop()
            player_hand.append(new_player_card)
            print 'You draw %s' % new_player_card
        else:
            player_in = False

player_score_label, player_score = hand_value(player_hand)
dealer_score_label, dealer_score = hand_value(dealer_hand)

if player_score <= 21:
    dealer_hand_string = '''\nDealer is at %s\nwith the hand %s\n'''
    print(dealer_hand_string % (dealer_score_label, dealer_hand))
else: 
    print("Dealer wins.")

while hand_value(dealer_hand)[1] < 17:
    new_dealer_card = deck.pop()
    dealer_hand.append(new_dealer_card)
    print 'Dealer draws %s' % new_dealer_card
dealer_score_label, dealer_score = hand_value(dealer_hand)

if player_score < 100 and dealer_score == 100:
    print('You beat the dealer!')
elif player_score > dealer_score:
    print('You beat the dealer!')
elif player_score == dealer_score:
    print('You tied the dealer, nobody wins.')
elif player_score < dealer_score:
    print("Dealer wins!")
