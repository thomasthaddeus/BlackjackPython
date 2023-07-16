"""blackjack_testcase.py
_summary_

_extended_summary_
"""


def blackjack(crd1, crd2):
    """
    Calculate the score in a simplified version of the blackjack game.

    This function takes two integers, x and y, representing the values of two cards.
    It calculates the score based on the rules of the simplified blackjack game.

    Args:
        crd1 (int): The value of the first card.
        crd2 (int): The value of the second card.

    Returns:
        int: The calculated score according to the rules of the simplified blackjack game.
    """
    if crd1 <= 0 or crd2 <= 0:
        return 0
    if crd1 > 21 and crd2 > 21:
        return 0
    if crd1 > 21:
        return crd2
    if crd2 > 21:
        return crd1
    return crd1 if (21 - crd1) < (21 - crd2) else crd2


if __name__ == "__main__":
    test_cases = [
        (19, 21),
        (21, 19),
        (18, 5),
        (5, 18),
        (19, 22),
        (22, 19),
        (18, 18),
        (25, 22),
        (22, 25),
        (19, -1),
        (-1, 19),
        (-5, -2),
        (18, 0),
        (0, 9),
        (0, 0)
    ]

    for x, y in test_cases:
        result = blackjack(x, y)
        print(f"blackjack({x}, {y}) = {result}")
