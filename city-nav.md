this program calculates the actual cumulative distance across a network of highways.

When navigating a map where every road has a different "cost" (length), we use **Dijkstra’s Algorithm** 

## Implementation Details
* **Graph Representation:** I converted the CSV data into an "Adjacency List." Each city is a node, and the roads are edges with weights representing kilometers.
* **The Priority Queue:** To keep the search fast, the program uses a "Min-Heap." 
* **Bi-directional Logic:** Since roads run both ways, the script treats every connection in the dataset as a two-way street.

## Key Insights (Measures of Effectiveness)
* **Mathematical Optimality:** Because Dijkstra is complete and optimal, the distances provided are guaranteed to be the shortest possible given the dataset.
* **Path Transparency:** The program doesn't just give a number; it traces the trail e.g., *Hyderabad -> Pune -> Mumbai*
* **Efficiency:** Even with a complex network of cities, the algorithm finishes quickyl

## How to Use
1. Ensure your dataset is named `indian-cities-dataset.csv`.
2. Run the script:
   ```bash
   python city_navigator.py
