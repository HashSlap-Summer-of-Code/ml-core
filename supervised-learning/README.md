# About Supervised Learning

Supervised Learning is a type of machine learning where the model is trained on a labeled dataset, meaning each input has a corresponding known output.
The goal is for the model to learn the mapping function between inputs (features) and outputs (labels) so it can make predictions on unseen data.

## ⭐ Key Concepts

- **Labeled Data** – The training data consists of input-output pairs. For example, an image (input) labeled as “cat” (output).
- **Training Phase** – The algorithm learns by minimizing the difference between predicted and actual outputs using a loss function.
- **Testing / Validation Phase** – The trained model is evaluated on unseen data to measure its performance and generalization ability.
- **Regression** – Used when the output variable is continuous (e.g., predicting house prices).
- **Classification** – Used when the output variable is categorical (e.g., spam or not spam).
- **Overfitting / Underfitting** – Overfitting happens when the model learns noise instead of patterns; underfitting happens when it fails to learn enough.
- **Evaluation Metrics** – Common metrics include Accuracy, Precision, Recall, F1-Score, Mean Squared Error (MSE), and R² Score.

## ⭐ Workflow

         +-------------------+
         |   Input Data (X)  |
         +---------+---------+
                   |
                   |  with Labels (Y)
                   v
         +-------------------+
         |  Train Model (f)  |
         +---------+---------+
                   |
                   |  Learn mapping f(X) ≈ Y
                   v
         +-------------------+
         |  Trained Model    |
         +---------+---------+
                   |
                   |  New Data (X')
                   v
         +-------------------+
         | Predicted Output  |
         +-------------------+

## ⭐ Common Algorithms

- **Linear Regression** – Models the relationship between dependent and independent variables using a straight line.
- **Logistic Regression** – Used for binary classification problems.
- **Decision Trees** – Splits data into branches based on feature values for prediction.
- **Support Vector Machines (SVM)** – Finds the optimal boundary (hyperplane) that best separates data points of different classes.
- **k-Nearest Neighbors (KNN)** – Classifies data points based on the majority class of their nearest neighbors.
- **Naive Bayes** – A probabilistic classifier based on Bayes’ Theorem with independence assumptions.
- **Random Forest** – An ensemble of decision trees that improves performance and reduces overfitting.

## ⭐ Tools & Libraries

| Category         | Tools / Libraries                 |
| ---------------- | --------------------------------- |
| Core ML          | Scikit-learn, TensorFlow, PyTorch |
| Data Handling    | Pandas, NumPy                     |
| Visualization    | Matplotlib, Seaborn               |
| Model Evaluation | Scikit-learn Metrics, Yellowbrick |

## ⭐ Applications

- Email spam filtering
- Disease diagnosis from medical data
- Credit risk prediction
- Image and speech recognition
- Weather forecasting
- Sentiment analysis

## 🔗 Helpful Resources

- [Scikit-learn: Supervised Learning Overview](https://scikit-learn.org/stable/supervised_learning.html)  
- [Coursera: Supervised Machine Learning by Andrew Ng](https://www.coursera.org/learn/machine-learning)  
- [KDNuggets: Guide to Supervised Learning](https://www.kdnuggets.com/2020/06/supervised-learning-overview.html)  
- [Towards Data Science: Supervised vs Unsupervised Learning](https://towardsdatascience.com/supervised-vs-unsupervised-learning-14f68e32ea8d)  
- [Stanford CS229: Machine Learning Notes](http://cs229.stanford.edu/)
