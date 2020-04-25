from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import ChartModule

from model import Simulation

from run import sim_params

def agent_portrayal(agent):
    portrayal = {"Shape": "circle",
                 "Filled": "true",
                 "Layer": 0,
                 "Color": "blue",
                 "r": 0.8}

    if agent.infected:
        portrayal["Color"] = "red"
        portrayal["Layer"] = 0
    else:
        if agent.immune:
            portrayal["Color"] = "green"
            portrayal["Layer"] = 0
        else:
            portrayal["Color"] = "blue"
            portrayal["Layer"] = 0

    if not agent.alive:
        portrayal["Color"] = "black"
        portrayal["Layer"] = 0

    return portrayal

grid = CanvasGrid(
    agent_portrayal,
    sim_params.get('grid_x'),
    sim_params.get('grid_y'),
    sim_params.get('grid_x') * 4,
    sim_params.get('grid_y') * 4)
chart = ChartModule([{"Label": "Infected",
                      "Color": "Red"},
                     {"Label": "Immune",
                      "Color": "Green"},
                     {"Label": "Deaths",
                      "Color": "Black"}],
                    data_collector_name='datacollector')
server = ModularServer(Simulation,
                       [grid, chart],
                       "COVID-19 Model",
                       {"params":sim_params})
server.port = 8521 # The default
server.launch()





