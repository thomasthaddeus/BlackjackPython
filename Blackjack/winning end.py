player_score_label, player_score = hand_value(player_hand)
dealer_score_label, dealer_score = hand_value(dealer_hand)

if player_score <= 21:
    dealer_hand_string = '''\nDealer is at %s\nwith the hand %s\n'''
    print  dealer_hand_string % (dealer_score_label, dealer_hand)
else: 
    print "Dealer wins."

while hand_value(dealer_hand)[1] < 17:
    new_dealer_card = deck.pop()
    dealer_hand.append(new_dealer_card)
    print 'Dealer draws %s' % new_dealer_card
dealer_score_label, dealer_score = hand_value(dealer_hand)

if player_score < 100 and dealer_score == 100:
    print 'You beat the dealer!'
elif player_score > dealer_score:
    print 'You beat the dealer!'
elif player_score == dealer_score:
    print 'You tied the dealer, nobody wins.'
elif player_score < dealer_score:
    print "Dealer wins!"
