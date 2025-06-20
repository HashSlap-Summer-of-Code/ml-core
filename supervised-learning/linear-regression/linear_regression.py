import numpy as np

# Define model
class Model():
    def __init__(self, n_features, n_samples):
        self.weights = np.zeros(n_features) # weights
        self.b = 0                          # bias
        self.learning_rate = 0.001          # learning rate for gradient descent
        self.n = n_samples                  # number of data points

    def predict(self, X):
        # Compute predictions y_pred = X*m + b
        return np.dot(X, self.weights) + self.b
    
    def mean_squared_error(self, y, y_pred):
        # Computer mean squared error loss
        # MSE = 1/2n * sum((y_true - y_pred)^2)
        return (1/ (2 * self.n)) * np.sum((y-y_pred) ** 2)
    
    def gradient_descent(self, X, y, y_pred):
        # Compute gradient of loss with respect to weights and bias
        error = y_pred - y

        # Compute partial derivatives with respect to weights and bias
        dm = (1/self.n) * np.dot(X.T, error)
        db = (1/self.n) * np.sum(error)

        return dm, db
    
    def update_parameters(self, dm, db):
        self.weights -= self.learning_rate * dm
        self.b -= self.learning_rate * db
    
    def train(self, X, y, epochs = 10000):
        for epoch in range(epochs):
            # Make prediction
            y_pred = self.predict(X)

            # Compute gradients
            dm, db = self.gradient_descent(X, y, y_pred)

            # Update model's parameters
            self.update_parameters(dm, db)

            # Print loss every 1000 epoch
            if epoch % 1000 == 0:
                loss = self.mean_squared_error(y, y_pred)
                print(f"Epoch {epoch}, Loss = {loss:0.5f}")
        

def main():
    # Seed so results don't change
    np.random.seed(42)

    # Create small dataset
    X = np.random.rand(10, 2)

    # Define true weights and biases
    true_m = np.array([3.5, -2.0])
    true_b = 4

    # Create target variable with a little noise
    y = np.dot(X, true_m) + true_b + np.random.randn(X.shape[0]) * 0.1

    # Initialize and train model
    model = Model(n_samples=X.shape[0], n_features=X.shape[1])
    model.train(X, y, epochs=10000)

    # Make prediction and calculate the MSE
    predictions = model.predict(X)
    mse = model.mean_squared_error(y, predictions)
    print(f"Final MSE: {mse:.5f}")


if __name__ == "__main__":
    main()