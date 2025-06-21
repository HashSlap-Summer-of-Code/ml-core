import numpy as np

class Perceptron:
    def __init__(self, input_size, learning_rate=0.1, epochs=10):
        self.weights = np.zeros(input_size + 1)  # +1 for bias
        self.lr = learning_rate
        self.epochs = epochs

    def predict(self, x):
        x = np.insert(x, 0, 1)  # Add bias term
        return 1 if np.dot(self.weights, x) > 0 else 0

    def train(self, X, y):
        for _ in range(self.epochs):
            for xi, target in zip(X, y):
                xi_bias = np.insert(xi, 0, 1)
                prediction = self.predict(xi)
                self.weights += self.lr * (target - prediction) * xi_bias

# Example usage
if __name__ == "__main__":
    # Linearly separable data
    X = np.array([[2, 3], [1, 1], [-1, -2], [-2, -4]])
    y = np.array([1, 1, 0, 0])

    model = Perceptron(input_size=2)
    model.train(X, y)

    # Test predictions
    for xi in X:
        print(f"Input: {xi}, Predicted: {model.predict(xi)}")
