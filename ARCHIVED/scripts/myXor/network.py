import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)  # Seed for reproducibility


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def cost(y_true: float, y_pred: float):
    return (y_true - y_pred) ** 2 / 2


class Neuron:
    def __init__(self, weights: np.ndarray, bias: float):
        self.weights = weights  # Input weights
        self.bias = bias  # For this network biases are not used

    def forward(self, inputs):
        return np.dot(inputs, self.weights) + self.bias


# The XOR input and output
learning_data = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
target_data = np.array([[0], [1], [1], [0]])

# Network with initializations
layers = [2, 3, 1]  # First layer is not neurons, but input data
network = [
    [
        Neuron(weights=np.random.uniform(size=layers[i]), bias=0)
        for _ in range(layers[i])
    ]
    for i in range(len(layers) - 1)
]

print("Initial Weights and Biases:")
for i, layer in enumerate(network):
    print(f"Layer {i + 2}:")
    for neuron in layer:
        print(neuron.weights)
        print(neuron.bias)
    print()
