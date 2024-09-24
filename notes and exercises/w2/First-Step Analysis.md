# First Step Analysis (revisited)

The $n$th power of a transition probability matrix having both transient and absorbing states is directly evaluated. 

## Conceptual set-up

Now consider a Markov chain with states labeled $0,1,\dots , N$. The states $0, 1, \dots , r-1$ are *transient*

$$\lim_{n \rightarrow \infty}\mathbf{P}_{ij}^{(n)} = 0, \quad \text{for } 0 \leq i,j < r$$
while states $r, \dots , N$ are absorbing. Here $\mathbf{P}_{ii}=1$ for $r \leq i \leq N$. The transition matrix has the form
$$\mathbf{P}= \left\Vert \begin{matrix} \mathbf{Q}  &  \mathbf{R}  \\ \mathbf{0} & \mathbf{I} \end{matrix} \right\Vert$$
E.g., a four-state transition matrix has the form
$$\mathbf{P}=\left\Vert \begin{matrix} Q_{00} & Q_{01} & R_{02}  & R_{03} \\ Q_{10}  & Q_{11} & R_{12} & R_{13} \\ 0 & 0 & 1 & 0  \\ 0 & 0 & 0 & 1\end{matrix} \right\Vert$$
It can be shown that raising the matrix to the $n$th power results in the following
$$
\begin{align}
\mathbf{P}^{n} = \left\Vert \begin{matrix} \mathbf{Q}^{n}  &  \left( \mathbf{I} + \mathbf{Q} + \cdots + \mathbf{Q}^{n-1} \right) \mathbf{R} \\ \mathbf{0} & \mathbf{I} \end{matrix} \right\Vert
\end{align}
$$

^aea52f

## Mean Number of Visits

Let $W_{ij}^{\left( n \right)}$ be the mean number of visits to state $j$ up to stage $n$ for a Markov chain starting in state $i$. Formally, 

$$W_{ij}^{(n)} = \mathbb{E}\left[\sum\limits_{k=0}^{n} \mathbf{1}\left\{ X_{k}=j  \mid X_{0}=i\right\}\right]$$
Where
$$\mathbf{1}\left\{ X_{t}=j \right\} = \begin{cases} 1,   &  \text{if } X_{t}=j  \\
0,  & \text{if } X_{t}\neq j \end{cases}$$
(The identity function).

Now, we make the simplification
$$\begin{align}
W_{ij}^{(n)} &= \mathbb{E}\left[\sum\limits_{k=0}^{n} \mathbf{1}\left\{ X_{k}=j  \mid X_{0}=i\right\}\right]\\
&= \sum\limits_{k=0}^{n} \mathbb{E} \left[\mathbf{1} \left\{ X_{k}=j \mid X_{0}=i\right\}\right]\\
&= \sum\limits_{k=0}^{n} \operatorname{P} \left( X_{k}=k ,\mid X_{0}=i \right) \\
&= \sum\limits_{k=0}^{n} \mathbf{P}_{ij}^{(n)}
\end{align}$$
Referring back to [[#^aea52f]], when $i$ and $j$ are transient we know that $P_{ij}^{k} = Q_{ij}^{k}$ (when $0 \leq i,j < r$), then

$$\begin{align}
W_{ij}^{(n)} &= Q_{ij}^{0} + Q_{ij}^{(1)} + \cdots +Q_{ij}^{(n)}, \quad 0 \leq i, j < r\\
\implies \mathbf{W}^{n} &= \mathbf{I} + \mathbf{Q}+\cdots +\mathbf{Q}^{n}, \quad \text{(matrix form)}\\
&\equiv \mathbf{I}+\mathbf{Q} \left( \mathbf{I}+\mathbf{Q} + \cdots + \mathbf{Q}^{n-1} \right) \\
&= \mathbf{I} + \mathbf{Q} \mathbf{W}^{n-1}
\end{align}$$
This can also be written as 

$$\begin{align}
W_{ij}^{(n)} &= \delta_{ij} + \sum\limits_{k=0}^{r-1} Q_{ik}W_{kj}^{(n-1)}\\
&= \delta_{ij}+ \sum\limits_{k=0}^{r-1} P_{ik}W_{kj}^{(n-1)}\\
\end{align}$$

*The equation asserts that the mean number of visits to state $j$ in the first $n$ stages starting from the initial stage $i$ includes the initial visit if $i=j \left( \delta_{ij} \right)$ plus the future visits during the $n-1$ remaining stages weighted by the appropriate transition probabilities.*

 Taking the limit
$$\begin{align}
W_{ij} &= \lim_{n \rightarrow \infty} W_{ij}^{(n)} \\
&= \mathbb{E} \left[\text{Total visits to } j \mid X_{0}=i\right], \quad 0 \leq i, j < r
\end{align}$$
Returning to the matrix equations
$$\begin{align}
\mathbf{W}^{n\rightarrow \infty} &= \mathbf{I} + \mathbf{Q} + \mathbf{Q}^{2}+ \cdots \\
&= \mathbf{I}+\mathbf{Q} \mathbf{W}^{n-1} \quad (\text{because } \lim_{n \rightarrow \infty}) \\
&= \mathbf{I}+\mathbf{Q}\mathbf{W} \\
\implies \mathbf{W} &= \mathbf{I}+\mathbf{Q}\mathbf{W} \\
\implies \mathbf{W}\left( \mathbf{I}-\mathbf{Q} \right)&=\mathbf{I}\\
\implies \mathbf{W}&= \left( \mathbf{I}-\mathbf{Q} \right)^{-1}
\end{align}$$
The matrix $\mathbf{W}$ is known as the *fundamental matrix* of $\mathbf{Q}$

## Relating the Above to Useful Results

### Mean Time to Absorption

Let $T$ be the time of absorption 

$$T = \min \left\{ n \geq 0; r \leq X_{n} \leq N \right\}$$
Then the $\left( i, j \right)$th element of the fundamental matrix $\mathbf{W}$ evaluates 
$$
\begin{align}
W_{ij}=\mathbb{E}\left[\sum\limits_{n=0}^{T-1} \mathbb{1}\left\{ X=j \right\} \mid X_{0}=i\right], \quad \text{for } 0 \leq i, j < r
\end{align}
$$
^aba5b3

Let $\nu_{i}= \mathbb{E}\left[T \mid X_{0}=i\right]$. The time to absorption is composed of *sojourns* in the transient states. Formally,
$$\begin{align}
\sum\limits_{j=0}^{r-1} \sum\limits_{n=0}^{T-1} \mathbb{1} \left\{ X_{n}=j \right\} &\equiv \sum\limits_{n=0}^{T-1} \sum\limits_{j=0}^{r-1} \mathbb{1} \left\{ X_{n}=j \right\} \\
&= \sum\limits_{n=0}^{T-1}1 = T
\end{align}$$
It follows from [[#^aba5b3]] that 
$$
\begin{align}
\sum\limits_{j=0}^{r-1} \sum\limits_{n=0}^{T-1} W_{ij} &=  \sum\limits_{j=0}^{r-1} \mathbb{E} \left[\sum\limits_{n=0}^{T-1}\mathbb{1}\left\{ X_{n}=j \right\} \mid X_{0}=i\right] \\
&= \mathbb{E} \left[T \mid X_{0}=i\right] \\
&= \nu_{i}, \quad \text{for } 0 \leq i < r
\end{align}
$$
Summing over the transient states
$$
\begin{align}
\sum\limits_{j=0}^{r-1} W_{ij}&= \sum\limits_{j=0}^{r-1} \delta_{ij} + \sum\limits_{j=0}^{r-1} \sum\limits_{k=0}^{r-1}P_{ij}W_{kj}
\end{align}
$$
Using the equivalence that $\nu_{i}=\sum\limits_{j=0}^{r-1} W_{ij}$ results in
$$
\nu_{i} = 1 + \sum\limits_{k=0}^{r-1} P_{ij}\nu_{k} \quad \text{for } i=0,1, \dots , r-1
$$
Which is identical to equation derived from first step analysis in [[Markov Chains 1#Lecture Notes#First-step analysis|Lecture 1]].

*The sum of each row $i$ of $\mathbf{W}$ gives us $\mathbb{E} \left[T \mid X_{0}=i\right]=\nu_{i}$.* 

### Hitting Probabilities

Probability of absorption in a particular absorbing state $k$ up to time $n$, starting from initial state $i$, is simply
$$\begin{align}
P_{ij}^{(n)} &= \operatorname{P} \left( X_{n}=k \mid X_{0}=i \right) \\
&= \operatorname{P} \left( T \leq n \text{ and } X_{T}=k \mid X_{0}=i \right)
\end{align}$$
for $i = 0, \dots , r-1$ and $k=r, \dots , N$.

Let $T = \min \left\{ n \geq 0: \ r \leq X_{n} \leq N \right\}$ is the time of absorption. Let
$$\mathrm{U}_{ik}^{(n)} = \operatorname{P} \left( T \leq n \text{ and } X_{T}=k \mid X_{0}=i \right)$$
For transient states, we know that they can only be hit once. Therefore, the hitting probability *is* the mean number of visits for transient states.

$$\begin{align}
\mathrm{U}^{(n)}&=\left( \mathrm{I} + \mathrm{Q} + \cdots \mathrm{Q}^{n-1} \right) \mathrm{R} \\
&= \mathrm{W}^{(n-1)}\mathrm{R}
\end{align}$$
Taking the limit, we get the hitting probabilities
$$\mathrm{U}_{ik}=\lim_{n \rightarrow \infty} \mathrm{U}_{ik}^{(n)} = \operatorname{P} \left( X_{T} = k \mid X_{0}=i \right)$$
for $0 \leq i < r$ and $r \leq k < N$.

Which leads us to the expression of hitting probabilities in terms of the fundamental matrix $\mathrm{W}$
$$\mathrm{U}= \mathrm{W} \mathrm{R}$$