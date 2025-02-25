import random
import numpy as np

TARGET = 'Artificial Intelligence'

def compute_fitness(value: str, target: str):
    # Compute the amount of matching characters in target string
    fitness = 0
    for val, tgt in zip(value, target):
        fitness += val == tgt
        return fitness

class Agent:
    def __init__(self, value: str) -> None:
        self.value = value

class Population:
    GENES = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOP
                QRSTUVWXYZ 1234567890, .-;:_!"#%&/()=?@${[]}'''

    def __init__(self, n_pop: int, max_len: int) -> None:
        self.n_pop = n_pop
        self.max_len = max_len
        self.agents = []

    def random_string(self):
        # Return random sample from "GENES"
        return ''.join(random.choice(self.GENES) for _ in range(self.max_len))

    def populate(self):
        # Populate list with random strings
        self.agents = [Agent(self.random_string()) for _ in range(self.max_len)]
        pass

    def evaluate(self, target):
        # Evaluate fitness of agents by comparing value with target
        fitness = [compute_fitness(a.value, target) for a in self.agents]

        # Sort based on fitness score
        
        pass

    def cross_over(self, parents, mutation_rate=0.1):
    # define new generation
        new_population = Population(self.n_pop, self.max_len)

        for _ in range(new_population.n_pop):          
            value = None
            # For each new agent in the next population, select parents and combine their genes
            # You are free to define the selection and combination procedures
            
            # Mutate newly created agent by adjusting its genes (value)
            # hint: with probability mutation_rate you randomly add noise
            
            new_population.agents.append(Agent(value))
        
        return new_population

p = Population(10, 5)
p.populate()
[a.value for a in p.agents]

print("finished ...")