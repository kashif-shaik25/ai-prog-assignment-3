import pandas as pd
import heapq

def build_graph(file_path):
    df = pd.read_csv(file_path)
    graph = {}
    for _, row in df.iterrows():
        u, v, d = row['Origin'], row['Destination'], row['Distance']
        if u not in graph: graph[u] = []
        if v not in graph: graph[v] = []
        # Add edges both ways (undirected road network)
        graph[u].append((v, d))
        graph[v].append((u, d))
    return graph

def dijkstra(graph, start):
    # Standard Dijkstra/Uniform-Cost Search implementation
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    predecessors = {node: None for node in graph}
    
    while pq:
        current_dist, u = heapq.heappop(pq)
        
        if current_dist > distances[u]:
            continue
            
        for v, weight in graph.get(u, []):
            distance = current_dist + weight
            if distance < distances[v]:
                distances[v] = distance
                predecessors[v] = u
                heapq.heappush(pq, (distance, v))
                
    return distances, predecessors

def get_path_string(predecessors, target):
    path = []
    curr = target
    while curr is not None:
        path.append(curr)
        curr = predecessors[curr]
    return " -> ".join(path[::-1])

def run_analysis(start_node):
    graph = build_graph('indian-cities-dataset.csv')
    
    if start_node not in graph:
        print(f"Error: {start_node} not found in dataset.")
        return

    distances, predecessors = dijkstra(graph, start_node)
    
    print(f"{'Destination City':<20} | {'Distance (km)':<15} | {'Shortest Path'}")
    print("-" * 70)
    
    for city in sorted(distances.keys()):
        dist = distances[city]
        path = get_path_string(predecessors, city)
        print(f"{city:<20} | {dist:<15} | {path}")

if __name__ == "__main__":
    run_analysis('Hyderabad')
