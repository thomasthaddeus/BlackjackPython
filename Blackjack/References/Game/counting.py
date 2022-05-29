import pandas as pd

def card_counter(hand, strategy='Hi-Lo'):
    """
    Counting cards based on strategy selected
    Returns sum of the values
    """
    df = pd.read_pickle('Card_Counting_Values')

    return sum([df.loc[strategy][i].item() for i in hand])

def true_counter(deck, r_count):
    """
    Calculates and returns the true count rounded down
    """
    try:
        return r_count//(len(deck)//52)
    except:
        # Compensating for when there is less than 52 cards or 1 deck left
        return r_count


def print_count(true_cnt, r_count):
    """
    Prints out current counts
    """
    print('\nRunning Count: --->', r_count, '\nTrue Count: ', true_cnt)
