import numpy as np

class GaussianNaiveBayes:
    def fit(self, X, y):
        self.classes = np.unique(y)
        self.means = {}
        self.vars = {}
        self.priors = {}

        for c in self.classes:
            X_c = X[y == c]
            self.means[c] = np.mean(X_c, axis=0)
            self.vars[c] = np.var(X_c, axis=0)
            self.priors[c] = X_c.shape[0] / X.shape[0]

    def predict(self, X):
        return np.array([self._predict_single(x) for x in X])

    def _predict_single(self, x):
        posteriors = []
        for c in self.classes:
            prior = np.log(self.priors[c])
            likelihood = np.sum(self._log_gaussian(x, self.means[c], self.vars[c]))
            posteriors.append(prior + likelihood)
        return self.classes[np.argmax(posteriors)]

    def _log_gaussian(self, x, mean, var):
        eps = 1e-9  # to avoid division by zero
        return -0.5 * np.log(2 * np.pi * var + eps) - ((x - mean) ** 2) / (2 * var + eps)



#Example:   Dataset: 2 classes, 2 features
X_train = np.array([
    [1.0, 2.0],
    [1.1, 1.9],
    [3.0, 3.5],
    [3.1, 3.7]
])
y_train = np.array([0, 0, 1, 1])

X_test = np.array([
    [1.2, 2.1],
    [3.2, 3.4]
])

model = GaussianNaiveBayes()
model.fit(X_train, y_train)
predictions = model.predict(X_test)

print("Predictions:", predictions)
