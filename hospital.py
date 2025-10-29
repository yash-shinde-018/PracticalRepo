# hierarchical_hospital.py
import pandas as pd
from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "hospital": ["H1","H2","H3","H4"],
    "num_beds":[100, 25, 300, 80],
    "avg_wait":[30, 45, 15, 25],  # minutes
    "satisfaction":[0.8, 0.6, 0.9, 0.75]
}).set_index("hospital")

X = StandardScaler().fit_transform(df)
Z = linkage(X, method='complete')
plt.figure(figsize=(6,4))
dendrogram(Z, labels=df.index.tolist())
plt.title("Hospital Clustering")
plt.show()

df['cluster'] = fcluster(Z, t=2, criterion='maxclust')
print(df)
