import numpy as np
import matplotlib.pyplot as plt
import heapq
import time

class UGVPathfinder:
    def __init__(self, size=70, density=0.2):
        self.size = size
        self.grid = np.random.choice([0, 1], size=(size, size), p=[1-density, density])
        
    def heuristic(self, a, b):
        """Euclidean distance heuristic."""
        return np.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

    def get_neighbors(self, node):
        neighbors = []
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
            x, y = node[0] + dx, node[1] + dy
            if 0 <= x < self.size and 0 <= y < self.size and self.grid[x, y] == 0:
                neighbors.append((x, y))
        return neighbors

    def find_path(self, start, goal):
        if self.grid[start] == 1 or self.grid[goal] == 1:
            return None, 0, 0
        
        start_time = time.time()
        close_set = set()
        came_from = {}
        gscore = {start: 0}
        fscore = {start: self.heuristic(start, goal)}
        oheap = []
        heapq.heappush(oheap, (fscore[start], start))
        
        nodes_explored = 0

        while oheap:
            current = heapq.heappop(oheap)[1]
            nodes_explored += 1

            if current == goal:
                data = []
                while current in came_from:
                    data.append(current)
                    current = came_from[current]
                data.append(start)
                computation_time = (time.time() - start_time) * 1000 # ms
                return data[::-1], computation_time, nodes_explored

            close_set.add(current)
            for neighbor in self.get_neighbors(current):
                
                move_cost = 1.414 if (neighbor[0] != current[0] and neighbor[1] != current[1]) else 1
                tentative_g_score = gscore[current] + move_cost

                if neighbor in close_set and tentative_g_score >= gscore.get(neighbor, float('inf')):
                    continue
                
                if tentative_g_score < gscore.get(neighbor, float('inf')):
                    came_from[neighbor] = current
                    gscore[neighbor] = tentative_g_score
                    fscore[neighbor] = gscore[neighbor] + self.heuristic(neighbor, goal)
                    heapq.heappush(oheap, (fscore[neighbor], neighbor))
        
        return None, 0, nodes_explored

def run_simulation():
   
    size = 70
    densities = {"Low": 0.1, "Medium": 0.2, "High": 0.35}
    start, goal = (0, 0), (69, 69)
    
    for level, d in densities.items():
        ugv = UGVPathfinder(size, d)
       
        ugv.grid[start] = 0
        ugv.grid[goal] = 0
        
        path, c_time, nodes = ugv.find_path(start, goal)
        
        print(f"--- Results for {level} Density ({d*100}%) ---")
        if path:
            print(f"Path Found! Length: {len(path)} steps")
            print(f"Execution Time: {c_time:.2f} ms")
            print(f"Nodes Explored: {nodes}")
            
            
            plt.figure(figsize=(8,8))
            plt.imshow(ugv.grid, cmap='binary')
            path_x, path_y = zip(*path)
            plt.plot(path_y, path_x, color='red', linewidth=2, label='UGV Path')
            plt.scatter([start[1]], [start[0]], color='green', label='Start')
            plt.scatter([goal[1]], [goal[0]], color='blue', label='Goal')
            plt.title(f"UGV Navigation: {level} Density")
            plt.legend()
            plt.show()
        else:
            print("No path found due to obstacle density.")

if __name__ == "__main__":
    run_simulation()
