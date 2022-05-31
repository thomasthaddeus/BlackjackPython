"""Algorithm for generating a decision tree."""

from tabulate import tabulate


def hard_hand():
    """Generate a hard hand decision tree."""
    table = [
        ['Players Hand', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Ace'],
        ['5', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit',
            'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],
        ['6', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit',
            'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],
        ['7', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit',
            'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],
        ['8', 'Hit', 'Hit', 'Hit', "Double Hit",
            "Double Hit", 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],
        ["9", "Double Hit", "Double Hit", "Double Hit", "Double Hit",
            "Double Hit", "Hit", "Hit", "Hit", "Hit", "Hit"],
        ["10", "Double Hit", "Double Hit", "Double Hit", "Double Hit",
            "Double Hit", "Double Hit", "Double Hit", "Double Hit", "Hit", "Hit"],
        ["11", "Double Hit", "Double Hit", "Double Hit", "Double Hit", "Double Hit",
            "Double Hit", "Double Hit", "Double Hit", "Double Hit", "Double Hit"],
        ["12", "Hit", "Hit", "Stand", "Stand", "Stand",
            "Hit", "Hit", "Hit", "Hit", "Hit"],
        ["13", "Stand", "Stand", "Stand", "Stand",
            "Stand", "Hit", "Hit", "Hit", "Hit", "Hit"],
        ["14", "Stand", "Stand", "Stand", "Stand",
            "Stand", "Hit", "Hit", "Hit", "Hit", "Hit"],
        ["15", "Stand", "Stand", "Stand", "Stand",
            "Stand", "Hit", "Hit", "Hit", "Hit", "Hit"],
        ["16", "Stand", "Stand", "Stand", "Stand",
            "Stand", "Hit", "Hit", "Hit", "Hit", "Hit"],
        ['17', "Stand", "Stand", "Stand", "Stand", "Stand",
            "Stand", "Stand", "Stand", "Stand", "Stand"],
        ['18', "Stand", "Stand", "Stand", "Stand", "Stand",
            "Stand", "Stand", "Stand", "Stand", "Stand"],
        ['19', "Stand", "Stand", "Stand", "Stand", "Stand",
            "Stand", "Stand", "Stand", "Stand", "Stand"],
        ['20', "Stand", "Stand", "Stand", "Stand", "Stand",
            "Stand", "Stand", "Stand", "Stand", "Stand"],
        ['21', "Stand", "Stand", "Stand", "Stand", "Stand",
            "Stand", "Stand", "Stand", "Stand", "Stand"]
    ]
    tab = print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
    # 32 / 663 - single deck probability
    return tab

hard_hand()
