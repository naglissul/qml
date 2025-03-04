# Bachelor thesis plan

Thesis topic: "Variational quantum eigensolver algorithm performance analysis on various molecules"

> What should be constant and what should be investigated as a variable? Read papers, what doesn't have an effect. Or maybe even just take one.

> What should be the EVALUATORS for evaluating efficiency? Time? Theoretical time? Accuracy? Circuit depth? Decoherence?

Molecules: $H_2$, $LiH$, $He$, $BeH_2$ ...?

Ansatze: UCCSD and it's modifications, Hardware specific (and that's it???)

Optimizers: L_BFGS_B and other ???

Environment: AER simulator, IBM quantum hardware (brisbane and other???), ???; qiskit, other???

Second quantization mappers (fermionic operators): Parity, Jordan-Wigner, Bravyi-Kitaev.

---

Basically my aim is to analyze all the posibilities to run VQE algo and then compare different molecules with different vqe methods on different devices.

Outcome would be a table: columns - running environment; rows - molecules x theory; cells - theoretical (complexity) and practical (speedup) comparison.

1. Analyze theory, from theoretical side what are the best optimizers, ansatze etc. Parallelizing classical stuff (?)
2. Analyze practise, what are the free computer options, what are actual speedups, accuracy, draw graphs (both classical computer, maybe parallelize, and q-computer).
3. Two tables:

- One testing BEST theoretical analysis outcomes on different devices.
- Another few testing the theoretical analysis outcomes if they are correct on one/afew computers, measuring speedups and seeing how they align with the theory.

For analysis/comparison: theoretical complexities; speedup, circuit depth, accuracy.
