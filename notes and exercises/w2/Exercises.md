# 3.6.1 - Random Walks

A rate is put in a linear maze with $6$ possible states:
$$\left\{ X_{0} \text{ (shock)}, X_{1}, X_{2}, X_{3} \text{ (rat)}, X_{4}, X_{5} \text{ (food)} \right\}$$
**a) Assume that the rat is equally likely to move right or left at each step. What is the probability that the rat finds the food before getting shocked?**

I.e., what is the probability of ending up in state $5$, starting in any state $k \in \left\{ 1,2,3,4 \right\}$?

We will assume that both states $0$ and $5$ are absorbing. 
$$\begin{align}
\operatorname{P} \left( X_{T}=5 \mid X_{0}=k \right) &=1-\operatorname{P} \left( X_{T}=0 \mid X_{0}=k \right)\\
\implies \operatorname{P} \left( X_{T}=5 \mid X_{0}=k \right) &= 1-u_{k} \\
\end{align}$$
Since $\theta=\frac{q}{p}=1 \implies u_{k} = \frac{N-k}{N}$


**(b) As a result of learning, at each step the rat moves to the right with probability $p > \frac{1}{2}$ and to the left with probability $q = 1−p < \frac{1}{2}$. What is the probability that the rat finds the food before getting shocked?**

Same question, but now using the case where $p \neq q:$
$$\begin{align}
\operatorname{P} \left( X_{T}=5 \mid X_{0}=k \right) &= 1-u_{k} \\
&=1-\frac{\left( \frac{q}{p} \right)^{3}-\left( \frac{q}{p} \right)^{5}}{1-\left( \frac{q}{p} \right)^{5}}
\end{align}$$
# 3.7.1 - More First-Step Analysis

Given the Markov chain with transition probability matrix is given by
$$\mathrm{P}=\left\Vert \begin{matrix} 1 & 0 & 0 & 0  \\ 0.1 & 0.2 & 0.5 & 0.2  \\  0.1 & 0.2  & 0.6 & 0.1 \\ 0 & 0 & 0 & 1 \end{matrix} \right\Vert$$
Re-ordering the matrix ($\left\{ 1,2,3,4 \right\} \rightarrow \left\{2, 3, 1, 4\right\}$)

$$\begin{align}
\mathrm{P}&=\left\Vert \begin{matrix} \mathbf{Q}  &  \mathbf{R}  \\ \mathbf{0} & \mathbf{I} \end{matrix} \right\Vert\\
&=\left\Vert \begin{matrix} 0.2 & 0.5 & 0.1 & 0.2 \\ 0.2 & 0.6 & 0.1 & 0.1 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{matrix} \right\Vert
\end{align}$$
Therefore, 
$$\mathrm{Q}=\left\Vert \begin{matrix} 0.2 & 0.5 \\ 0.2 & 0.6 \end{matrix} \right\Vert, \quad \mathrm{R}=\left\Vert \begin{matrix} 0.1 & 0.2 \\ 0.1 & 0.1 \end{matrix} \right\Vert$$
The fundamental matrix is given by
$$\begin{align}
\mathrm{W} &= \left( \mathrm{I}-\mathrm{Q} \right)^{-1}\\
&= \left\Vert \begin{matrix} 1.82 &  2.27 \\
0.91  &  3.64 \end{matrix} \right\Vert
\end{align}$$
**a) the probability of absorption into state 0 starting from state 1**

- $u_{1}=0.1+0.2u_{1}+0.5u_{2}$
- $u_{2}=0.1+0.2u_{1}+0.6u_{2}$
$$\begin{align}
\mathrm{u} &= \mathrm{Q} \mathrm{u} + \begin{bmatrix} 0.1\\
0.1 \end{bmatrix}\\
\implies \mathrm{u} &= \left( \mathrm{I}-\mathrm{Q} \right)^{-1}\begin{bmatrix} 0.1\\
0.1 \end{bmatrix} \\
&= \mathrm{W} \begin{bmatrix} 0.1\\
0.1 \end{bmatrix} \\
&= \begin{bmatrix}0.409 \\ 0.455\end{bmatrix}
\end{align}$$

Which is the same as the first column of:
$$\begin{align}
\mathrm{U} &= \mathrm{W} \mathrm{R} \\
&= \left\Vert \begin{matrix} 1.82 &  2.27 \\
0.91  &  3.64 \end{matrix} \right\Vert \cdot \left\Vert \begin{matrix} 0.1 & 0.2 \\ 0.1 & 0.1 \end{matrix} \right\Vert \\
&= \left\Vert \begin{matrix} 0.41  & 0.59 \\ 0.45  &  0.55 \end{matrix} \right\Vert
\end{align}$$
So the answer is $0.41$.

**b) the mean time spent in each of states 1 and 2 prior to absorption.**

Using the information from [[Markov Chains 2#First Step Analysis (revisited)#Relating the Above to Useful Results#Mean Time to Absorption|the notes]], we know that *The sum of each row $i$ of $\mathbf{W}$ gives us $\mathbb{E} \left[T \mid X_{0}=i\right]=\nu_{i}$*. Therefore,

$$\nu= \begin{bmatrix} 1.82+2.27 \\ 0.91+3.64 \end{bmatrix} = \begin{bmatrix} 4.09  \\ 4.55 \end{bmatrix}$$
# 2.3.3 - Distribution of a Random Sum

Suppose that upon striking a plate a single electron is transformed into a number $X_{1}$ of electrons, where $X_{1}$ is a random variable with mean $\mu$ and standard deviation $\sigma$ . Suppose that each of these electrons strikes a second plate and releases further electrons, independently of each other and each with the same probability distribution as $X_{1}$. Let $X_{2}$ be the total number of electrons emitted from the second plate. Determine the mean and variance of $X_{2}$.

Set up:

This is a random sum $X = \xi_{1}+ \dots +\xi_{N}$ where $N \sim \mathcal{N}\left( \mu, \sigma^2 \right)$ and $\xi \sim \mathcal{N} \left( \mu, \sigma^{2} \right)$.

Therefore,
$$\begin{align}
\mathbb{E}\left[\xi_{k}\right] &= \mu, \quad \operatorname{Var}\left( \xi_{k} \right)=\sigma^{2}\\
\mathbb{E}\left[N\right] &= \nu = \mu, \quad \operatorname{Var} \left( N \right) = \tau^{2} = \sigma^{2}
\end{align}$$

Using [[Markov Chains 2#Random Sums#Moments of A Random Sum|the moments of a random sum]] we know that 
$$\begin{align}
\mathbb{E}\left[X\right] &= \mu \nu \\
&= \mu^{2}
\end{align} $$
and 
$$\begin{align}
\operatorname{Var} \left( X \right) &= \nu \sigma^{2} + \mu^{2} \tau^{2}\\
&= \mu \sigma^{2}+\mu^{2} \sigma^{2}\\
&= \mu \sigma^{2} \left( 1+\mu \right)
\end{align}$$
# 3.9.2 - Probability Generating Functions

**Determine the probability generating function for the offspring distribution in which an individual either dies, with probability $p_0$, or is replaced by two progeny, with probability $p_2$, where $p_0 + p_2 = 1$.**

Offspring distribution: $p_{k} = \operatorname{P} \left( \xi =k \right)$ where $k \in \left\{ 0,2 \right\}$. This has the generating function
$$\begin{align}
\phi \left( s \right) &= \mathbb{E}\left[s^{\xi}\right] \\
&= \sum\limits_{k \in \left\{ 0, 2 \right\}}^{} s^{k} p_{k}\\
&= s^{0}p_{0}+s^{2}p_{2}\\
&= p_{0}+s^{2}p_{2}
\end{align}$$
We can re-write this in the form of $p_{0}$ alone
$$\begin{align}
&= p_{0}+s^{2} \left( 1-p_{0} \right) \\
&= p_{0} \left( 1-s^{2} \right) + s^{2}
\end{align}$$
