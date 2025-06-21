# ml_pipeline_template.py




import argparse
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

def load_data(file_path):
    """
    Loads a CSV file into a Pandas DataFrame.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def preprocess_data(data, target_column):
    """
    Splits the data into train/test sets and scales the features.
    """
    X = data.drop(columns=[target_column])
    y = data[target_column]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    return X_train_scaled, X_test_scaled, y_train, y_test

def train_model(X_train, y_train):
    """
    Trains a logistic regression model.
    """
    model = LogisticRegression()
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    """
    Evaluates the model on the test set.
    """
    predictions = model.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, predictions))
    print("Classification Report:\n", classification_report(y_test, predictions))

def main(args):
    data = load_data(args.data)
    if data is not None:
        X_train, X_test, y_train, y_test = preprocess_data(data, args.target)
        model = train_model(X_train, y_train)
        evaluate_model(model, X_test, y_test)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Reusable ML Pipeline Template")
    parser.add_argument('--data', type=str, required=True, help="Path to the CSV file")
    parser.add_argument('--target', type=str, required=True, help="Target column name")

    args = parser.parse_args()
    main(args)
