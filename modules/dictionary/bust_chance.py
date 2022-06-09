"""Calculates the chances that the player will bust."""

from re import A


cards = 52
deck = 6

chance = deck * (cards - 2)

hand = {"11": f"{0}%",
        "12": f"{chance}%",  # 32
        "13": f"{chance}%",  # 40
        "14": f"{chance}%",  # 48
        "15": f"{chance}%",  # 56
        "16": f"{chance}%",  # 64
        "17": f"{chance}%",  # 72
        "18": f"{chance}%",  # 78
        "19": f"{chance}%",  # 85
        "20": f"{chance}%",  # 92
        "21": f"{100}%"}

bust_chance = dict{card3_12: {{A,A}, {2,(10,J,Q,K)}, {3,9}, {4,8}, {5,7}, {6,6}},
                   card3_13: {{A,2}, {3,(10,J,Q,K)}, {4,9}, {5,8}, {6,7}},
                   card3_14: {{A,3}, {4,(10,J,Q,K)}, {5,9}, {7,7}, {6,8}},
                   card3_15: {{A,4}, {5,(10,J,Q,K)}, {6,9}, {7,8}},
                   card3_16: {{A,5}, {6,(10,J,Q,K)}, {7,9}, {8,8}},
                   card3_17: {{A,6}, {7,(10,J,Q,K)}, {8,9}},
                   card3_18: {{A,7}, {8,(10,J,Q,K)}, {9,9}},
                   card3_19: {{A,8}, {9,(10,J,Q,K)}},
                   card3_20: {{A,9}, {(10,J,Q,K),(10,J,Q,K)}},
                   card3_21: {A,(10,J,Q,K)}}
