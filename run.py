from person import Person
from model import *

# Simulation parameters
sim_params = {
    "num_persons": 1000,  # number of persons in simulation
    "grid_x": 100,  # size of grid: X axis
    "grid_y": 100,  # size of grid: Y axis
    "density": 0.1,  # population density
    "initial_infected": 0.01,  # initial percentage of population infected
    "infect_rate": 0.1,  # chance to infect someone in close contact
    "recovery_period": 14 * 24,  # number of hours to recover after being infected, 0 for never
    "mortality_rate": 0.005,  # mortality rate among those infected
    "active_ratio": 8 / 24.0,  # ratio of hours in the day when active
    "immunity_chance": 1.0,  # chance of infection granting immunity after recovery
    "quarantine_rate": 0.9,  # percentage in quarantine
    "cycles": 10 * 24  # cycles to run, 0 for infinity
}  # end of parameters

model = Simulation(sim_params)
current_cycle = 0
cycles_to_run = sim_params.get('cycles')
#print(cycles_to_run)
#print(sim_params)
while 1:
    model.step()
    if cycles_to_run > 0 and current_cycle >= cycles_to_run:
        break
    current_cycle += 1
