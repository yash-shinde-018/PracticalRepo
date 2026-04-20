import heapq

def a_star(graph, start, goal, h):
    # graph: {node: [(neighbor, cost), ...], ...}
    open_set = [(h[start], 0, start, None)]  # (f = g+h, g, node, parent)
    came_from = {}  # node -> parent
    g_score = {start: 0}
    closed = set()

    while open_set:
        f, g, node, parent = heapq.heappop(open_set)
        if node in closed:
            continue
        came_from[node] = parent
        if node == goal:
            # reconstruct path
            path = []
            cur = node
            while cur is not None:
                path.append(cur)
                cur = came_from[cur]
            return list(reversed(path)), g
        closed.add(node)
        for nei, cost in graph.get(node, []):
            tentative_g = g + cost
            if nei in closed and tentative_g >= g_score.get(nei, float('inf')):
                continue
            if tentative_g < g_score.get(nei, float('inf')):
                g_score[nei] = tentative_g
                heapq.heappush(open_set, (tentative_g + h.get(nei, 0), tentative_g, nei, node))
    return None, None

def read_graph():
    n = int(input("Enter number of vertices: ").strip())
    m = int(input("Enter number of edges: ").strip())
    print("Enter edges (u v cost) meaning u -> v with given cost:")
    graph = {i: [] for i in range(n)}
    for _ in range(m):
        u, v, c = map(int, input().split())
        graph[u].append((v, c))
    print("Enter heuristic (h) for each node (space separated):")
    h_vals = list(map(float, input().split()))
    h = {i: h_vals[i] for i in range(len(h_vals))}
    return graph, h

if __name__ == "__main__":
    graph, h = read_graph()
    start = int(input("Enter start node: ").strip())
    goal = int(input("Enter goal node: ").strip())
    path, cost = a_star(graph, start, goal, h)
    print("\nA* Result:")
    if path:
        print("Path:", " -> ".join(map(str, path)))
        print("Total cost:", cost)
    else:
        print("No path found from", start, "to", goal)


Enter number of vertices: 4
Enter number of edges: 6
Enter edges (u v cost) meaning u -> v with given cost:
2 0 1
0 2 1
1 2 1
0 1 2
3 3 0
1 3 3
Enter heuristic (h) for each node (space separated):
2 1 3 0
Enter start node: 2
Enter goal node: 3

A* Result:
Path: 2 -> 0 -> 1 -> 3
Total cost: 6
