# 3.1.4 - Creating a Transition Probability Matrix

The random variables $\xi_{1}, \xi_{2}, \dots$ are independent and with common probability mass function

| $k$                         | $0$   | $1$   | $2$   | $3$   |
| --------------------------- | ----- | ----- | ----- | ----- |
| $\operatorname{P}(\xi = k)$ | $0.1$ | $0.3$ | $0.2$ | $0.4$ |
Set $X_{0}=0$ and let $X_{n}=\max \left\{ \xi_{1}, \dots , \xi_{n} \right\}$ be the largest $\xi$ observed to date. *Determine the transition probability matrix*
- Starting at $X_{0}=0$, the probability of the next state corresponds to that in the above probability mass function.
$$\begin{bmatrix} 0.1  & 0.3 & 0.2 & 0.4  \end{bmatrix}$$
- Moving into $X_{n}=1$, the probability that the maximum $\xi$ observed is equal to $1$ is now the sum of $P(\xi=0)$ and $P(\xi=1)$.
$$\begin{bmatrix} 0 & 0.4 & 0.2 & 0.4 \end{bmatrix}$$
and so on...
$$\begin{align}
\mathrm{P} &= \left\Vert \begin{matrix} 0.1 & 0.3 & 0.2 & 0.4\\
0 & 0.4 & 0.2 & 0.4\\
0 & 0 & 0.6 & 0.4\\
0 & 0 & 0 & 1 \end{matrix} \right\Vert
\end{align}$$
$\checkmark$
# 3.2.1 - Limiting Distribution

Consider the Markov chain with the following transition probability matrix
$$\begin{align}
\begin{bmatrix} 0.40 & 0.30 & 0.20 & 0.10\\ 0.10 & 0.40 & 0.30 & 0.20\\ 0.30 & 0.20 & 0.10 & 0.40\\ 0.20 & 0.10 & 0.40 & 0.30 \end{bmatrix}
\end{align}$$
Suppose that the initial distribution is $p_{i} = \frac{1}{4}$ for  $i = 0,1,2,3$. *Show that* $\operatorname{P} \left( X_{n}=k \right) = \frac{1}{4}, k=0,1,2,3$, for all $n$. *Can a general result be deduced from this example?*

We know that for [[Markov Chains 1#n-step Transition Probability Matrices|n-step]] transition probabilities from state $i$ to $j$ are given by raising the 1-step transition probability matrix to the power of $n$. I.e.,
$$\operatorname{P} \left( X_{n}=j \mid X_{0}=i \right) = \mathrm{P}^{n}_{ij}$$
Using the [[Markov Chains 1#Law of Total Probability|law of total probability]], we can incorporate the initial distribution
$$\begin{align}
\operatorname{P} \left( X_{n}=k \right) &= \sum\limits_{i=0}^{3} \operatorname{P} \left( X_{0}=i \right) \operatorname{P} \left( X_{n}=k \mid X_{0}=i \right)\\
&=  \frac{1}{4} \left( \sum\limits_{i=0}^{3} \mathrm{P}^{n}_{ik}  \right)\\
&= \frac{1}{4}\sum\limits_{i=0}^{3} \mathrm{P}^{n}_{ik} 
\end{align}$$
Which simply $\frac{1}{4}$ of the sum of a single column in the n-step transition probability matrix. Iterating through a varying number of $n$s we find that this is consistently equal to $\frac{1}{4}$.

This is because the transition probability matrix is [[Markov Chains 3#Doubly Stochastic Matrices|doubly stochastic]], resulting in a uniform limiting distribution.

**Should be proven via induction. But reasoning is sound.**

# 3.4.4 - Probability of Never Reaching a Specific Transitory State

We are given the following transition probability matrix of a Markov chain
$$\begin{align}
\mathrm{P} &= \left\Vert \begin{matrix} 1 & 0 & 0 & 0\\
0.1 & 0.2 & 0.5 & 0.2\\
0.1 & 0.2 & 0.6 & 0.1 \\
0.2 & 0.2 & 0.3 & 0.3  \end{matrix} \right\Vert
\end{align}$$
and asked to find, given that the starting state $X_{0}=1$, *the probability that the process never visits state 2.*

We can express this formally as
$$\begin{align}
\operatorname{P} \left( X_{n}=0 \mid X_{0}=1 \text{ and } X_{i} \neq 2 \text{ for all } i \in \left\{ 1,2,\dots, n-1 \right\} \right)
\end{align}$$
**Credits to Peter:**

Can convert state $2$ into an absorbing state, keeping other transition probabilities the same, creating a new probability transition matrix
$$\begin{align}
\mathrm{P}&= \left\Vert \begin{matrix} 1 & 0 & 0 & 0\\
0.1 & 0.2 & 0.5 & 0.2 \\
0 & 0 & 1 & 0\\
0.2 & 0.2 & 0.3 & 0.3 \end{matrix} \right\Vert
\end{align}$$
and calculate the probability of the process absorbing in state $0$, given that the process starts in state $1$

- $u_{0}=1$
- $u_{1}=0.1 u_{0}+0.2u_{1}+0.2u_{3}$
	- $\implies 0.8 u_{1}=0.1+0.2 \cdot \frac{0.2}{0.7} \left( 1+u_{1} \right)$
	- $\vdots$
	- $u_{1} \approx 0.212$
- $u_{2}=0$
- $u_{3}=0.2 +0.2 u_{1}+0.3 u_{3}$
	- $\implies 0.7 u_{3}=0.2+0.2 u_{1}$
	- $\implies u_{3} = \frac{0.2}{0.7} \left( 1+u_{1} \right)$

# 3.2.5 - Long time until absorption

We are given the following transition probability matrix
$$\begin{align}
\mathrm{P}&= \left\Vert \begin{matrix} 0.7 & 0.2 & 0.1\\
0.3 & 0.5 & 0.2\\
0 & 0 & 1 \end{matrix} \right\Vert
\end{align}$$
The Markov chain starts in state $X_{0}=0$. Let
$$T = \min \left\{ n \geq 0 ; X_{n}=2 \right\}$$
be the first time the process reaches state $2$ (absorbing).

We are asked to *determine $\operatorname{P} \left( X_{3}=0 \mid X_{0}, T>3 \right)$* 

**Hint:** The event $\left\{ T > 3 \right\}$ is the same as the event $\left\{ X_{3}\neq 2 \right\}=\left\{ X_{3}=0 \right\} \cup \left\{ X_{3}=1 \right\}$. 

Using this hint, we re-write the conditional probability using the law of total probability and the results from an n-step transition probability matrix
$$\begin{align}
\operatorname{P} \left( X_{3}=0 \mid X_{0}, X_{3}=0 \ \lor \ X_{3}=1  \right) &= \frac{\operatorname{P} \left( X_{3}=0 \cap \left( \left( X_{0}, X_{3}=0 \right) \cup \left( X_{0}, X_{3}=1 \right)\right) \right)}{\operatorname{P} \left(  \left( X_{0}, X_{3}=0 \right) \cup \left( X_{0}, X_{3}=1 \right)\right)} \\
&= \frac{\operatorname{P} \left( X_{3}=0 \cap \left( X_{0}, X_{3}=0 \right) \right) + \operatorname{P} \left( X_{3}=0 \cap \left( X_{0}, X_{3}=1 \right) \right)}{\operatorname{P} \left( X_{0}, X_{3}=0 \right) + \operatorname{P} \left( X_{0}, X_{3}=1 \right)}\\
&= \frac{\mathrm{P}_{00}^{3}+0}{\mathrm{P}_{00}^{3}+\mathrm{P}_{01}^{3}}\\
&= \frac{1}{0.457+0.230}\\
&= 0.665 \checkmark
\end{align}$$
# 3.4.7 - First-Step Analysis

$X_{n}$ is a Markov chain with transition probabilities $P_{ij}$. We are given a discount factor $\beta$ with $0 < \beta < 1$ and a cost function $c(i)$, and we wish to determine the *total expected discounted cost starting from state $i$*, defined by
$$\begin{align}
h_{i} &= \mathbb{E} \left[\sum\limits_{n=0}^{\infty} \beta^{n} c \left( X_{n} \right) \mid X_{0}=i\right]
\end{align}$$
Solving 
$$\begin{align}
h_{i} &= \mathbb{E} \left[\sum\limits_{n=0}^{\infty} \beta^{n} c \left( X_{n} \right) \mid X_{0}=i\right] \\
 &= \mathbb{E}\left[\beta^{0} c(X_{0}) + \sum\limits_{n=1}^{\infty}\beta^{n}c (X_{n}) \mid X_{0}=i\right] \\
&= \mathbb{E} \left[c(i)+\sum\limits_{n=1}^{\infty}\beta^{n}c (X_{n}) \mid X_{0}=i\right] \\
&= c(i) + \mathbb{E}\left[\sum\limits_{n=1}^{\infty} \beta^{n} c (X_{n}) \mid X_{0}=i\right]
\end{align}$$
Now, we can incorporate the transition probabilities in the following way: $X_{0}=i$, let $X_{1}=j$. Since all transitions $i \rightarrow j$ are mutually exclusive, the following holds

$$\begin{align}
&= c(i) + \sum\limits_{j}^{}\mathbb{E} \left[\sum\limits_{n=1}^{\infty} \beta^{n} c(X_{n}) \mid X_{0}=i, X_{1}=j\right] P_{ij} \\
&= c(i) + \sum\limits_{j}^{}  \mathbb{E} \left[\sum\limits_{n=1}^{\infty} \beta^{n} c(X_{n}) \mid X_{1}=j\right] P_{ij}\\
&= c(i) + \sum\limits_{j}^{}  \mathbb{E} \left[\sum\limits_{n=0}^{\infty} \beta^{n+1} c(X_{n+1}) \mid X_{1}=j\right] P_{ij} \\
&= c(i) + \beta \sum\limits_{j}^{}  \mathbb{E}  \left[\sum\limits_{n=0}^{\infty} \beta^{n} c(X_{n}) \mid X_{0}=j\right] P_{ij} \\
&= c(i)+\beta \sum\limits_{j}^{} h_{j}P_{ij}
\end{align}$$
