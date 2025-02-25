import random
import numpy as np

TARGET = 'Artificial Intelligence'

def compute_fitness(value: str, target: str):
    ### for each character in the value/target string
    ### compute the amount of matching characters and return this amount 
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
        
        pass

print("finished ...")