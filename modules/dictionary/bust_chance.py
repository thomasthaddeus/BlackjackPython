"""Calculates the chances that the player will bust."""

import random

x = random.choice
cards = (x, y)
decks = 6
tens_d = {'10':10 ,"J":10, 'Q':10, 'K':10}

chance = decks * (cards - 2)

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

p21 = ((4 / 52) * (16 / 51)) + ((16 / 52) * (4 / 51))
p20 = (3 / 48)
p19 = (4 / 48)
p18 = ()
p17 = ()
p16 = ()
