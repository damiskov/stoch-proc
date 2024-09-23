# Regular Transition Probability Matrices

Consider a transition probability matrix $\mathrm{P} = \left\Vert P_{ij} \right\Vert$ on a finite number of states labeled $0,1,\dots , N$ that has the property 
$$\operatorname{all} \left( \mathrm{P}^{k} \right) >0$$
Such a transition probability matrix/Markov chain is called *regular*. A significant feature of regular Markov chains is the existence of *limiting probability distributions* 
$$\pi=\left( \pi_{0}, \pi_{1}, \dots , \pi_{N} \right), \quad \forall j \in \left\{ 0, 1, \dots , N \right\}: \pi_{j} >0,$$
$\sum\limits_{j}^{}\pi_{j}=1$ and this distribution is independent of the initial state. For a regular transition matrix we have the *convergence*
$$\lim_{n \rightarrow \infty} P_{ij}^{(n)}=\pi_{j} > 0 \quad\text{for } j=0, 1, \dots N$$
This convergence means that in the long run ($n \rightarrow \infty$), the probability of finding the Markov chain in state $j$ is approximately $\pi_{j}$ no matter in which state the chain began at time $0$.
### Theorem 4.1
Let $\mathrm{P}$ be a regular transition probability matrix on the states $0,1,\dots N$. Then the limiting distribution $\mathbf{\pi} = \left( \pi_{1}, \pi_{2}, \dots \pi_{N} \right)$ is the unique nonnegative solution of the equations
$$
\begin{align}
\pi_{j}&= \sum\limits_{k=0}^{N} \pi_{k} \mathrm{P}_{kj}, \quad j=0, 1, \dots N \\
\sum\limits_{k=0}^{N} \pi_{k} &= 1
\end{align}
$$
# Doubly Stochastic Matrices

A transition probability matrix is called *doubly stochastic* if the columns sum to one as well as the rows. Formally, $\mathrm{P}=\left\Vert P_{ij} \right\Vert$ is doubly stochastic if
$$\begin{align}
P_{ij}\geq 0 \quad \text{and} \quad \sum\limits_{k}^{}P_{ik}=\sum\limits_{k}^{}P_{kj} \quad \text{for all } i, j\\
\end{align}$$
- Have uniform limiting distribution.

## Interpretation of the Limiting Distribution

Second interpretation of the limiting distribution: 
- $\pi_{j}$ also gives the long run mean fraction of time that the process $\left\{ X_{n} \right\}$ is in state $j$.

Thus, if each visit to state $j$ incurs a “cost” of $c_{j}$, then the long run mean cost per unit time associated with this Markov chain is
$$
\text{Long run mean cost per unit time} = \sum\limits_{j=0}^{N} \pi_{j}c_{j}
$$
