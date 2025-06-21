import numpy as np
import matplotlib.pyplot as plt

class KMeans:
    def __init__(self, k=3, max_iters=100, tolerance=1e-4, random_state=42):
        self.k = k
        self.max_iters = max_iters
        self.tolerance = tolerance
        self.random_state = random_state

    def fit(self, data):
        np.random.seed(self.random_state)
        # Initialize centroids randomly from the data
        indices = np.random.choice(len(data), self.k, replace=False)
        self.centroids = data[indices]

        for i in range(self.max_iters):
            # Assign each point to the nearest centroid
            self.labels = self._assign_clusters(data)

            # Calculate new centroids
            new_centroids = np.array([
                data[self.labels == j].mean(axis=0) for j in range(self.k)
            ])

            # Check if centroids have converged
            if np.linalg.norm(self.centroids - new_centroids) < self.tolerance:
                break

            self.centroids = new_centroids

    def _assign_clusters(self, data):
        # Compute Euclidean distance from each point to each centroid
        distances = np.linalg.norm(data[:, np.newaxis] - self.centroids, axis=2)
        return np.argmin(distances, axis=1)

    def predict(self, data):
        return self._assign_clusters(data)

    def plot(self, data):
        colors = ['red', 'green', 'blue', 'purple', 'orange']
        for i in range(self.k):
            points = data[self.labels == i]
            plt.scatter(points[:, 0], points[:, 1], c=colors[i % len(colors)], label=f'Cluster {i+1}')
        plt.scatter(self.centroids[:, 0], self.centroids[:, 1], c='black', marker='X', s=200, label='Centroids')
        plt.title(f'K-Means Clustering (k={self.k})')
        plt.legend()
        plt.grid(True)
        plt.show()


if __name__ == "__main__":
    # Example 2D dataset with 3 clusters
    np.random.seed(42)
    data = np.vstack((
        np.random.randn(4, 2) + [5, 5],
        np.random.randn(3, 2) + [0, 0],
        np.random.randn(3, 2) + [-5, 5]
    ))

    model = KMeans(k=3)
    model.fit(data)
    model.plot(data)
