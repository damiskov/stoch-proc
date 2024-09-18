# Content
- Limiting and invariant distributions
- Classification of states and chains
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
## Doubly Stochastic Matrices

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
# Classification of States

(Typo on [[textbook- Prob 2.pdf#page=201|page 194]] ?)


A Markov chain with probability transition matrix is given by
$$\begin{align}
\mathrm{P} = \left\Vert \begin{matrix}  0 & 1 \\
1 & 0 \end{matrix} \right\Vert
\end{align}$$
Oscillates deterministically between the two states $0, 1$. The Markov chain is *periodic* and *no limiting distribution exists.*

Another transition probability matrix for a Markov chain is given by
$$\begin{align}
\mathrm{P} = \left\Vert \begin{matrix} \frac{1}{2} & \frac{1}{2}\\
0 & 1 \end{matrix} \right\Vert
\end{align}$$
$\mathrm{P}$ is given by
$$
\begin{align}
\mathrm{P}^{n} &= \left\Vert \begin{matrix} \left( \frac{1}{2} \right)^{n}  & 1-\left( \frac{1}{2} \right)^{n} \\ 0 & 1 \end{matrix} \right\Vert\\
\implies \lim_{n \rightarrow \infty} \mathrm{P}^{n} &= \left\Vert \begin{matrix} 0 & 1\\
0 & 1 \end{matrix} \right\Vert
\end{align}
$$
Here, state $0$ is *transient*, I.e, after a process starts from state $0$ there is a positive probability that it will never return to that state.

## Irreducible Markov Chains
- State $j$ is *accessible* from state $i$ if $P_{ij}^{n} >0$ for some integer $n \geq 0$. I.e., it can be reached from state $i$ in a finite number of transitions.
- If two states $i,j$ are each accessible to the other, they are said to *communicate* $i \leftrightarrow j$.
	- If two states $i$ and $j$ do not communicate, then either
$$P_{\mathbf{ij}}^{n}=0, \quad \text{for all } n \geq 0$$
or, 
$$P_{\mathbf{ji}}^{n}=0, \quad \text{for all } n \geq 0$$

## Periodicity of a Markov Chain

The *period* of a state $i$ (denoted $d(i)$), is the greatest common divisor of all integers $n \geq 1$ for which $P_{ii}^{n} > 0$.

Some basic properties of the period of a state
1. If $i \leftrightarrow j$ then $d(i)=d(j)$
This assertion shows that the *period is a constant in each class of communicating states.*
2. If state $i$ has period $d(i)$, then there exists an integer $N$ depending on $i$ such that for all integers $n \geq N$,
$$P_{ii}^{(n \cdot d(i))} >0$$
Asserts that *a return to state $i$ can occur at all sufficiently large multiples of the period $d(i).$*
3. If $P_{ji}^{(m)}>0$, then $P_{ji}^{(m+n \cdot d(i))}>0$ for all $n \in \mathbb{Z}^+$ sufficiently large.  

### ChatGPT

The **periodicity of a state** in a Markov chain refers to how often, in a regular cycle, you can return to that state.
#### Simple Explanation:

Imagine you're in a state of a Markov chain (like being on a specific spot in a game board). The **period** of this state is the number of steps (or moves) it takes to come back to this spot in a regular pattern.
- **Period = 1**: This means you can return to the state after 1 step, 2 steps, 3 steps, etc., without any specific pattern. You can come back at any time, so it's called **aperiodic** (no fixed cycle).
- **Period > 1**: If the state has a period of 2, for example, it means you can only return to this state after an even number of steps (like 2, 4, 6 steps, etc.). There is a regular pattern or cycle to when you can come back.
## Recurrent and Transient States

Consider an arbitrary, but fixed state $i$. We define, for each integer $n \geq 0$,
$$
\begin{align}
f_{ii}^{(n)} &= \operatorname{P} \left( X_{n}=i, X_{\nu} \neq i, \nu=1,2, \dots n-1 \mid X_{0}=i \right)
\end{align}
$$
I.e., the probability of starting in state $i$, and returning to state $i$ in $n$ transitions is given by $P_{ii}^{(n)}$. Clearly
$$\begin{align}
f_{ii}^{(1)} = P_{ii}
\end{align}$$
$f_{ii}^{(n)}$ can be calculated recursively according to
$$
\begin{align}
P_{ii}^{(n)} &= \sum\limits_{k=0}^{n} f_{ii}^{(k)}P_{ii}^{(n-k)}, \quad n \geq 1
\end{align}
$$
Consider all possible ways for a Markov process to proceed from $X_{0}=i$ to $X_{n}=i$, and the first return to state $i$ is at the $k < n$'th transition. Call this event $E_{k}$. This is given by $f_{ii}^{(k)}.$ In the remaining $n-k$ transitions, we are only dealing with processes that end with $X_{n}=i$. Using the Markov property
$$\begin{align}
\operatorname{P} \left( E_{k} \right) &= \operatorname{P} \left( \text{first return is at } k \text{th transition} \mid X_{0}=i \right) \operatorname{P} \left( X_{n}=i \mid X_{k}=i \right)\\
&\equiv f_{ii}^{(k)} \cdot P_{ii}^{(n)}, \quad 1 \leq k \leq n
\end{align}$$
## The Basic Limit Theorem of Markov Chains

First, consider a recurrent state $i$. Then, 

$$f_{ii}^{(n)} = \operatorname{P} \left( X_{n}=i, X_{\nu} \neq i \quad\text{ for } \nu=1, \dots , n-1 \mid X_{0}=i \right)$$
is the probability distribution of the *first return time*
$$
R_{i}=\min \left\{ n \geq 1 ; X_{0}=i \right\}
$$
This is,
$$
f_{ii}^{\left( n \right)}= \operatorname{P} \left( R_{i}=n \mid X_{0}=i \right), \quad \text{for } n=1, 2, \dots 
$$
We are assuming that state $i$ is recurrent (obviously), then $f_{ii} = \sum\limits_{n=1}^{\infty} = f_{ii}^{(n)}=1$ (i.e., we must return to state $i$ at some point), and $R_{i}$ is a finite valued random variable. The mean duration between visits to state $i$ is 
$$
m_{i}=\mathbb{E}\left[R_{i} \mid X_{0}=i\right] = \sum\limits_{n=1}^{\infty} n \cdot f_{ii}^{(n)}
$$
After starting in state $i$, the processes is (on average) back in state $i$ after $m_{i}= \mathbb{E}\left[R_{i}\mid X_{0}=i\right]$.

### Theorem 4.3 - The basic limit theorem of Markov Chains

- Consider a *recurrent*, *aperiodic*, *irreducible* Markov chain.
- $P_{ii}^{(n)}$ is the probability of entering state $i$ at the $n$th transition, given that $X_{0}=i$.
- Let $f_{ii}^{(n)}$ be the probability of first returning to state $i$ at the $n$th transition.
Then,
$$\lim_{n \rightarrow \infty}P_{ii}^{(n)} = \frac{1}{\sum\limits_{n=0}^{\infty} n \cdot f_{ii}^{(n)}}= \frac{1}{m_{i}}$$

