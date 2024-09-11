import numpy as np
import matplotlib.pyplot as plt

# Sigmoid activation function and its derivative
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# XOR input and output
inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
outputs = np.array([[0], [1], [1], [0]])

# Seed for reproducibility
np.random.seed(42)

# Initialize weights and biases
input_layer_neurons = 2
hidden_layer_neurons = 2
output_neurons = 1

# Weights and bias initialization
hidden_weights = np.random.uniform(size=(input_layer_neurons, hidden_layer_neurons))
hidden_bias = np.random.uniform(size=(1, hidden_layer_neurons))
output_weights = np.random.uniform(size=(hidden_layer_neurons, output_neurons))
output_bias = np.random.uniform(size=(1, output_neurons))

print("Initial Weights and Biases:")
print(f"Hidden Weights:\n{hidden_weights}")
print(f"Hidden Bias:\n{hidden_bias}")
print(f"Output Weights:\n{output_weights}")
print(f"Output Bias:\n{output_bias}\n")

# Learning rate
learning_rate = 1

# Training the network
epochs = 3

for epoch in range(epochs):
    # Forward propagation
    hidden_layer_input = np.dot(inputs, hidden_weights) + hidden_bias
    hidden_layer_activation = sigmoid(hidden_layer_input)

    output_layer_input = np.dot(hidden_layer_activation, output_weights) + output_bias
    predicted_output = sigmoid(output_layer_input)

    # Compute the loss
    error = outputs - predicted_output
    d_predicted_output = error * sigmoid_derivative(predicted_output)

    # Backpropagation
    error_hidden_layer = d_predicted_output.dot(output_weights.T)
    d_hidden_layer = error_hidden_layer * sigmoid_derivative(hidden_layer_activation)

    # Update weights and biases
    output_weights += hidden_layer_activation.T.dot(d_predicted_output) * learning_rate
    output_bias += np.sum(d_predicted_output, axis=0, keepdims=True) * learning_rate
    hidden_weights += inputs.T.dot(d_hidden_layer) * learning_rate
    hidden_bias += np.sum(d_hidden_layer, axis=0, keepdims=True) * learning_rate

    # Debugging output every 1000 epochs
    if epoch % 1000 == 0:
        loss = np.mean(np.square(outputs - predicted_output))
        print(f"Epoch {epoch}")
        print(f"Loss: {loss}")
        print(f"Hidden Weights:\n{hidden_weights}")
        print(f"Hidden Bias:\n{hidden_bias}")
        print(f"Output Weights:\n{output_weights}")
        print(f"Output Bias:\n{output_bias}")
        print(f"Predicted Output:\n{predicted_output}\n")

# Testing the network
print("Final Predicted Output:")
print(predicted_output)

# Binary classification result
binary_output = (predicted_output > 0.5).astype(int)
print("Final Binary Output:")
print(binary_output)

# Visualizing the network with weights and biases using matplotlib
def visualize_network(hidden_weights, hidden_bias, output_weights, output_bias):
    fig, ax = plt.subplots()

    # Nodes
    ax.text(0.1, 0.8, 'Input 1', fontsize=12, ha='center')
    ax.text(0.1, 0.5, 'Input 2', fontsize=12, ha='center')
    ax.text(0.5, 0.9, 'Hidden 1', fontsize=12, ha='center')
    ax.text(0.5, 0.35, 'Hidden 2', fontsize=12, ha='center')
    ax.text(0.9, 0.65, 'Output', fontsize=12, ha='center')

    # Weights and biases
    ax.text(0.2, 0.85, f'w1: {hidden_weights[0, 0]:.2f}', fontsize=8, ha='center')
    ax.text(0.15, 0.70, f'w2: {hidden_weights[0, 1]:.2f}', fontsize=8, ha='center')
    ax.text(0.15, 0.55, f'w3: {hidden_weights[1, 0]:.2f}', fontsize=8, ha='center')
    ax.text(0.2, 0.40, f'w4: {hidden_weights[1, 1]:.2f}', fontsize=8, ha='center')

    ax.text(0.75, 0.85, f'w5: {output_weights[0, 0]:.2f}', fontsize=8, ha='center')
    ax.text(0.75, 0.45, f'w6: {output_weights[1, 0]:.2f}', fontsize=8, ha='center')

    ax.text(0.5, 0.95, f'b1: {hidden_bias[0, 0]:.2f}', fontsize=8, ha='center')
    ax.text(0.5, 0.3, f'b2: {hidden_bias[0, 1]:.2f}', fontsize=8, ha='center')
    ax.text(0.9, 0.7, f'b3: {output_bias[0, 0]:.2f}', fontsize=8, ha='center')

    # Edges
    ax.arrow(0.17, 0.8, 0.2, 0.1, head_width=0.02, head_length=0.02, fc='k', ec='k')
    ax.arrow(0.17, 0.8, 0.2, -0.4, head_width=0.02, head_length=0.02, fc='k', ec='k')
    ax.arrow(0.17, 0.5, 0.2, 0.35, head_width=0.02, head_length=0.02, fc='k', ec='k')
    ax.arrow(0.17, 0.5, 0.2, -0.15, head_width=0.02, head_length=0.02, fc='k', ec='k')

    ax.arrow(0.6, 0.9, 0.2, -0.2, head_width=0.02, head_length=0.02, fc='k', ec='k')
    ax.arrow(0.6, 0.4, 0.2, 0.2, head_width=0.02, head_length=0.02, fc='k', ec='k')

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    plt.show()

# Visualize the network
visualize_network(hidden_weights, hidden_bias, output_weights, output_bias)
