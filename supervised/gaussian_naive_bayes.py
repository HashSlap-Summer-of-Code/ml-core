# Gaussian Naive Bayes Classifier - Basic Example

import numpy as np

class GaussianNaiveBayes:
    def fit(self, X, y):
        self.classes = np.unique(y)
        self.mean = {}
        self.var = {}
        self.priors = {}

        for c in self.classes:
            X_c = X[y == c]
            self.mean[c] = X_c.mean(axis=0)
            self.var[c] = X_c.var(axis=0)
            self.priors[c] = X_c.shape[0] / X.shape[0]

    def gaussian_density(self, class_idx, x):
        mean = self.mean[class_idx]
        var = self.var[class_idx]
        numerator = np.exp(- (x - mean) ** 2 / (2 * var))
        denominator = np.sqrt(2 * np.pi * var)
        return numerator / denominator

    def predict(self, X):
        return np.array([self._predict(x) for x in X])

    def _predict(self, x):
        posteriors = []
        for c in self.classes:
            prior = np.log(self.priors[c])
            conditional = np.sum(np.log(self.gaussian_density(c, x)))
            posteriors.append(prior + conditional)
        return self.classes[np.argmax(posteriors)]

# Sample run
if __name__ == "__main__":
    X = np.array([
        [1.0, 2.1],
        [1.2, 1.9],
        [0.8, 2.0],
        [3.0, 3.1],
        [3.2, 2.9],
        [2.8, 3.0],
    ])
    y = np.array([0, 0, 0, 1, 1, 1])
    
    model = GaussianNaiveBayes()
    model.fit(X, y)
    
    X_test = np.array([[1.1, 2.0], [3.1, 3.0]])
    predictions = model.predict(X_test)
    
    print("Predictions:", predictions)
