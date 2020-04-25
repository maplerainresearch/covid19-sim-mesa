# COVID-19 multi-agent simulation using Mesa

This is a simplistic multi-agent simulation of how COVID-19 can spread.<br>
<br>
`main.py`: For running from the commandline. At the end of the run, a chart will show the simulation results.<br>
`run.py`: Main python module for running the simulation. The simulation settings can be changed here.<br>
`server.py`: Visualization module that uses a web browser for visualizing the simulation. Running this will display the simulation grid and a chart of results that can be stepped through or run continuously.<br>
<br>
`model.py`: The simulation model.<br>
`person.py`: Agent model that represents one person.<br>
<br>
Some additional information on this simulation can be found [here](https://teck78.blogspot.com/2020/04/using-mesa-framework-to-simulate-spread.html) here.<br>
<br>
This simulation uses the [Mesa](https://github.com/projectmesa/mesa) Mesa framework and is licensed under the Apache License, Version 2.0.<br>
Copyright 2020 Maple Rain Research Co., Ltd.<br>