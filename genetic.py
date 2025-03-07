import numpy as np
import random

def fitness(schedule, jobs):
    time_slots = [0] * max(job.deadline for job in jobs)
    total_profit = 0
    completed_jobs = 0

    for job_id in schedule:
        job = jobs[job_id]
        # range() goes from latest deadline to earliest deadline
        # provides more flexibility in fitting jobs within the schedule based on deadlines
        # jobs will run as late as possible to maximize amount of jobs to run in earlier timeslots
        for t in range(min(job.deadline, len(time_slots)) -1, -1, -1):
            if time_slots[t] == 0:
                time_slots[t] = job.id
                total_profit += job.profit
                completed_jobs += 1
                break
        
        return total_profit, completed_jobs

# Note to self: read up on classes in py
class Job:
    def __init__(self, id: str, deadline: int, profit: int) -> None:
        self.id = id
        self.deadline = deadline
        self.profit = profit 

class Agent:
    def __init__(self, schedule):
        self.schedule = schedule
        self.fitness = 0

class Population:
    def __init__(self, n_pop: int, jobs: int):
        self.n_pop = n_pop
        self.jobs = jobs
        self.agents = []

    def populate(self):
        self.agents = [Agent(random.sample(range(len(self.jobs)), len(self.jobs))) for _ in range(self.n_pop)]
    
    def evaluate(self, target):
        for agent in self.agents:
        
    
    def cross_over(self, parents, mutation_rate = 0.1):
        new_population = Population(self.n_pop, self.max_len)
        return new_population

    # Genes will be possible slots for a job to occur
    # Separate gene for each shift for every controller over a whole week
    # Gene should represent the solution

    GENES = ""
    
