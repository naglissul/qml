# Scientific paper list about VQE et similaire

[A variational eigenvalue solver on a quantum processor (2013)](https://arxiv.org/pdf/1304.3061)

---

https://qiskit-community.github.io/qiskit-algorithms/stubs/qiskit_algorithms.VQE.html

Qiskit built-in VQE tools.

---

[Quantum chemistry](https://chemistry.com.pk/books/quantum-chemistry-2e-mcquarrie/)

What are those ground states... And general about quantum chemistry.

---

[MoG-VQE: Multiobjective genetic variational quantum eigensolver (2020)](https://arxiv.org/pdf/2007.04424)

Choosing ansatz. Example with $H_2$, $H_4$, $H_6$, $BeH_2$ and most importantly, $LiH$.

A circuit to build $LiH$ ground state.

---

[Demonstration of small programmable quantum computer with atomic qubits](https://arxiv.org/pdf/1603.04512)

The first programmable q-computer of 5 qubits, implementation of Deutsch-Joshua algorithm.

---

https://arxiv.org/pdf/2305.06538

Basic paper with intro to QC and VQE, but very little talking about the actual algorithm, just using built-in tools.

---

https://arxiv.org/pdf/2111.05176

The Variational Quantum Eigensolver: a review of methods and
best practices (2022)

Quite extensive.

## Papers from tutorials and other files in this repo

[Evidence for the utility of quantum computing before fault tolerance (2023)](https://www.nature.com/articles/s41586-023-06096-3)

From qiskit tutorial. This goes through TRANSVERSE FIELD ISING MODEL of quantum computing.

## REMEMBER THESE (read again)

(1)
[Ising model from qiskit tutorial](https://www.nature.com/articles/s41586-023-06096-3)

(2)
[Paper explaining basics and how hamiltonian is found](https://arxiv.org/pdf/2305.06538)

## More papers on trying to set the thesis scope

[Algorithm 778: L-BFGS-B: Fortran subroutines for large-scale bound-constrained optimization](https://dl.acm.org/doi/10.1145/279232.279236)

Mentioned in qiskit VQE built-in implementation:

[A variational eigenvalue solver on a quantum processor (2013)](https://arxiv.org/abs/1304.3061)

[(H2 ground state) The Two Electron Molecular Bond Revisited: From Bohr Orbits to Two-Center Orbitals. Advances In Atomic, Molecular, and Optical Physics. (2005) ](https://www.researchgate.net/figure/Ground-state-ER-of-H2-molecule-calculated-by-the-self-consistent-Hartree-Fock-method_fig10_222707765)

[Finding Ground State Energy of Molecules with Variational Quantum Eigensolver(2019)](https://cs269q.stanford.edu/projects2019/KangLeeVQE_Y.pdf) // H2, LiH, BeH2

[Exploring the scaling limitations of the variational quantum eigensolver with the bond dissociation of hydride diatomic molecules](https://onlinelibrary.wiley.com/doi/10.1002/qua.27097) // Limitations with TiH and other hydrates

## Random VQE papers from VU library eLABa

[Local, expressive, quantum-number-preserving VQE ansätze for fermionic systems](https://iopscience.iop.org/article/10.1088/1367-2630/ac2cb3/pdf)

[Bakis: Applications of quantum computing to molecular analysis in chemistry](https://talpykla.elaba.lt/elaba-fedora/objects/elaba:210648145/datastreams/MAIN/content)

# Have read through

[Finding Ground State Energy of Molecules with Variational Quantum Eigensolver (2019)](https://cs269q.stanford.edu/projects2019/KangLeeVQE_Y.pdf)

Not a real paper, just a project of students.

Evaluates:

- Speed - number of quantum gates
- Accuracy - calculated $E_0$ compared with actual $E_0$ from Schrodinger equation (classically)
