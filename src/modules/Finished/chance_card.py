chance3 = {
    'card3_12': {{A,A}, {2,(10,J,Q,K)}, {3,9}, {4,8}, {5,7}, {6,6}},
    'card3_13': {{A,2}, {3,(10,J,Q,K)}, {4,9}, {5,8}, {6,7}},
    'card3_14': {{A,3}, {4,(10,J,Q,K)}, {5,9}, {7,7}, {6,8}},
    'card3_15': {{A,4}, {5,(10,J,Q,K)}, {6,9}, {7,8}},
    'card3_16': {{A,5}, {6,(10,J,Q,K)}, {7,9}, {8,8}},
    'card3_17': {{A,6}, {7,(10,J,Q,K)}, {8,9}},
    'card3_18': {{A,7}, {8,(10,J,Q,K)}, {9,9}},
    'card3_19': {{A,8}, {9,(10,J,Q,K)}},
    'card3_20': {{A,9}, {(10,J,Q,K),(10,J,Q,K)}},
    'card3_21': {A,(10,J,Q,K)}
    }

def third_card():
    """"""
    while True:
        c = []
        deck_a = []
        for k, v in range(chance3):
            c.append(k, v)
        for i, j in deck():
            deck_a.append(i, j)
        random.shuffle(deck_a)
        return deck_a


def standing_hand(card1, card2):
    """Defines the standing hand""" # 30%
    stander = []
    blackjack = []
    stander_count = 0
    blackjack_count = 0
    hand = card1 + card2
    if hand == 17 or 18 or 19 or 20:
        stander.append(card1 + card2)
        stander_count += 1
        return hand
    elif hand == 21:
        blackjack.append(card1 + card2)
        blackjack_count += 1
        return blackjack
