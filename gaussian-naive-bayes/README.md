# About GNB

Gaussian Naive Bayes is a probabilistic machine learning algorithm used mainly for classification problems. It’s based on Bayes’ Theorem, which describes how to update the probability of a hypothesis when given new evidence.

- It’s called “Naïve” because it assumes that all features are independent of each other — an assumption that simplifies computation but often still works surprisingly well in real life.

- It’s called “Gaussian” because it assumes that the continuous features follow a Normal (Gaussian) distribution.

## Formula for Bayes' Theorem


## How it works?

1. Assume data features are independent e.g., In an email spam filter, “free” and “win” are treated as separate features.
2. Estimate the probability distribution for each feature using a Gaussian (Normal) curve. For each class, the model calculates:

3. Compute the posterior probability for each class.
4. Predict the class with the highest posterior probability.

## When to use?

- When your features are continuous and approximately follow a normal distribution.
- When you need a fast and efficient classifier that performs well with limited data.

## Advantages

- Simple and easy to implement.
- Works well even with small datasets.
- Requires very few parameters.
- Performs surprisingly well even when independence assumption is violated.

## Limitations

- Assumes all features are independent — which may not always be true.
- Performs poorly when feature correlations are strong.
- Sensitive to how well data fits the Gaussian distribution.

## Real-World Applications

- Email spam detection
- Sentiment analysis
- Document classification
- Medical diagnosis (e.g., disease prediction from symptoms)
- Weather prediction