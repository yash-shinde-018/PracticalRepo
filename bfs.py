from collections import deque
def bfs(graph, start):
    visited = {start}
    q = deque([start])
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in graph.get(u, []):
            if v not in visited:
                visited.add(v)
                q.append(v)
    return order
def read_graph():
    n = int(input("Number of nodes: ").strip())
    g = {}
    for _ in range(n):
        parts = input().split()
        if not parts:
            continue
        node = int(parts[0])
        g[node] = [int(x) for x in parts[1:]] if len(parts) > 1 else []
    return g
if __name__ == "__main__":
    graph = read_graph()
    start = int(input("Start node: ").strip())
    print("BFS order:", bfs(graph, start))
