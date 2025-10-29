# pagerank.py
import numpy as np

def pagerank(adj_matrix, d=0.85, eps=1e-6, max_iter=100):
    n = adj_matrix.shape[0]
    # build stochastic matrix M where M[j,i] = 1/outdeg(i) if i -> j
    outdeg = adj_matrix.sum(axis=0)
    M = np.zeros_like(adj_matrix, dtype=float)
    for i in range(n):
        if outdeg[i] == 0:
            # handle dangling node: distribute uniformly
            M[:, i] = 1.0 / n
        else:
            M[:, i] = adj_matrix[:, i] / outdeg[i]
    pr = np.ones(n) / n
    teleport = (1.0 - d) / n
    for it in range(max_iter):
        new_pr = d * M.dot(pr) + teleport
        if np.linalg.norm(new_pr - pr, 1) < eps:
            pr = new_pr
            break
        pr = new_pr
    return pr

if __name__ == "__main__":
    # adjacency matrix where A[i,j] = 1 if j -> i (column j points to row i)
    A = np.array([
        [0,1,1,0],
        [1,0,0,0],
        [1,0,0,1],
        [0,1,0,0]
    ], dtype=float)
    ranks = pagerank(A)
    print("PageRank scores:", ranks)
