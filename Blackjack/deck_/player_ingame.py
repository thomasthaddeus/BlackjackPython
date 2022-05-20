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
