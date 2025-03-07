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

    def populate(self):
        self.agents = [Agent(self.random_string()) for _ in range(self.n_pop)]

    def random_string(self):
        # sample from GENES pool and join genes together
        return ''.join(random.choice(self.GENES) for _ in range(self.max_len))
    
    def evaluate(self, target):
        # evaluate agents
        fitness_scores = [compute_fitness(a.value, target) for a in self.agents]
        # sort agents based on fitness score
        sorted_agents = sorted(zip(fitness_scores, self.agents), reverse=True, key=lambda x: x[0])
        # return sorted agent list and best agent 
        return [a for _, a in sorted_agents], sorted_agents[0]
    
    def cross_over(self, parents, mutation_rate=0.1):
        # define new generation
        new_population = Population(self.n_pop, self.max_len)

        for _ in range(new_population.n_pop):          
            # for n parents there are n-1 cutoffs  
            cutoffs = np.random.choice(self.max_len, len(parents)-1, replace=False).tolist()
            # to index, we need the begin and end indices (0 and max_len)
            cutoffs = sorted(list(set([0] + cutoffs + [self.max_len])))
            # take partitions from all parents and join the substrings
            value = ''.join([p.value[i:j] for i, j, p in zip(cutoffs, cutoffs[1:], parents)])

            # small random changes to not get stuck local optima
            if random.random() < mutation_rate:
                list_value = list(value)
                idx = random.randint(0, self.max_len-1)
                list_value[idx] = random.choice(self.GENES)
                value = ''.join(list_value)
            
            new_population.agents.append(Agent(value))
        
        return new_population

p = Population(10, 5)
p.populate()
[a.value for a in p.agents]

num_parents = 2
mutation_rate = 0.05
population = Population(n_pop=200, max_len=len(TARGET))
population.populate()

for i in range(999999):
    sorted_agents, best_fitness = population.evaluate(TARGET)
    print(f'iter: {i}, best fitness: {best_fitness[0]}, value: "{sorted_agents[0].value}"')
    parents = sorted_agents[:num_parents]
    new_population = population.cross_over(parents, mutation_rate)
    population = new_population
    if sorted_agents[0].value == TARGET: break