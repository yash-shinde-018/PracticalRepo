import numpy as np
import pandas as pd
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Example synthetic weather dataset (replace with pd.read_csv)
data = {
    "temp": [30, 32, 31, 15, 16, 14, 28, 27, 29],
    "humidity": [70, 65, 68, 85, 87, 90, 66, 64, 67],
    "wind": [5, 7, 6, 12, 11, 13, 4, 6, 5]
}
df = pd.DataFrame(data)

X = StandardScaler().fit_transform(df.values)
Z = linkage(X, method='ward')  # single, complete, average, ward are common
plt.figure(figsize=(8, 4))
dendrogram(Z, labels=df.index.tolist(), leaf_rotation=90)
plt.title("Weather data dendrogram")
plt.tight_layout()
plt.show()

# choose clusters (e.g., 3)
clusters = fcluster(Z, t=3, criterion='maxclust')
df['cluster'] = clusters
print(df)
