# Learning QC, ML, QML

- QC - Quantum Computing
- ML - Machine Learning
- QML - Quantum Machine Learning

> Repo status: only QC - from basics to running VQE algorithm of $H_2$ with qiskit on the simulator.

Repo has a lot of unsuccessful try outs. This is the list that has fully functional code and is worth checking out:

1. [Basic circuit on hardware (my own code)](GENERAL/qiskit-tryouts/RUNNING_BASIC_CIRCUIT.ipynb)
2. [Qiskit tutorial 1](GENERAL/qiskit-tutorial/3-hello-tuto.ipynb)
3. [Qiskit tutorial 2](GENERAL/qiskit-tutorial/4-primitives.ipynb)
4. [Qiskit tutorial 3](GENERAL/qiskit-tutorial/5-dynamic-circuits.ipynb)
5. [VQE of H2 on simulator](VQE/7-qiskit-nature-example.ipynb)
6. IN_PROGRESS...

For setup install python libraries from [requirements.txt](requirements.txt):

```bash
pip install -r requirements.txt
```

Also you would need to have IBM account to run code on hardware. And then you would need to copy API key and using it setup the IBM Runtime Service. It is nicely explained in an official [qiskit tutorial](https://youtu.be/dZWz4Gs_BuI?si=1u-2p2-1tn3aW43S).

Not very ordered, but you can also find some notes on QC theory in [theory-cheatsheet directory](GENERAL/theory-cheatsheet/).

Some info can also be found in READMEs inside dirs.

More things coming soon...
