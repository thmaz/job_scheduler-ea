import numpy as np
import random

TARGET = 'Artificial intelligence'

def compute_fitness(value: str, target: str):
    ### for each character in the value/target string
    ### compute the amount of matching characters and return this amount 
    fitness = 0
    for val, tgt in zip(value, target):
        fitness += val == tgt
    return fitness

assert compute_fitness('    cif hello world', TARGET) == 3