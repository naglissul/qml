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

def train_network(learning_rate, epochs=10000):
    # Initialize weights and biases
    hidden_weights = np.random.uniform(size=(2, 2))
    hidden_bias = np.random.uniform(size=(1, 2))
    output_weights = np.random.uniform(size=(2, 1))
    output_bias = np.random.uniform(size=(1, 1))
    
    losses = []
    
    for epoch in range(epochs):
        # Forward propagation
        hidden_layer_input = np.dot(inputs, hidden_weights) + hidden_bias
        hidden_layer_activation = sigmoid(hidden_layer_input)
        
        output_layer_input = np.dot(hidden_layer_activation, output_weights) + output_bias
        predicted_output = sigmoid(output_layer_input)
        
        # Compute the loss
        error = outputs - predicted_output
        loss = np.mean(np.square(error))
        losses.append(loss)
        
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
            print(f"Learning Rate: {learning_rate}, Epoch {epoch}")
            print(f"Loss: {loss}")
            print(f"Hidden Weights:\n{hidden_weights}")
            print(f"Hidden Bias:\n{hidden_bias}")
            print(f"Output Weights:\n{output_weights}")
            print(f"Output Bias:\n{output_bias}\n")
    
    return losses

# Train networks with different learning rates
learning_rate_moderate = 0.1
learning_rate_high = 1.0

print("Training with moderate learning rate (0.1):")
losses_moderate = train_network(learning_rate_moderate)

print("\nTraining with high learning rate (1.0):")
losses_high = train_network(learning_rate_high)

# Plotting the losses
import matplotlib.pyplot as plt

plt.plot(losses_moderate, label='Learning Rate = 0.1')
plt.plot(losses_high, label='Learning Rate = 1.0')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.title('Loss vs. Epochs for Different Learning Rates')
plt.show()
