# XOR learner

import numpy as np

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

# Learning rate
learning_rate = 0.1

# Training the network
epochs = 10000
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
