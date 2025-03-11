import random

def fitness(schedule, jobs):
    time_slots = [-1] * max(job.deadline for job in jobs)
    total_profit = 0
    completed_jobs = 0

    print("\nJob Placement Process:")
    for job_id in schedule:
        job = jobs[job_id]
        # range() goes from latest deadline to earliest deadline
        # provides more flexibility in fitting jobs within the schedule based on deadlines
        # jobs will run as late as possible to maximize amount of jobs to run in earlier timeslots
        for t in range(min(job.deadline, len(time_slots)) -1, -1, -1):
            if time_slots[t] == -1:
                time_slots[t] = job.id
                total_profit += job.profit
                completed_jobs += 1
                print(f"Placing Job {job.id} at time slot {t} (Profit: {job.profit})")
                break
    return total_profit, completed_jobs

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
    
    def evaluate(self):
        for agent in self.agents:
            agent.fitness, _ = fitness(agent.schedule, self.jobs)
        self.agents.sort(key=lambda a: a.fitness, reverse=True)
    
    # Random subset of agents, best agents from the tournament get selected
    def tournament_selection(self, tournament_size: int):
        tournament = random.sample(self.agents, tournament_size)

        return max(tournament, key=lambda a: a.fitness)

    # Crossover based on jobs so deadlines will be respected during crossover
    # Randomly select a subset of jobs from one parent
    # Create child schedule that includes these jobs and fills remaining open slots from other parents jobs
    def cross_over(self, tournament_size: int):
        new_population = Population(self.n_pop, self.jobs)

        for _ in range(new_population.n_pop):
            # Use tournament sample instead of only random selection, tournament size can be adjusted
            parent1 = self.tournament_selection(tournament_size)
            parent2 = self.tournament_selection(tournament_size)

            # Random subset of jobs get selected from parent 1
            num_selected_jobs = random.randint(1, len(parent1.schedule))

            selected_jobs = random.sample(parent1.schedule, num_selected_jobs)
            
            # Create child with selected jobs from parent 1
            child_schedule = selected_jobs[:]

            # Remaining slots filled with jobs from parent 2, while respecting deadlines
            for job_id in parent2.schedule:
                if job_id not in child_schedule:
                    child_schedule.append(job_id)
                if len(child_schedule) == len(parent1.schedule):
                    break
            new_population.agents.append(Agent(child_schedule))
        return new_population
    
    def mutate(self, mutation_rate: float):
        for agent in self.agents:
            if random.random() < mutation_rate:
                idx1, idx2 = random.sample(range(len(agent.schedule)), 2)
                
                agent.schedule[idx1], agent.schedule[idx2] = agent.schedule[idx2], agent.schedule[idx1]
    
    def print_chromosomes(self):
        for idx, agent in enumerate(self.agents):
            schedule_str = ', '.join(str(job_id) for job_id in agent.schedule)
            print(f"Chromosome {idx + 1}: Schedule = [{schedule_str}]")


def ga_run(jobs: int, pop_size: int, generations: int, mutation_rate: float, tournament_size: int):
    pop = Population(pop_size, jobs)
    pop.populate()
    print("Initial Population of Chromosomes:")
    pop.print_chromosomes()
    for i in range(generations):
        pop.evaluate()

        top_agent = max(pop.agents, key=lambda a: a.fitness)
        max_profit, job_count = fitness(top_agent.schedule, jobs)
        
        # Print the best agent's details for the current generation
        print(f"Generation {i}: Best agent - Jobs completed: {job_count}, Maximum profit: {max_profit}")
        new_pop = pop.cross_over(tournament_size)
        new_pop.mutate(mutation_rate)
        pop = new_pop
    
    max_profit, job_count = fitness(top_agent.schedule, jobs)
    return max_profit, job_count

print("Import success")