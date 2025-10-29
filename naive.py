import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix, accuracy_score

data = np.array([
    [45, 32, 5, 1, 1],  # Win = 1
    [10, 20, 1, 0, 0],  # Lose = 0
    [60, 48, 6, 2, 1],
    [15, 30, 1, 0, 0],
    [75, 55, 8, 3, 1],
    [25, 28, 2, 0, 0],
    [90, 60, 10, 4, 1],
    [30, 35, 3, 0, 0],
    [110, 70, 12, 5, 1],
    [5, 15, 0, 0, 0]
])

X = data[:, :-1]  # Features: Runs, Balls, Fours, Sixes
y = data[:, -1]   # Output: Win/Lose

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

model = GaussianNB()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

cm = confusion_matrix(y_test, y_pred)

print(f"Accuracy: {accuracy * 100:.2f}%\n")

print("Confusion Matrix:")
print(cm)
