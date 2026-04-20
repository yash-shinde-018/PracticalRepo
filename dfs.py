# Simple DFS for a directed graph (no extra imports)
def dfs(adj, u, visited, order):
    visited.add(u)
    order.append(u)
    for v in adj[u]:
        if v not in visited:
            dfs(adj, v, visited, order)

def main():
    n = int(input("Enter number of vertices: ").strip())
    m = int(input("Enter number of edges: ").strip())
    print("Enter edges (u v) meaning u -> v:")
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)

    start = int(input("\nEnter starting node for DFS: ").strip())
    visited = set()
    order = []
    if 0 <= start < n:
        dfs(adj, start, visited, order)

    print("\nDFS Traversal:")
    if order:
        print(" ".join(map(str, order)))
    else:
        print("No nodes visited (check start node).")

if __name__ == "__main__":
    main()
