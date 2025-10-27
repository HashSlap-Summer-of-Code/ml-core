# About Neural Networks

Neural Networks are computational models inspired by the structure and functioning of the human brain. They consist of interconnected nodes, or "neurons," organized into layers that process information and learn to recognize patterns in data. Neural networks form the foundation of modern deep learning systems.

## ⭐️ Key Concepts

- **Neuron and Layers**

  Each neuron receives inputs, applies a transformation (usually a weighted sum followed by an activation function), and passes the result to the next layer. Layers are typically categorized as input, hidden, and output layers.
- **Activation Functions**

  Non-linear functions such as ReLU, Sigmoid, and Tanh that allow the network to model complex relationships.
- **Forward Propagation**

  The process of passing inputs through the network to produce an output.
- **Loss Function**

  A measure of the difference between the predicted output and the actual value. Common examples include Mean Squared Error and Cross-Entropy Loss.
- **Backpropagation**

  The algorithm that adjusts the weights of the network to minimize the loss using gradient descent.
- **Hyperparameters**

  Configuration parameters such as learning rate, batch size, and number of layers that affect model training and performance.

## ⭐️ Common Architectures

| Type                                   | Description                                                                 |
| -------------------------------------- | --------------------------------------------------------------------------- |
| **Feedforward Neural Network (FNN)**   | Basic network with information flowing from input to output without cycles. |
| **Convolutional Neural Network (CNN)** | Specializes in image and spatial data processing.                           |
| **Recurrent Neural Network (RNN)**     | Designed for sequential data such as text or time series.                   |
| **Long Short-Term Memory (LSTM)**      | A variant of RNN that handles long-term dependencies.                       |
| **Transformer**                        | State-of-the-art architecture for natural language and sequence modeling.   |

## ⭐️ Example: Simple Feedforward Neural Network (using PyTorch)

```python
import torch
import torch.nn as nn
import torch.optim as optim

# Define a simple neural network
class SimpleNN(nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.layer1 = nn.Linear(2, 4)
        self.relu = nn.ReLU()
        self.layer2 = nn.Linear(4, 1)
    
    def forward(self, x):
        return self.layer2(self.relu(self.layer1(x)))

# Example training step
model = SimpleNN()
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

x = torch.tensor([[1.0, 2.0]])
y = torch.tensor([[1.0]])

# Forward + Backward + Optimize
output = model(x)
loss = criterion(output, y)
loss.backward()
optimizer.step()

print("Output:", output.item())
```

Expected output

```
Output: 0.85   # (Approximate value depending on initialization)
```

This example shows how data flows through layers, loss is calculated, and gradients are updated during training.

## ⭐️ Applications

- Image and speech recognition
- Natural language understanding and translation
- Recommender systems
- Fraud detection and predictive analytics
- Game and autonomous system control

## 🔗 Helpful Resources

- [Deep Learning Book by Ian Goodfellow](https://www.deeplearningbook.org/)
- [PyTorch Tutorials](https://pytorch.org/tutorials/)
- [TensorFlow Guides](https://www.tensorflow.org/guide)
- [Stanford CS231n: Convolutional Neural Networks for Visual Recognition](http://cs231n.stanford.edu/)
- [Andrej Karpathy’s Neural Networks: A Visual Introduction](https://karpathy.ai/zero-to-hero.html)

