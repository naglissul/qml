# Dockerfile
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /scripts

# Copy the current directory contents into the container at /scripts
COPY scripts /scripts

# Install numpy and matplotlib
RUN pip install numpy qiskit qiskit-ibm-runtime qiskit[visualization] qiskit-aer pylatexenc
RUN pip install matplotlib spectral

# Set the command to open a terminal
CMD ["bash"]
