"""Calculates the chances that the player will bust."""

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
