import numpy as np
import matplotlib.pyplot as plt

# Sample 2D dataset: 10 points
X = np.array([
    [1, 2], [1.5, 1.8], [5, 8],
    [8, 8], [1, 0.6], [9, 11],
    [8, 2], [10, 2], [9, 3], [6, 4]
])

class KMeans:
    def __init__(self, k=3, max_iters=100):
        self.k = k
        self.max_iters = max_iters

    def fit(self, data):
        # Initialize centroids randomly from data points
        np.random.seed(42)
        indices = np.random.choice(len(data), self.k, replace=False)
        self.centroids = data[indices]

        for _ in range(self.max_iters):
            # Assign clusters
            self.labels = self._assign_clusters(data)
            # Recompute centroids
            new_centroids = np.array([
                data[self.labels == i].mean(axis=0) for i in range(self.k)
            ])
            # Check for convergence
            if np.all(new_centroids == self.centroids):
                break
            self.centroids = new_centroids

    def _assign_clusters(self, data):
        distances = np.linalg.norm(data[:, np.newaxis] - self.centroids, axis=2)
        return np.argmin(distances, axis=1)

    def predict(self, data):
        return self._assign_clusters(data)

# Run model
kmeans = KMeans(k=3)
kmeans.fit(X)
labels = kmeans.predict(X)

# Plot results
colors = ['r', 'g', 'b']
for i in range(3):
    points = X[labels == i]
    plt.scatter(points[:, 0], points[:, 1], s=50, c=colors[i], label=f'Cluster {i+1}')
plt.scatter(kmeans.centroids[:, 0], kmeans.centroids[:, 1], s=200, marker='X', c='black', label='Centroids')
plt.legend()
plt.title("K-Means Clustering (k=3)")
plt.show()
