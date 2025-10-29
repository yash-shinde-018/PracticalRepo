# hierarchical_college.py
import pandas as pd
from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster
import matplotlib.pyplot as plt

# sample college data (replace with CSV read)
df = pd.DataFrame({
    "college": ["A","B","C","D","E"],
    "avg_marks":[78, 85, 60, 72, 88],
    "placement_rate":[0.7, 0.9, 0.4, 0.6, 0.95],
    "faculty_student":[1/20, 1/15, 1/40, 1/30, 1/12]
}).set_index("college")

X = StandardScaler().fit_transform(df)
Z = linkage(X, method='average')
plt.figure(figsize=(7,4))
dendrogram(Z, labels=df.index.tolist())
plt.title("College Hierarchical Clustering")
plt.show()

df['cluster'] = fcluster(Z, t=2, criterion='maxclust')
print(df)