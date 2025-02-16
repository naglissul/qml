$$
|\psi\rangle = e^{i\gamma}(\cos \frac \theta 2 |0\rangle + e^{i \varphi} \sin \frac \theta 2 |1\rangle)
$$

## NOT

$X|0\rangle = |1\rangle$

$X|1\rangle = |0\rangle$

## ?

$Y|0\rangle = e^{\frac \pi 2 i}|1\rangle = i|1\rangle$

$Y|1\rangle = e^{-\frac \pi 2 i}|0\rangle = -i|0\rangle$

## Phase

$P(\varphi)$ or $R_z(\theta)$

For which

$P(\varphi)|0\rangle = |0\rangle$

$P(\varphi)|1\rangle = e^{\varphi i}|1\rangle$

And then

$P(\pi) = Z$

$P(\frac \pi 2) = S$

$P(\frac \pi 4) = T$

$R_Z(\frac{3\pi}{2}) = S^\dagger$

$R_Y(\frac\pi2) = Y$

$R_Y(\frac\pi4) = \sqrt Y$

$R_Y(\frac{7\pi}{4}) = \sqrt Y ^\dagger$

### ALSO

$Z_1Z_2 = Z \otimes Z$

# Expvalues and ep. 4 of qiskit stuff

## Inner product

Similar to dot product, just with complex numbers stuff...

$\langle\psi|\psi\rangle$ = 1

$\langle 0|1\rangle = 0$

In case of $|\psi\rangle = \alpha|0\rangle + \beta|1\rangle$:

$\langle 0|\psi\rangle = \alpha$

## Dyadic form of gate:

$G = \sum_i \lambda_i|\phi_i\rangle\langle\phi_i|$

Ex:

$Z|0\rangle = |0\rangle$ and $Z|1\rangle = -|1\rangle$,

$\therefore Z = |0\rangle\langle0|-|1\rangle\langle1|$

## Density matrix

Pure or mixed state...

$\rho = \sum_i p_i |\psi_i\rangle\langle\psi_i|$

Ex:

Mixed state of $|0\rangle$ with 50% probability and $|1\rangle$ with 50% probability.

$\rho = \frac12 |0\rangle\langle0| + \frac12 |1\rangle\langle0| = \frac12 \begin{pmatrix}1 & 0 \\ 0 & 1\end{pmatrix} $

## Expval

Probabilistic:

$\langle \hat O \rangle = \sum_i \lambda_i P(\lambda_i)$, where $P(\lambda_i)$ means calculating probability of measuring the eigenvector of $\hat O$ (which has eigenvalue $\lambda_i$) in the state $|\psi\rangle$.

Matrix:

$\langle \hat O \rangle = \langle\psi|\hat O |\psi\rangle$

## Hamiltonian

Hamiltonian $H$ describes TIME EVOLUTION of a system. Writing in unitary operator, describing evolution over $t$ BASICALLY PARAMETERIZED QUANTUM CIRCUIT:

$U(t) = e^{-iHt}$

And this can be approximated using q-gates.

### Hamiltonian decomposition

e.g.: $H = Z_1Z_2 + X_1$

then $H_1=Z_1Z_2$ and $H_2=X_1$

### Trotter-Suzuki approximation

e.g.: $e^{=iHt} = e^{-iZ_1Z_2t}e^{-iX_1t}$

### Trotter term implementation

One qubit ($X$):

$$
R_x(2t)|\psi\rangle
$$

Two qubit diagonal needs entanglement ($Z_1Z_2$):

$$
CZ\;(R_2(-2t) \otimes I)\;CZ\;(|q_1\rangle \otimes |q_2\rangle)
$$

### Ising Hamiltonian

describes a system of interacting spins in a magnetic field:

$$H = \sum_{i<j} J_{ij}Z_iZ_j + \sum_i h_iX_i$$

$[H_1, H_2] \neq 0$, i.e. $H_1$ and $H_2$ don't commute. Therefore we need Trotter-Suzuki (?).

# Hydrogen VQE paper

# Extra for qiskit

## Measuring on _sth_ basis.

Applying observable operator and measuring and getting a certain operators eigenstate with probability of that eigenstate eigenvalue (ofc, abs squared).

**$Z$ basis (eigenstates): $\ket0$ and $\ket1$**

Because $Z\ket0 = \ket0$ and $Z\ket1 = -\ket1$

**$X$ basis (eigenstates): $\ket+ = \frac{\ket0 + \ket1}{\sqrt2}$ and $\ket- = \frac{\ket0 - \ket1}{\sqrt2}$**

Because $X\ket+ = \ket+$ and $X\ket- = -\ket-$

**$Y$ basis (eigenstates): $\ket{+i} = \frac{\ket0 +i\ket1}{\sqrt2}$ and $\ket{-i} = \frac{\ket0 -i\ket1}{\sqrt2}$**

> Reminder: $Y\ket0 = i\ket1$ and $Y\ket1 = -i\ket0$

Because $Y\ket{+i} = \ket{+i}$ and $Y\ket{-i} = -\ket{-i}$

So we basically whenever measuring a quantum state, we have to specify on what basis we are measuring. On what operator/matrix eigenvectors' basis. We can have a state $\ket\psi$ and express it as a linear combination of eigenvalues and eigenvectors (of specified operator/matrix/observable).

$$
\ket\psi \\
= \alpha_1\ket0 + \beta_1\ket1 \text{ this is on Z basis} \\
= \alpha_2\ket+ + \beta_2\ket- \text{ this is on X basis}\\
= \alpha_3\ket{+i} + \beta_3\ket{-i} \text{ this is on Y basis}
$$

For example:

$$
\ket{\Psi^-} \\
= \frac{1}{\sqrt2}\ket{00} - \frac{1}{\sqrt2}\ket{11} \text{  on ZZ basis}\\
= \frac{1}{\sqrt2}\ket{+i,+i} + \frac{1}{\sqrt2}\ket{-i,-i} = \frac{1}{\sqrt2}(\frac{1}{\sqrt2}\ket{00}+\frac{i}{\sqrt2}\ket{10}+\frac{i}{\sqrt2}\ket{01}-\frac{1}{\sqrt2}\ket{11}) + \frac{1}{\sqrt2}(\frac{1}{\sqrt2}\ket{00}-\frac{i}{\sqrt2}\ket{10}-\frac{i}{\sqrt2}\ket{01}-\frac{1}{\sqrt2}\ket{11}) \text{  on YY basis}\\
= \frac{1}{\sqrt2}\ket{+-} + \frac{1}{\sqrt2}\ket{-+} = \frac{1}{\sqrt2}(\frac{1}{\sqrt2}\ket{00}+\frac{1}{\sqrt2}\ket{10}-\frac{1}{\sqrt2}\ket{01}-\frac{1}{\sqrt2}\ket{11}) + \frac{1}{\sqrt2}(\frac{1}{\sqrt2}\ket{00}-\frac{1}{\sqrt2}\ket{10}+\frac{1}{\sqrt2}\ket{01}-\frac{1}{\sqrt2}\ket{11}) \text{  on XX basis}
$$

# Trying to set the thesis scope

