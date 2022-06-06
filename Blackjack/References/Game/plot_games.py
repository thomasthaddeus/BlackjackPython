"""Graphing results in matplotlib to show different strategies."""
# Source: https://gist.github.com/marcosan93/7185c6549128fc329337d027f4a3e16c

import ./counting_values.py
import ./counting.py
import ./dealer_fn.py
import ./functions.py
import ./game_simulation.py
import ./player_move.py

import matplotlib.pyplot as plt

plt.style.use('ggplot')
plt.figure(figsize = (16, 8))

for i in results:
    plt.plot(games_sim, results[i], label=i+': '+str(results[i][-1])+'%')

plt.title("Blackjack Probability \nGraph 3")
plt.ylabel("Percentage Won (also Draws)")
plt.xlabel("Games Played")
plt.ylim([50,54])
plt.xlim([0,len(games_sim)])
plt.legend()
plt.savefig("bj_3.png")
plt.show()
