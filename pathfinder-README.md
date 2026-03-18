# UGV Pathfinding Simulation

## Overview
This project implements a pathfinding system for an Unmanned Ground Vehicle (UGV) operating on a 70x70 km grid. The goal is to calculate the most efficient route from a designated start point to a goal point while navigating around randomly generated obstacles of varying densities.

## Design Methodology
The core logic relies on the **A* (A-Star) Search Algorithm**. I chose A* because it provides a mathematically optimal path while remaining computationally efficient by using heuristics to guide the search.

### Pathfinding Logic
The algorithm evaluates the "cost" of potential paths using the standard formula:
**f(n) = g(n) + h(n)**

* **g(n):** The actual distance traveled from the start to the current node.
* **h(n):** The estimated distance to the goal (Heuristic). 

To allow for more realistic movement, the simulation supports **8-way adjacency** (horizontal, vertical, and diagonal moves). I utilized **Euclidean distance** for the heuristic to ensure the UGV prioritizes diagonal shortcuts when they are available, as this results in a shorter total distance than standard grid-based movement.

## Features
* **Grid Map:** A 70x70 matrix representing the operational area.
* **Variable Obstacle Density:** The system generates three levels of environmental complexity:
    * **Low (10%):** Sparse obstacles.
    * **Medium (20%):** Moderate clutter.
    * **High (35%):** Dense environment testing the limits of the pathfinder.
* **Visualization:** A visual trace of the final path is rendered using Matplotlib, showing the start, the goal, and the obstacles.

## Measures of Effectiveness (MoE)
To evaluate the algorithm’s performance, the simulation tracks and outputs four primary metrics:
1.  **Path Length:** Total distance units covered.
2.  **Execution Time:** The time (in milliseconds) required to compute the solution.
3.  **Nodes Explored:** The number of grid cells analyzed, representing the algorithm's search efficiency.
4.  **Feasibility:** A check to verify if a valid path was found given the specific obstacle layout.

## Setup and Usage
The project is written in Python 3 and requires `numpy` for grid management and `matplotlib` for visualization.

### Installation
```bash
pip install numpy matplotlib
