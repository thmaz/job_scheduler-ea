import random
import numpy as np

def fitness(schedule, jobs):
    max_deadline = max(job.deadline for job in jobs)
    time_slots = [-1] * max_deadline
    total_profit = 0
    completed_jobs = 0

    used_jobs = set()  # Track scheduled jobs

    # Sort jobs by deadline first, then by profit in descending order
    sorted_jobs = sorted([jobs[job_id] for job_id in schedule], key=lambda j: (j.deadline, -j.profit))

    for job in sorted_jobs:
        # Try placing job in the latest available slot before its deadline
        for t in range(job.deadline - 1, -1, -1):
            if time_slots[t] == -1:
                time_slots[t] = job.id
                used_jobs.add(job.id)
                total_profit += job.profit
                completed_jobs += 1
                break 

    scheduled_jobs = [job for job in time_slots if job != -1]
    return total_profit, completed_jobs, scheduled_jobs

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
    def __init__(self, n_pop: int, jobs: list, selection_method: str):
        self.n_pop = n_pop
        self.jobs = jobs
        self.agents = []
        self.selection_method = selection_method

    def populate(self):
        self.agents = [Agent(random.sample(range(len(self.jobs)), len(self.jobs))) for _ in range(self.n_pop)]
    
    def evaluate(self):
        for agent in self.agents:
            agent.fitness, _, _ = fitness(agent.schedule, self.jobs)
        self.agents.sort(key=lambda a: a.fitness, reverse=True)
    
    def select_parent(self, tournament_size: int = 3):
        if self.selection_method == "tournament":
            return self.tournament_selection(tournament_size)
        elif self.selection_method == "roulette":
            return self.rwheel_selection()
        elif self.selection_method == "elitism":
            return self.elitism_selection()
        else:
            raise ValueError("Invalid selection method.")
        
    # Tournament selection:
    # Best agents from the tournament get selected from random subset of agents
    # Size of tournament is set in ga_run function
    def tournament_selection(self, tournament_size: int):
        tournament = random.sample(self.agents, tournament_size)
        return max(tournament, key=lambda a: a.fitness)
    
    # Roulette wheel selection:
    # Change agent gets selected is proportional to their fitness
    def rwheel_selection(self):
        total_fitness = sum(agent.fitness for agent in self.agents)
        selection_chance = [agent.fitness / total_fitness for agent in self.agents]
        return np.random.choice(self.agents, p=selection_chance)
    
    # Elitism selection:
    # Best agent gets picked
    def elitism_selection(self):
        return self.agents[0] # Sorting by best agent takes place in evaluate function

    # Crossover based on jobs so deadlines will be respected during crossover
    # Randomly select a subset of jobs from one parent
    # Create child schedule that includes these jobs and fills remaining open slots from other parents jobs
    def cross_over(self, tournament_size: int, crossover_method: str):
        new_population = Population(self.n_pop, self.jobs, self.selection_method)

        for _ in range(new_population.n_pop):
            # Use tournament sample instead of only random selection, tournament size can be adjusted
            parent1 = self.select_parent(tournament_size)
            parent2 = self.select_parent(tournament_size)

            if crossover_method == "order":
                child_schedule = self.order_crossover(parent1.schedule, parent2.schedule)
            elif crossover_method == "pmx":
                child_schedule = self.pm_crossover(parent1.schedule, parent2.schedule)
            else:
                raise ValueError("Method Invalid! Choose from: 'pmx' or 'order'")

            new_population.agents.append(Agent(child_schedule))

        return new_population
    
    # Order Crossover:
    # This method makes child while preserving the order of jobs from parents.
    def order_crossover(self, p1, p2):
        size = len(p1)
        start, end = sorted(random.sample(range(size), 2))

        child = [-1] * size
        child[start:end] = p1[start:end]

        p2_pos = 0
        for i in range(size):
            if child[i] == -1:
                while p2[p2_pos] in child:
                    p2_pos += 1
                child[i] = p2[p2_pos]

        return child
    
    # Partially mapped crossover:
    # This method also maintains relative order, but lets each element appear only once
    def pm_crossover(self, p1, p2): # Gets stuck in loop for crossover functions
        size = len(p1)
        start, end = sorted(random.sample(range(size), 2))

        child = [-1] * size
        mapping = {}

        # Copy segment from Parent 1 to child
        for i in range(start, end):
            child[i] = p1[i]
            mapping[p1[i]] = p2[i]
        
        seen_values = set(mapping.keys())

        # Fill remaining slots ensuring uniqueness
        for i in range(size):
            if child[i] == -1:
                val = p2[i]
                while val in seen_values:
                    if val not in mapping:
                        break
                    val = mapping[val]
                child[i] = val
                seen_values.add(val)

        # Ensure the child is a valid permutation of jobs
        available_jobs = set(range(size)) - set(child)
        for i in range(size):
            if child[i] == -1:
                child[i] = available_jobs.pop()

        return child

    def mutate(self, mutation_rate: float, mutation_method: str):
        """Mutation function with method selection."""
        for agent in self.agents:
            if random.random() < mutation_rate:
                if mutation_method == "swap":
                    self.swap_mutation(agent.schedule)
                elif mutation_method == "random_reset":
                    self.random_resetting(agent.schedule)
                else:
                    raise ValueError("Method Invalid! Choose from: 'swap' or 'random_reset'")

    # Swap mutation:
    # Swap two random genes
    def swap_mutation(self, schedule):
        idx1, idx2 = random.sample(range(len(schedule)), 2)
        schedule[idx1], schedule[idx2] = schedule[idx2], schedule[idx1]

    # Random resetting:
    # Replace a random gene with a new gene
    def random_resetting(self, schedule):
        idx = random.randint(0, len(schedule) - 1)
        available_jobs = list(set(range(len(schedule))) - set(schedule))
        if available_jobs:
            schedule[idx] = random.choice(available_jobs)  # Replace with a random job ID

    
    def print_chromosomes(self):
        for idx, agent in enumerate(self.agents):
            schedule_str = ', '.join(str(job_id) for job_id in agent.schedule)
            print(f"Chromosome {idx + 1}: Schedule = [{schedule_str}]")

def ga_run(jobs: int, pop_size: int, generations: int, mutation_rate: float, tournament_size: int, selection_method: str, crossover_method: str, mutation_method: str):
    pop = Population(pop_size, jobs, selection_method)
    pop.populate()

    print("Initial Population of Chromosomes:")
    pop.print_chromosomes()

    for i in range(generations):
        pop.evaluate()
        top_agent = max(pop.agents, key=lambda a: a.fitness)
        max_profit, job_count, best_schedule = fitness(top_agent.schedule, jobs)
        
        # Print the best agent's details for the current generation
        # print(f"Generation {i}: Best agent - Jobs completed: {job_count}, Maximum profit: {max_profit}")
        new_pop = pop.cross_over(tournament_size, crossover_method)
        new_pop.mutate(mutation_rate, mutation_method)
        pop = new_pop

    max_profit, job_count, best_schedule = fitness(top_agent.schedule, jobs)
    return max_profit, job_count, best_schedule

print("Import success")