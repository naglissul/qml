# Bachelor thesis

VQE algorithm performance analysis on various molecules

- [Paper in progress, official plan](https://www.overleaf.com/read/zpvkyxyfzpmn#c1c979)
- [Running basic case of QC on simulator & hardware, estimator & sampler](./../GENERAL/qiskit-tryouts/RUNNING_BASIC_CIRCUIT.ipynb)
- [Running VQE on simulator & hardware](./R!-run-on-q-hardware/R1-run-on-q-hardware.ipynb), the latter has problems, documented [here](./R!-run-on-q-hardware/Failing_vqe_case.ipynb)

## Plan

Official plan (far from reality):

- (21 March 2025) Conduct literature analysis on the whole VQE algorithm process and variations, finding recommendations on what ansätze, classical optimizer, second quantization methods.
- (4 April 2025) Conduct literature analysis, determining which molecules, how and on what quantum and classical hardware can be tested. What is the performance of VQE on different molecule data input, as of today, what are the perceived possibilities on implementing this algorithm in computational chemistry, what are the limitations.
- (18 April 2025) Test theoretical literature analysis outcome on quantum hardware, comparing the results.
- (2 May 2025) Conduct empirical experiment with selected molecule data on selected devices.
- (16 May 2025) Performing analysis on empirical data, yielding conclusions on current possibilities and limitations.

Official deadlines:

- **2025-05-23 10:00 Hand in**

Actual plan:

1. In parallel:

- run VQE algorithm on IBMQ hardware (and other devices)
- write introduction (briefly read and familiarize with a lot of articles; list experiments and metrics, possibly will change)

2. In parallel:

- Read in detail literature analysis (and possibly change list of experiments and metrics)
- Write methodology
- Do experiments

3. Finalize...

## Ideas

04-23

[Qedma QESEM](https://docs.quantum.ibm.com/guides/qedma-qesem) might be interesting to use for VQE...

Should make HEA for hardware, not just straight theoretical UCCSD or similar...

Only for simulators (?) use UCCSD and other ansatzes...

Should try ADAPT-VQE, because a lot of literature mentions it...

Show calculations for Hamiltonian (mapping, integrals, Schrodinger equation) or out of scope?

Ansatzes form papers (for hardware) then... Reduce qubits. Why not running basic? For simulator it is ok with basic ansatzes (UCCSD and other)

[List of papers read...](./PAPER_LIST.md)

## Variables\*

1. Atomic distance. Calculate ground state energies with different atomic distances:

![alt text](image.png)

https://www.nature.com/articles/nature23879

2. Molecule. Separate graph for each molecule. [This paper](https://link.springer.com/article/10.1007/s00339-020-03755-4) list: CO, HCl, F $_2$ , NH $_4^+$ , CH $_4$, NH $_{3}$, H $_3O^+$ , H ${_2}$, BeH $_{2}$, LiH, OH $^-$, HF, HeH $^+$, H $_2$

3. Ansatz. UCCSD and it's improvements, Special from papers, also ADAPT-VQE. Papildomi laisvieji kintamieji

4. Hamiltonian. Method used to generate: Mapper (Parity, Jordan-Wigner, Braev-Kitaev) and qubit reduction (only for Parity?)

5. (Shot count)

## Metrics (comparison and benchmarks)

1. Runtime/speedup: quantum and classical separately, disregard job scheduling delay (or maybe not, and include the importance of communication complexity). For simulator also separate classical from pseudo-quantum. Is there a quantum advantage?

2. Accuracy. Value absolute error, Value relative error, State fidelity. From schrodinger equation classical solution, or/and other papers.

3. Circuit depth

4. Number of qubits

5. Number of parameters

6. Number of iterations/oracle calls (until convergence - find what is a proper/default required gradient norm/change in function value/change in param value)

7. Speed of convergence (maybe there are other ways to determine if coinvergence is _good_)

8. [Expressibility, entanglement capability](https://arxiv.org/pdf/2012.09265), preserved symmetry (for ansatz).

9. Num of CNOTs?

## Devices (& Methodology)

1. Aer simulator

2. IBM_BRISBANE - decoherence times (relaxation time, dephasing time), native gates, coupling map.

3. IBM_SHERBROOKE

4. IBM online simulator (?)

5. (Try) Amazon bracket simulator

6. (Try) IonQ, Rigetti via MS Azure Q

7. (Try) Cirq Google's siomulator

8. (Try) PennyLane

# notes 04-24

1. metodologija: Opt algo -> chemistry -> chosen (1/2-1/3). (lit apzvalga)

2. ibmq hardware skyrelis. properties of computers

3. uzdavinio formuluote. kokia problema, kokie kintamieji, koks procesas/algorithmai (be konkreciu skaiciu)

4. eksperimentai.

///

Also pennylane zvilgtelt del naujienu

Also petkevicius atsius pavyzdyni baki

also iki pirmadienio tureti rezultatu grafiku ir ansatz palyginimo, ir aprasyti.
