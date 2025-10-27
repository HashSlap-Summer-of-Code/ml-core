# About GNB

Gaussian Naive Bayes is a probabilistic machine learning algorithm used mainly for classification problems. It’s based on Bayes’ Theorem, which describes how to update the probability of a hypothesis when given new evidence.

- It’s called “Naïve” because it assumes that all features are independent of each other — an assumption that simplifies computation but often still works surprisingly well in real life.

- It’s called “Gaussian” because it assumes that the continuous features follow a Normal (Gaussian) distribution.

### Formula for Bayes' Theorem

<p align="center">
<img width="457" height="221" alt="Screenshot 2025-10-27 at 1 07 15 PM" src="https://github.com/user-attachments/assets/fb9404cb-8644-4d22-a857-49c8f4bdfde5" />
</p>

## ⭐️ How it works?

1. Assume data features are independent e.g., In an email spam filter, “free” and “win” are treated as separate features.
2. Estimate the probability distribution for each feature using a Gaussian (Normal) curve. For each class, the model calculates:
  
  <p align="center">
  <img width="425" height="386" alt="normal-distribution-formula" src="https://github.com/user-attachments/assets/d4d6748c-6e71-4784-a615-5b4e5dbedab5" />
  </p>
  
3. Compute the posterior probability for each class.
4. Predict the class with the highest posterior probability.

## ⭐️ When to use?

- When your features are continuous and approximately follow a normal distribution.
- When you need a fast and efficient classifier that performs well with limited data.

## ⭐️ Advantages

- Simple and easy to implement.
- Works well even with small datasets.
- Requires very few parameters.
- Performs surprisingly well even when independence assumption is violated.

## 📌 Limitations

- Assumes all features are independent — which may not always be true.
- Performs poorly when feature correlations are strong.
- Sensitive to how well data fits the Gaussian distribution.

## ⭐️ Real-World Applications

- Email spam detection
- Sentiment analysis
- Document classification
- Medical diagnosis (e.g., disease prediction from symptoms)
- Weather prediction
