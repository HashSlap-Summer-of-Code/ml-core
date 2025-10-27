import json
import os
from datetime import datetime

import joblib
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

def train_and_save(version="v1"):
    X, y = load_iris(return_X_y=True)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    pipe = Pipeline([
        ("scaler", StandardScaler()),
        ("clf", LogisticRegression(max_iter=200))
    ])
    pipe.fit(X_train, y_train)

    preds = pipe.predict(X_test)
    report = classification_report(y_test, preds, output_dict=True)
    print("Evaluation report:", json.dumps(report, indent=2))

    model_dir = os.path.join("models", version)
    os.makedirs(model_dir, exist_ok=True)
    model_path = os.path.join(model_dir, "model.joblib")
    joblib.dump(pipe, model_path)

    metadata = {
        "version": version,
        "created_at": datetime.utcnow().isoformat() + "Z",
        "framework": "scikit-learn",
    }
    with open(os.path.join(model_dir, "metadata.json"), "w") as f:
        json.dump(metadata, f, indent=2)

    print(f"Saved model to {model_path}")
    return model_path

if __name__ == "__main__":
    train_and_save("v1")