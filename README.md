## Purpose

This repo serves the following functions:
1. To compare the performance of OpenDSS and Pandapower in modelling a simple network from the ENWL project.
2. To get feedback on how well I managed to convert an OpenDSS model to Pandapower.

Depending on your level of interest you can look at the following files:

1. `comparison_nb.ipynb`: Simply loads in the bus / line voltages from the outputs of both solvers and compares the difference in their results.
2. `opendss/network.py`: Compiles and runs the 4 wire OpenDSS model kindly provided by Frederik Geth, and processes the output data into a useful CSV form.
3. `pandapower/network.py`: Creates a Pandapower that is intended to be equivalent to the OpenDSS model. It is worth noting that I performed the transformation between formats by hand and there may be mistakes. If you find any please let me know. There are a great deal more required parameters for Pandapower than for OpenDSS so I may have chosen incorrectly. 

