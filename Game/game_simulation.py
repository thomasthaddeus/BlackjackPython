# Declaring variables for use
import random
results      = {}
winnings     = 0
total_games  = 0
games_sim    = 1000
rec_rounds   = 10
limit        = 16
strategies   = list(df.index)
random.shuffle(strategies) # shuffling the index for more randomization


# Looping through the various strategies we have
for strat in strategies:
    print(f"Simulating {strat}")

    results[f"{strat}"] = []
    c = games_sim

    # Simulating the games with a specific strategy
    for _ in range(games_sim):
        bj           = play_blackjack(limit, strat)

        # Recording only the last N rounds played in order to 
        # account for the effectiveness of the card counting technique
        last_wins    = sum(bj[0][-rec_rounds:])
        last_draws   = sum(bj[1][-rec_rounds:])
        winnings    += last_wins+last_draws
        total_games += rec_rounds

        wp = round((winnings/total_games)*100, 4)
        results[f"{strat}"].append(wp)

        c -= 1
        print(c, end=" ")
                
    print(f"\nCompleted {strat}\n")
    
    if strat == strategies[-1]:
        print(f"SIMULATED ALL STRATEGIES {games_sim} TIMES EACH")


games_sim = list(range(games_sim))
