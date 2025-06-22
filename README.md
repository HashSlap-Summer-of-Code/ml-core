
# 🧠 ml-core

<p align="center">
  <img src="https://img.shields.io/github/license/HashSlap-Summer-of-Code/ml-core?style=flat-square&color=brightgreen" />
  <img src="https://img.shields.io/github/forks/HashSlap-Summer-of-Code/ml-core?style=flat-square&color=gray" />
  <img src="https://img.shields.io/github/stars/HashSlap-Summer-of-Code/ml-core?style=flat-square&color=blue" />
  <img src="https://img.shields.io/github/issues/HashSlap-Summer-of-Code/ml-core?style=flat-square&color=green" />
  <img src="https://img.shields.io/github/issues-pr/HashSlap-Summer-of-Code/ml-core?style=flat-square&color=gold" />
</p>

---

## 📌 About

> **ml-core** is an open-source repository under the **HashSlap Summer of Code** initiative, dedicated to implementing core Machine Learning projects across various domains. It's beginner-friendly, contribution-ready, and built entirely in Python.

---

## 📁 Project Structure

Each folder in this repository represents a subdomain of machine learning. Contributors can choose issues or create projects under:

```
ml-core/
├── computer-vision/
├── natural-language-processing/
├── supervised-learning/
├── unsupervised-learning/
├── deep-learning/
├── time-series/
├── generative-models/
└── reinforcement-learning/
```

Each project should include:

* Well-structured code
* A `README.md` explaining the approach
* Sample results/outputs

---

## 🚀 How to Contribute

We welcome **first-time contributors** and experienced ML practitioners alike!

### 📦 Steps:

1. Fork the repository 🍴
2. Pick an issue or propose your own project
3. Create a folder inside the relevant domain
4. Add code + README
5. Submit a Pull Request ✅

Contributions will be reviewed and merged by mentors.

---

## 📊 Experiment Logger

Located at: `utils/experiment_logger.py`

### ✅ Features

- Logs training results (accuracy, loss, hyperparameters, etc.) to CSV
- Supports multiple experiments for comparison
- Visualize performance trends using matplotlib/seaborn

### 📦 Requirements

```bash
pip install matplotlib seaborn pandas


###  🚀 How to Use

from utils.experiment_logger import log_experiment, plot_metrics

###  Log an experiment
log_experiment(
    model_name='Perceptron',
    metrics={'accuracy': 0.9, 'loss': 0.12},
    hyperparams={'learning_rate': 0.01, 'epochs': 20},
    dataset_name='Iris'
)

### Plot results
plot_metrics(metric='accuracy')

### 🔁 Integration
Just import and call log_experiment(...) at the end of your model training script. It works across all subdomains like supervised-learning/, deep-learning/, etc.



## 🔥 Why Contribute?

* 🎓 Build real ML projects
* 🧠 Deepen conceptual knowledge
* 📈 Boost your GitHub profile
* 📢 Get featured in contributor spotlights
* 🏷️ Earn participation certificates and digital badges

---

## 📜 License

This repository is licensed under the [MIT License](LICENSE).

---

