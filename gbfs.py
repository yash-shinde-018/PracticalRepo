import heapq
def greedy_best_first_search(graph, start, goal, heuristic):
    open_list = []
    heapq.heappush(open_list, (heuristic[start], start))
    visited = set()
    parent = {start: None}
    while open_list:
        _, current = heapq.heappop(open_list)
        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1]
        visited.add(current)
        for neighbor in graph[current]:
            if neighbor not in visited:
                parent[neighbor] = current
                heapq.heappush(open_list, (heuristic[neighbor], neighbor))
    return None

# Input section
graph = {}
heuristic = {}
n = int(input("Enter number of nodes: "))
print("\nEnter node names:")
nodes = input().split()
print("\nEnter adjacency list (space separated neighbors):")
for node in nodes:
    neighbors = input(f"Neighbors of {node}: ").split()
    graph[node] = neighbors
print("\nEnter heuristic values:")
for node in nodes:
    h = int(input(f"Heuristic value of {node}: "))
    heuristic[node] = h
start = input("\nEnter start node: ")
goal = input("Enter goal node: ")
path = greedy_best_first_search(graph, start, goal, heuristic)
if path:
    print("\nPath found:", " -> ".join(path))
else:
    print("\nNo path found.")

Enter number of nodes: 8
Enter node names:
A B C D E F G H
Enter adjacency list (space separated neighbors):
Neighbors of A: B C D
Neighbors of B: E
Neighbors of C: E F
Neighbors of D: F
Neighbors of E: H
Neighbors of F: 
Neighbors of G: F
Neighbors of H: G
Enter heuristic values:
Heuristic value of A: 40
Heuristic value of B: 32
Heuristic value of C: 25
Heuristic value of D: 35
Heuristic value of E: 19
Heuristic value of F: 17
Heuristic value of G: 0
Heuristic value of H: 10
Enter start node: A
Enter goal node: G