
# ml-core

<p align="center">
  <img src="https://img.shields.io/github/license/HashSlap-Summer-of-Code/ml-core?style=flat-square&color=brightgreen" />
  <img src="https://img.shields.io/github/forks/HashSlap-Summer-of-Code/ml-core?style=flat-square&color=gray" />
  <img src="https://img.shields.io/github/stars/HashSlap-Summer-of-Code/ml-core?style=flat-square&color=blue" />
  <img src="https://img.shields.io/github/issues/HashSlap-Summer-of-Code/ml-core?style=flat-square&color=green" />
  <img src="https://img.shields.io/github/issues-pr/HashSlap-Summer-of-Code/ml-core?style=flat-square&color=gold" />
</p>

---

## About

> **ml-core** is an open-source repository under the **HashSlap Summer of Code** initiative, dedicated to implementing core Machine Learning projects across various domains. It's beginner-friendly, contribution-ready, and built entirely in Python.

---

## ⭐️ Project Structure

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

## Preview to Sections:
- [Computer Vision](https://github.com/muskansngh07/ml-core-hacktoberfest/blob/created-readme-for-different-domains/computer-vision/README.md)
- [NLP](https://github.com/muskansngh07/ml-core-hacktoberfest/tree/created-readme-for-different-domains/natural-language-processing#readme)
- [Supervised Learning](https://github.com/muskansngh07/ml-core-hacktoberfest/tree/created-readme-for-different-domains/supervised-learning#readme)
- [Unsupervised Learning](https://github.com/muskansngh07/ml-core-hacktoberfest/tree/created-readme-for-different-domains/unsupervised-learning#readme)
- [Reinforcement Learning](https://github.com/muskansngh07/ml-core-hacktoberfest/tree/created-readme-for-different-domains/reinforcement-learning#readme)
- [Neural Networks](https://github.com/muskansngh07/ml-core-hacktoberfest/tree/created-readme-for-different-domains/neural-networks#readme)
- [Data Analysis](https://github.com/muskansngh07/ml-core-hacktoberfest/tree/created-readme-for-different-domains/data-analysis#readme)

---

## ⭐️ How to Contribute

We welcome **first-time contributors** and experienced ML practitioners alike!

###  Steps to Contribute

- Fork the repository - Click the **Fork** button at the top-right corner of this repository to create your own copy.

- Pick an Issue or Propose Your Own Project - Check the Issues tab or open a new issue describing your idea or improvement.

- Clone the repository
 
  ```bash
  git clone https://github.com/<your-username>/<repo-name>.git
  cd <repo-name>
  ```

- Create a new branch
  ```bash
  git checkout -b <your-branch-name>
  ```

- Create your project in the relevant domain folder.

  ```bash
  mkdir <domain>/<your_project_name>
  ```

- Add your code + README
- Stage and Commit your changes.
  ```bash
  git add .
  git commit -m "Added my project on <topic>"
  ```

- Push to your created branch
  ```bash
  git push origin <your-branch-name>
  ```
- Submit a Pull Request (PR)

  Go to your forked repository on GitHub → Click on Compare & pull request → Describe your changes clearly → Submit!

    📌 Tip: Before pushing, always pull the latest changes to avoid merge conflicts:

    ```bash
    git pull origin main --rebase
    ```

> Contributions will be reviewed and merged by mentors.

---

## ⭐️ Experiment Logger

Located at: `utils/experiment_logger.py`

### ☆ Features

- Logs training results (accuracy, loss, hyperparameters, etc.) to CSV
- Supports multiple experiments for comparison
- Visualize performance trends using matplotlib/seaborn

### ☆ Requirements

```bash
pip install matplotlib seaborn pandas
```

###  ☆ How to Use

from utils.experiment_logger import log_experiment, plot_metrics

###  ☆ Log an experiment
log_experiment(
    model_name='Perceptron',
    metrics={'accuracy': 0.9, 'loss': 0.12},
    hyperparams={'learning_rate': 0.01, 'epochs': 20},
    dataset_name='Iris'
)

### ☆ Plot results
plot_metrics(metric='accuracy')

### ☆ Integration
Just import and call log_experiment(...) at the end of your model training script. It works across all subdomains like supervised-learning/, deep-learning/, etc.


## ⭐️ Why Contribute?

- Build real ML projects
- Deepen conceptual knowledge
- Boost your GitHub profile
- Get featured in contributor spotlights
- Earn participation certificates and digital badges

---
## ⭐️ Templates

### ☆ ML Pipeline Template

A reusable and beginner-friendly Python script that demonstrates a typical Machine Learning pipeline.  
Supports CLI usage with [`argparse`](https://docs.python.org/3/library/argparse.html) for flexible input and automation.

📂 Location: `templates/ml_pipeline_template.py`

#### ☆☆ Features:
- Load data from CSV/JSON
- Preprocess and split into train/test
- Train a simple ML model (e.g., Logistic Regression)
- Evaluate performance
- Easily adaptable for your own datasets

#### ☆☆ How to Run:

python templates/ml_pipeline_template.py --data iris.csv --target species


## 📜 License

This repository is licensed under the [MIT License](LICENSE).

---

