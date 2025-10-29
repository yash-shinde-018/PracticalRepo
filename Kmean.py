import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Generate sample college data: SAT Scores & GPA
np.random.seed(42)
sat_scores = np.random.normal(1200, 150, 100).astype(int)   # SAT Score
gpa_values = np.random.normal(3.0, 0.4, 100)                 # GPA values

# Combine into dataset
data = np.column_stack((sat_scores, gpa_values))

# Apply K-Means
k = 3
kmeans = KMeans(n_clusters=k, random_state=42)
clusters = kmeans.fit_predict(data)

# Plotting Graph
plt.figure(figsize=(10, 6))
colors = ['purple', 'teal', 'gold']

for cluster_idx in range(k):
    cluster_data = data[clusters == cluster_idx]
    plt.scatter(cluster_data[:, 0], cluster_data[:, 1], 
                s=50, c=colors[cluster_idx], label=f"Cluster {cluster_idx}")

# Decorate graph
plt.title("Clustering of Colleges based on SAT Score and GPA")
plt.xlabel("SAT Score")
plt.ylabel("GPA")
plt.legend(title="Cluster")
plt.show()
