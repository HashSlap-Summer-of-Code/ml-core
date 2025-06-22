# utils/experiment_logger.py

import csv
import os
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

def log_experiment(model_name, metrics, hyperparams, dataset_name, log_file="experiment_log.csv"):
    """
    Logs experiment results to a CSV file.
    
    :param model_name: str, name of the model (e.g., 'Perceptron')
    :param metrics: dict, e.g., {'accuracy': 0.92, 'loss': 0.08}
    :param hyperparams: dict, e.g., {'learning_rate': 0.01, 'epochs': 10}
    :param dataset_name: str, e.g., 'Iris'
    :param log_file: str, path to the CSV log file
    """
    filename = os.path.join(LOG_DIR, log_file)
    fieldnames = ['timestamp', 'model', 'dataset'] + list(hyperparams.keys()) + list(metrics.keys())

    row = {
        'timestamp': datetime.now().isoformat(),
        'model': model_name,
        'dataset': dataset_name,
        **hyperparams,
        **metrics
    }

    write_header = not os.path.isfile(filename)

    with open(filename, mode='a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if write_header:
            writer.writeheader()
        writer.writerow(row)


def plot_metrics(log_file="experiment_log.csv", metric='accuracy'):
    """
    Plots a lineplot for a selected metric from the log.
    
    :param log_file: str, path to the CSV log file
    :param metric: str, metric to plot (e.g., 'accuracy')
    """
    import pandas as pd
    path = os.path.join(LOG_DIR, log_file)
    if not os.path.exists(path):
        print("No logs found.")
        return

    df = pd.read_csv(path)
    if metric not in df.columns:
        print(f"Metric '{metric}' not found in logs.")
        return

    plt.figure(figsize=(10, 5))
    sns.lineplot(data=df, x='timestamp', y=metric, hue='model', marker='o')
    plt.title(f'{metric.title()} Over Time')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
