# hits.py
import numpy as np

def hits(adj_matrix, max_iter=100, eps=1e-6):
    n = adj_matrix.shape[0]
    A = adj_matrix.copy().astype(float)
    auth = np.ones(n)
    hub = np.ones(n)
    for _ in range(max_iter):
        new_auth = A.T.dot(hub)
        new_hub = A.dot(new_auth)
        # normalize
        na = np.linalg.norm(new_auth)
        nh = np.linalg.norm(new_hub)
        if na==0 or nh==0:
            break
        new_auth /= na
        new_hub /= nh
        if np.linalg.norm(new_auth - auth) < eps and np.linalg.norm(new_hub - hub) < eps:
            auth, hub = new_auth, new_hub
            break
        auth, hub = new_auth, new_hub
    return auth, hub

if __name__ == "__main__":
    A = np.array([
        [0,1,1,0],
        [1,0,0,0],
        [1,0,0,1],
        [0,1,0,0]
    ])
    authority, hub = hits(A)
    print("Authority scores:", authority)
    print("Hub scores:", hub)
