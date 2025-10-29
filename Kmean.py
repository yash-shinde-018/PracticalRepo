import numpy as np

n = int(input("Enter number of points: "))
points = []

print("Enter each point as two numbers (x y):")
for _ in range(n):
    x, y = map(float, input().split())
    points.append([x, y])

points = np.array(points)

k = int(input("Enter number of clusters: "))

centroids = points[:k].astype(float)

labels = np.zeros(n, dtype=int)
prev_labels = np.full(n, -1)


while True:
    for i in range(n):
        dists = np.sum((points[i] - centroids)**2, axis=1)
        labels[i] = np.argmin(dists)

    if np.array_equal(labels, prev_labels):
        break

    prev_labels = labels.copy()

    for c in range(k):
        cluster_points = points[labels == c]
        if len(cluster_points) > 0:
            centroids[c] = cluster_points.mean(axis=0)

clusters = [[] for _ in range(k)]
for i in range(n):
    clusters[labels[i]].append(points[i])

print("\nFinal centroids:")
for c in range(k):
    print(f"Centroid {c+1}: ({centroids[c][0]:.3f}, {centroids[c][1]:.3f})")

print("\nCluster memberships:")
for c in range(k):
    print(f"Cluster {c+1}:")
    for pt in clusters[c]:
        print(f" ({pt[0]:.2f}, {pt[1]:.2f})")
