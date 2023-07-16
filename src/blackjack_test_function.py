"""Test Function from Chegg."""

def blackjack(x, y):
    """Blackjack function"""
    if x <= 0 or y <= 0:  # if any number is zero or negative then return zero
        return 0
    if x > 21 and y > 21:  # if both number is greater than 21 then return zero
        return 0
    elif x > 21:  # if only x is greater than 21 then return y
        return y
    elif y > 21:  # if only y is greater than 21 then return x
        return x
    else:  # if both x,y is less than 21 and g > 0 then return the number nearest to 21
        if (21 - x) < (21 - y):
            return x
        else:
            return y

if __name__ == '__main__':
    print("blackjack(19,21) = " + str(blackjack(19,21)))
    print("blackjack(21,19) = " + str(blackjack(21,19)))
    print("blackjack(18,5) = " + str(blackjack(18,5)))
    print("blackjack(5,18) = " + str(blackjack(5,18)))
    print("blackjack(19,22) = " + str(blackjack(19,22)))
    print("blackjack(22,19) = " + str(blackjack(22,19)))
    print("blackjack(18,18) = " + str(blackjack(18,18)))
    print("blackjack(25,22) = " + str(blackjack(25,22)))
    print("blackjack(22,25) = " + str(blackjack(22,25)))
    print("blackjack(19,-1) = " + str(blackjack(19,-1)))
    print("blackjack(-1,19) = " + str(blackjack(-1,19)))
    print("blackjack(-5,-2) = " + str(blackjack(-5,-2)))
    print("blackjack(18,0) = " + str(blackjack(18,0)))
    print("blackjack(0,9) = " + str(blackjack(0,9)))
    print("blackjack(0,0) = " + str(blackjack(0,0)))
