#Define Euclidean Distance
import math

def euclidean_distance(point1, point2):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(point1, point2)))

#Define the KNN Classifier

class KNN:
    def __init__(self, k=3):
        self.k = k
        self.X_train = []
        self.y_train = []

    def fit(self, X, y):
        self.X_train = X
        self.y_train = y

    def predict(self, x):
        # Calculate distances
        distances = [(euclidean_distance(x, train_x), label) 
                     for train_x, label in zip(self.X_train, self.y_train)]
        distances.sort(key=lambda x: x[0])  # Sort by distance
        k_nearest_labels = [label for _, label in distances[:self.k]]
        
        # Majority vote
        return max(set(k_nearest_labels), key=k_nearest_labels.count)
    
#Test with Sample Dataset    

def main():
    # Sample training data (2D points with 3 classes)
    X_train = [[1, 2], [2, 3], [3, 1], [6, 5], [7, 7], [8, 6], [10, 2]]
    y_train = ['A', 'A', 'A', 'B', 'B', 'B', 'C']

    # Create classifier instance
    knn = KNN(k=3)
    knn.fit(X_train, y_train)

    # Sample test data
    test_point = [5, 5]
    prediction = knn.predict(test_point)
    print(f"Predicted class for point {test_point} is: {prediction}")
# K-Nearest Neighbors (KNN) Implementation

import math

# Step 1: Define Euclidean Distance
def euclidean_distance(point1, point2):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(point1, point2)))

# Step 2: Define KNN Class
class KNN:
    def __init__(self, k=3):
        self.k = k
        self.X_train = []
        self.y_train = []

    def fit(self, X, y):
        self.X_train = X
        self.y_train = y

    def predict(self, x):
        # Compute distances
        distances = [(euclidean_distance(x, train_x), label)
                     for train_x, label in zip(self.X_train, self.y_train)]
        distances.sort(key=lambda x: x[0])
        k_nearest_labels = [label for _, label in distances[:self.k]]
        return max(set(k_nearest_labels), key=k_nearest_labels.count)

# Step 3: Test the implementation
def main():
    # Sample dataset (3 classes, 2D points)
    X_train = [[1, 2], [2, 3], [3, 1], [6, 5], [7, 7], [8, 6], [10, 2]]
    y_train = ['A', 'A', 'A', 'B', 'B', 'B', 'C']

    test_point = [5, 5]

    knn = KNN(k=3)
    knn.fit(X_train, y_train)
    prediction = knn.predict(test_point)
    
    print(f"Predicted class for point {test_point}: {prediction}")

if __name__ == "__main__":
    main()
