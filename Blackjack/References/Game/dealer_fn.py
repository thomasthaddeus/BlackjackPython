def dealer_turn(your_hand, dealer_hand, total, dtotal, r_count, true_cnt, deck, turn=True):
    """
    Activates the dealer's turn if player's move was 'stay'
    """
    # Tallying wins, losses, and draws
    wins = 0
    draw = 0
    loss = 0

    # Looping through the moves
    while turn:
        total = hand_total(your_hand)
        if total > 21:

            # Evaluating a player's hand to see if they have an ace
            check_ace(your_hand)
            total = hand_total(your_hand)
            player_print(your_hand, total)
            continue

        dtotal = hand_total(dealer_hand)
        dealer_print(dealer_hand, dtotal)

        while dtotal <= 16:

            # Dealing cards to the dealer if they have less than or equal to 16
            deal_card(dealer_hand, deck)
            dtotal = hand_total(dealer_hand)
            dealer_print(dealer_hand, dtotal)

            # Counter
            r_count += card_counter(dealer_hand[-1:])
            true_cnt = true_counter(deck, r_count)
            print_count(true_cnt, r_count)

        # Checking if the dealer wins
        if dtotal == 21:
            print("Game Over. House wins.")
            loss += 1
            break

        # Checking if the dealer busts
        elif dtotal > 21:
            if check_ace(dealer_hand):
                continue
            else:
                print("Dealer busts! You win!")
                wins += 1
                break

        # Comparing dealer hand to player hand
        elif 17 <= dtotal <= 21:
            if dtotal > total:
                print("Game Over. House wins")
                loss += 1
                break
            elif dtotal < total:
                print("Congratulations! You win!")
                wins += 1
                break
            elif dtotal == total:
                print("Draw. No lost bet.")
                draw += 1
                break
            else:
                print("House busts. You win!")
                wins += 1
                break
    return [wins, loss, draw, r_count, true_cnt]
