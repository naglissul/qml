from qiskit import QuantumCircuit
from qiskit.visualization import circuit_drawer

# Create a quantum circuit with 2 qubits
qc = QuantumCircuit(2)

# Apply Hadamard gate to the first qubit
qc.h(0)

# Apply CNOT gate (control=qubit 0, target=qubit 1)
qc.cx(0, 1)

# Print the quantum circuit as text
print(qc.draw(output='text'))
