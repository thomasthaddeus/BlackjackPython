"""Genetic Algorithm for Continuous Function Optimization

Optimizing the OneMax function is not very interesting;
we are more likely to want to optimize a continuous function.
For example, we can define the x^2 minimization function that
takes input variables and has an optima at  f(0, 0) = 0.0.
"""

# genetic algorithm search for continuous function optimization
from numpy.random import rand, randint


def decode(bounds1, n_bits, bitstring):
    """Decode bitstring to numbers."""
    decodedr = list()
    largest = 2**n_bits
    bind = len(bounds1)
    for i in range(bind):  # extract the substring
        start, end = i * n_bits, (i * n_bits) + n_bits
        substring = bitstring[start:end]
        chars = "".join(
            [str(s) for s in substring]
        )  # convert bitstring to a string of chars
        integer = int(chars, 2)  # convert string to integer
        # scale integer to desired range
        value = bounds1[i][0] + (integer / largest) * (bounds1[i][1] - bounds1[i][0])
        decodedr.append(value)
    return decodedr


def objective(numx):
    """Objective function."""
    return float(numx[1]**2 + numx[0]**2)


def selection(pop, scores, k=3):
    """tournament selection"""
    selection_ix = randint(len(pop))  # first random selection
    for i in randint(0, len(pop), k - 1):
        # check if better (e.g. perform a tournament)
        if scores[i] < scores[selection_ix]:
            selection_ix = i
    return pop[selection_ix]


def crossover(parent1, parent2, r_cross):
    """crossover two parents to create two children"""
    cross1, cross2 = (
        parent1.copy(),
        parent2.copy(),
    )  # children are copies of parents by default
    if rand() < r_cross:  # check for recombination
        pnt = randint(
            1, len(parent1) - 2
        )  # select crossover point that is not on the end of the string
        cross1 = parent1[:pnt] + parent2[pnt:]
        cross2 = parent2[:pnt] + parent1[pnt:]
    return [cross1, cross2]


def mutation(bitstring, mutation_r):
    """Mutation Operator."""
    bix = len(bitstring)
    for i in range(bix):  # check for a mutation
        if rand() < mutation_r:
            bitstring[i] = 1 - bitstring[i]  # flip the bit


def genetic_algorithm(objective, bounds2, n_bits, n_iter, n_pop, r_cross, r_mut):
    """Genetic algorithm"""
    # initial population of random bitstring
    pop = [randint(0, 2, n_bits * len(bounds2)).tolist() for _ in range(n_pop)]
    # keep track of best solution
    best1, best_eval = 0, objective(decode(bounds2, n_bits, pop[0]))
    # enumerate generations
    for gen in range(n_iter):
        # decode population
        decoded1 = [decode(bounds2, n_bits, p) for p in pop]
        # evaluate all candidates in the population
        scores = [objective(d) for d in decoded1]
        # check for new best solution
        for i in range(n_pop):
            if scores[i] < best_eval:
                best1, best_eval = pop[i], scores[i]
                print(f">{gen}, new best {decoded1[i]} = {scores[i]}")
        # select parents
        selected = [selection(pop, scores) for _ in range(n_pop)]
        # create the next generation
        children = list()
        for i in range(0, n_pop, 2):
            # get selected parents in pairs
            par1, par2 = selected[i], selected[i + 1]
            # crossover and mutation
            for cro in crossover(par1, par2, r_cross):
                # mutation
                mutation(cro, r_mut)
                # store for next generation
                children.append(cro)
        # replace population
        pop = children
    return [best1, best_eval]


bounds = [[-5.0, 5.0], [-5.0, 5.0]]  # define range for input
NUM_ITER1 = 100  # define the total iterations
NUM_BITS1 = 16  # bits per variable
NUM_POP1 = 100  # define the population size
CROSS_R1 = 0.9  # crossover rate
MUTATION_R1 = 1.0 / (float(NUM_BITS1) * len(bounds))  # mutation rate
best, score = genetic_algorithm(
    obj, bounds, NUM_BITS1, NUM_ITER1, NUM_POP1, CROSS_R1, MUTATION_R1
)  # perform the genetic algorithm search
print("Done!")
decoded = decode(bounds, NUM_BITS1, best)
print(f"{decoded} = {score}")
