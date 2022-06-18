"""Genetic algorithm search of the one max optimization problem"""

from numpy.random import randint
from numpy.random import rand


def onemax(var1):
    """returns one max optimization"""
    # objective function
    return -sum(var1)


def selection(pop, scores, k=3):
    """tournament selection"""
    # first random selection
    selection_ix = randint(len(pop))
    for num in randint(0, len(pop), k - 1):
        # check if better (e.g. perform a tournament)
        if scores[num] < scores[selection_ix]:
            selection_ix = num
    return pop[selection_ix]


def crossover(par1, par2, cross_r):
    """crossover two parents to create two children"""
    # children are copies of parents by default
    copy1, copy2 = par1.copy(), par2.copy()
    # check for recombination
    if rand() < cross_r:
        # select crossover point that is not on the end of the string
        point = randint(1, len(par1) - 2)
        # perform crossover
        copy1 = par1[:point] + par2[point:]
        copy2 = par2[:point] + par1[point:]
    return [copy1, copy2]


def mutation(bitstring, mutation_r):
    """Mutation Operator."""
    bix = len(bitstring)
    for i in range(bix): # check for a mutation
        if rand() < mutation_r:
            bitstring[i] = 1 - bitstring[i]  # flip the bit


def genetic_algorithm(objective, num_bits, num_iter, num_pop, cross_r, mutation_r):
    """initial population of random bitstring"""
    pop = [randint(0, 2, num_bits).tolist() for _ in range(num_pop)]
    bet, best_eval = 0, objective(pop[0])  # keep track of best solution
    for gen in range(num_iter):  # enumerate generations
        # evaluate all candidates in the population
        scores = [objective(c) for c in pop]
        for i in range(num_pop):  # check for new best solution
            if scores[i] < best_eval:
                bet, best_eval = pop[i], scores[i]
                print(f">{gen}, new best {pop[i]} = {scores[i]}")
        selected = [selection(pop, scores) for _ in range(num_pop)]  # select parents
        children = []  # create the next generation

        for i in range(0, num_pop, 2):
            # get selected parents in pairs
            par1, par2 = selected[i], selected[i + 1]
            for cross in crossover(par1, par2, cross_r):  # crossover and mutation
                mutation(cross, mutation_r)
                children.append(cross)  # store for next generation
        # replace population
        pop = children
    return [bet, best_eval]


NUM_ITER1 = 100000  # define the total iterations
NUM_BITS1 = 52  # bits
NUM_POP1 = 10000  # define the population size
CROSS_R1 = 0.9  # crossover rate
MUTATION_R1 = 1.0 / float(NUM_BITS1)  # mutation rate
# perform the genetic algorithm search
best, score = genetic_algorithm(
    onemax, NUM_BITS1, NUM_ITER1, NUM_POP1, CROSS_R1, MUTATION_R1
)

print("Done!")
print(f"{best} = {score}")
