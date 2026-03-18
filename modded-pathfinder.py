import numpy as np
import matplotlib.pyplot as plt
import heapq

class DynamicUGV:
    def __init__(self, size=70, density=0.2):
        self.size = size
        self.real_world = np.random.choice([0, 1], size=(size, size), p=[1-density, density])
        self.internal_map = np.zeros((size, size))
        self.sensor_range = 5 

    def heuristic(self, a, b):
        return np.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

    def get_neighbors(self, node, grid):
        neighbors = []
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
            x, y = node[0] + dx, node[1] + dy
            if 0 <= x < self.size and 0 <= y < self.size and grid[x, y] == 0:
                neighbors.append((x, y))
        return neighbors

    def a_star(self, start, goal):
        oheap = []
        heapq.heappush(oheap, (0, start))
        came_from = {}
        g_score = {start: 0}
        
        while oheap:
            current = heapq.heappop(oheap)[1]
            if current == goal:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                return path[::-1]

            for neighbor in self.get_neighbors(current, self.internal_map):
                cost = 1.414 if (neighbor[0]!=current[0] and neighbor[1]!=current[1]) else 1
                tentative_g = g_score[current] + cost
                if tentative_g < g_score.get(neighbor, float('inf')):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_score = tentative_g + self.heuristic(neighbor, goal)
                    heapq.heappush(oheap, (f_score, neighbor))
        return None

    def navigate(self, start, goal):
        current_pos = start
        actual_path = [start]
        self.real_world[start] = 0
        self.real_world[goal] = 0
        replan_count = 0
        
        while current_pos != goal:
            for i in range(max(0, current_pos[0]-self.sensor_range), min(self.size, current_pos[0]+self.sensor_range)):
                for j in range(max(0, current_pos[1]-self.sensor_range), min(self.size, current_pos[1]+self.sensor_range)):
                    if self.real_world[i, j] == 1:
                        self.internal_map[i, j] = 1
            
            path = self.a_star(current_pos, goal)
            if not path:
                return None, replan_count

            next_step = path[0]
            if self.real_world[next_step] == 1:
                replan_count += 1
                continue 
            
            current_pos = next_step
            actual_path.append(current_pos)
            if len(actual_path) > 2000:
                break

        return actual_path, replan_count

if __name__ == "__main__":
    ugv = DynamicUGV(density=0.2)
    start, goal = (0,0), (69,69)
    path, replans = ugv.navigate(start, goal)

    if path:
        print(f"Goal Reached. Replans: {replans}")
        route = np.array(path)
        plt.imshow(ugv.real_world, cmap='binary')
        plt.plot(route[:,1], route[:,0], color='red', label='UGV Actual Path')
        plt.legend()
        plt.show()
    else:
        print("Path blocked.")
