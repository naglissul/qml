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

def train_network(learning_rate, epochs=10):
    # Initialize weights and biases
    hidden_weights = np.random.uniform(size=(2, 2))
    hidden_bias = np.random.uniform(size=(1, 2))
    output_weights = np.random.uniform(size=(2, 1))
    output_bias = np.random.uniform(size=(1, 1))
    
    losses = []
    hidden_weights_history = []
    hidden_bias_history = []
    output_weights_history = []
    output_bias_history = []
    
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
        
        # Store the weights and biases history
        hidden_weights_history.append(hidden_weights.copy())
        hidden_bias_history.append(hidden_bias.copy())
        output_weights_history.append(output_weights.copy())
        output_bias_history.append(output_bias.copy())
        
        # Debugging output every 1000 epochs
        if epoch % 1000 == 0:
            print(f"Learning Rate: {learning_rate}, Epoch {epoch}")
            print(f"Loss: {loss}")
            print(f"Hidden Weights:\n{hidden_weights}")
            print(f"Hidden Bias:\n{hidden_bias}")
            print(f"Output Weights:\n{output_weights}")
            print(f"Output Bias:\n{output_bias}\n")
    
    return losses, hidden_weights_history, hidden_bias_history, output_weights_history, output_bias_history

# Train the network
learning_rate = 0.1
losses, hidden_weights_history, hidden_bias_history, output_weights_history, output_bias_history = train_network(learning_rate)

# Combine the plots into one window
fig, axs = plt.subplots(5, 1, figsize=(10, 20))
plots = []

# Plot 1: Loss vs. Epochs
ax = axs[0]
loss_plot, = ax.plot(losses, label='Loss')
plots.append(loss_plot)
ax.set_xlabel('Epochs')
ax.set_ylabel('Loss')
ax.set_title('Loss vs. Epochs')
ax.legend()

# Prepare the data for weights and biases
hidden_weights_history = np.array(hidden_weights_history)
hidden_bias_history = np.array(hidden_bias_history)
output_weights_history = np.array(output_weights_history)
output_bias_history = np.array(output_bias_history).flatten()

# Plot 2: Hidden Weights vs. Epochs
ax = axs[1]
for i in range(hidden_weights_history.shape[1]):
    for j in range(hidden_weights_history.shape[2]):
        hidden_weight_plot, = ax.plot(hidden_weights_history[:, i, j], label=f'Hidden Weight {i+1}-{j+1}')
        plots.append(hidden_weight_plot)
ax.set_xlabel('Epochs')
ax.set_ylabel('Hidden Weights')
ax.legend()
ax.set_title('Hidden Weights vs. Epochs')

# Plot 3: Hidden Biases vs. Epochs
ax = axs[2]
for i in range(hidden_bias_history.shape[1]):
    hidden_bias_plot, = ax.plot(hidden_bias_history[:, 0, i], label=f'Hidden Bias {i+1}')
    plots.append(hidden_bias_plot)
ax.set_xlabel('Epochs')
ax.set_ylabel('Hidden Biases')
ax.legend()
ax.set_title('Hidden Biases vs. Epochs')

# Plot 4: Output Weights vs. Epochs
ax = axs[3]
for i in range(output_weights_history.shape[1]):
    for j in range(output_weights_history.shape[2]):
        output_weight_plot, = ax.plot(output_weights_history[:, i, j], label=f'Output Weight {i+1}-{j+1}')
        plots.append(output_weight_plot)
ax.set_xlabel('Epochs')
ax.set_ylabel('Output Weights')
ax.legend()
ax.set_title('Output Weights vs. Epochs')

# Plot 5: Output Bias vs. Epochs
ax = axs[4]
output_bias_plot, = ax.plot(output_bias_history, label='Output Bias')
plots.append(output_bias_plot)
ax.set_xlabel('Epochs')
ax.set_ylabel('Output Bias')
ax.legend()
ax.set_title('Output Bias vs. Epochs')

# Adjust layout to add more space between plots
plt.tight_layout()
plt.subplots_adjust(hspace=0.5)
plt.show()
