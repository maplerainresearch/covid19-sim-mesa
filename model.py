from mesa import Model
from mesa.time import RandomActivation
from person import Person
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector
import numpy as np
import matplotlib.pyplot as plt

def total_infected(model):
    total = 0
    for agent in model.schedule.agents:
        if agent.infected:
            total += 1
    return total

def total_deaths(model):
    total = 0
    for agent in model.schedule.agents:
        if not agent.alive:
            total += 1
    return total

def total_immune(model):
    total = 0
    for agent in model.schedule.agents:
        if agent.immune:
            total += 1
    return total

class Simulation(Model):
    """A model with some number of agents."""
    def __init__(self, params, seed=None):
        #self.num_agents = params.get('num_persons')
        self.num_agents = int(params.get('density') * params.get('grid_x') * params.get('grid_y'))
        self.grid = MultiGrid(params.get('grid_x'), params.get('grid_y'), True)
        self.schedule = RandomActivation(self)
        self.start_infected = params.get('initial_infected')
        self.recovery_period = params.get('recovery_period')
        self.infect_rate = params.get('infect_rate')
        self.mortality_rate = params.get('mortality_rate') / self.recovery_period
        self.active_ratio = params.get('active_ratio')
        self.immunity_chance = params.get('immunity_chance')
        self.quarantine_rate = params.get('quarantine_rate')
        self.lockdown_rate = params.get('lockdown_rate')
        
        self.running = True
        self.current_cycle = 0
        
        # Create agents
        for i in range(self.num_agents):
            a = Person(i, self)
            if self.random.random() < self.start_infected:
                a.set_infected()
            if self.random.random() < self.lockdown_rate:
                a.set_lockdown()
            self.schedule.add(a)
            # Add the agent to a random grid cell
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(a, (x, y))

        self.datacollector = DataCollector(
            model_reporters={
                "Infected": total_infected,
                "Deaths": total_deaths,
                "Immune": total_immune
            })

    def step(self):
        '''Advance the model by one step.'''
        self.datacollector.collect(self)
        self.schedule.step()
        self.current_cycle += 1
