# Content

- Random walks
- First step analysis
- Random sums
- Probability generating functions
- Branching processes

# Random Walks

## The General Random Walk

The general random walk probability transition matrix
$$\begin{align}
\mathbf{P}=\left\Vert \begin{matrix} 1 & 0 & 0 & 0 & \cdots  & 0\\
q_{1} & r_{1} & p_{1} & 0 & \cdots  & 0\\
0 & q_{2} & r_{2} & p_{2} & \cdots  & 0\\
\vdots  & \vdots  & \vdots & \vdots  &   & \vdots\\
0 & 0 & 0 & 0 & \cdots  & 1  \end{matrix} \right\Vert
\end{align}$$
Where $q_{k} > 0$ and $p_{k}>0$ for $k=1, \dots , N-1$. Let $T = \min \left\{ n \geq 0; X_{n}=0 \ \lor \ X_{n}=0 \right\}$, i.e., the hitting time for states $0$ and $N$.

**Case where transition probabilities are the same from row to row:**

$$p \geq 0, \quad q \geq 0, \quad p+q+r = 1$$
Making some abbreviations

$$\rho_{k}= \frac{q_{1}q_{2}\cdots q_{k}}{p_{1}p_{2}\cdots p_{k}}= \left( \frac{q}{p} \right)^{k}=\theta^{k}, \quad \text{for } k=1, \dots , N-1$$
The **probability of gambler's ruin** (i.e., the process being absorbed in state $0$ before reaching state $N$) becomes
$$\begin{align}
u_{k} &= \operatorname{P} \left( X_{T}=0 \mid X_{0}=k \right) \\
&= \frac{\theta^{k}+\cdots + \theta^{N-1}}{1+\theta+\cdots +\theta^{N-1}} \\
&= \begin{cases} \dfrac{\theta^{k}-\theta^{N}}{1-\theta^{N}}, \quad \text{if } p \neq q \\
\dfrac{N-k}{N}, \quad \text{if } p=q\end{cases}
\end{align}$$
**Mean time** before absorption
$$\nu_{k}=\mathbb{E}\left[T \mid X_{0}=k\right], \quad \text{for } k=1, \dots , N-1$$
by first substituting $\rho_{i}=\theta_{i}$ into 

$$\vdots  \text{ (a lot of workings)}$$
$$\begin{align}
\nu_{i} &= \mathbb{E} \left[T \mid X_{0}=i\right] \\
&= \begin{cases} \dfrac{i \left( N-i \right)}{2p}, \quad \text{if } p=q \\
\dfrac{1}{p \left( 1-\theta \right)} \left[N \left( \dfrac{1-\theta^{i}}{1- \theta^{N}} \right)-i\right], \quad q \neq p \end{cases}
\end{align}$$

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
# Random Sums
- Dealing with sums of the form $X = \xi_{1}+ \dots + \xi_{N}$ where $N$ is random.
## Set up
- A sequence of $\xi_{1}, \xi_{2}, \dots$ IID (random) variables.
- $N$ is a discrete random variable.
	- Has probability mass function $p_{N}(n) = \operatorname{P} \left( N=n \right)$
Random sum $X$ is defined as 
$$X = \begin{cases} 0,  &  \text{if } N=0 \\
 \xi_{1}+ \dots + \xi_{N}  & \text{if } N > 0\end{cases}$$
## Conditional Distributions: The Mixed Case
- Let $X$ and $N$ be to jointly distributed random variables. 
- Possible values for $N$ are the discrete set $n=0,1,2,\dots$
- Define the *conditional distribution function* $F_{X \mid N} \left( x \mid n \right)$ of the random variable $X$, given that $N=n$, to be
$$F_{X \mid N} \left( x \mid n \right) = \frac{\operatorname{P} \left( X \leq x \text{ and } N=n \right)}{\operatorname{P} \left( N=n \right)} \ \text{ if } \operatorname{P} \left( N=n \right)>0$$
- Suppose that $X$ is continuous and that $F_{X \mid N} \left( x \mid n \right)$ is differentiable wrt $x$ at every $n$. The *conditional probability density function* is given as 
$$f_{X \mid N} \left( x \mid n \right) = \frac{d}{dx} F_{X \mid N} \left( x \mid n \right) \quad \left( \text{if } \operatorname{P} \left( N=n \right) >0 \right)$$
Can now define
$$\operatorname{P} \left( a \leq X < b, N=n \right) = \int_{a}^{b} f_{X \mid N} \left( x \mid n \right) p_{N}\left( n \right)dx$$
(where $p_{N}(n)= \operatorname{P} \left( N=n \right)$)

Using the *law of total probability* 
$$f_{X}(x) = \sum\limits_{n=0}^{\infty}f_{X \mid N} \left( x \mid n \right) p_{N}\left( n \right)$$
Suppose that $g$ is a function and $\mathbb{E}\left[\left\vert g(X) \right\vert\right] < \infty$. Conditional expectation of $g(X)$, given that $N=n$ is 
$$\mathbb{E}\left[g(X) \mid N=n\right] = \int g(x) f_{X \mid N} \left( x \mid n \right) dx$$
## Moments of A Random Sum
Assuming that $\xi_{k}$ and $N$ have finite moments 
$$\begin{align}
\mathbb{E}\left[\xi_{k}\right] &= \mu, \quad \operatorname{Var}\left( \xi_{k} \right)=\sigma^{2}\\
\mathbb{E}\left[N\right] &= \nu, \quad \operatorname{Var} \left( N \right) = \tau^{2}
\end{align}$$
The mean and variance for $X = \xi_{1}+\dots +\xi_{n}$ are
$$\begin{align}
\mathbb{E}\left[X\right] &= \mu \nu\\
\operatorname{Var} \left( X \right) &= \nu \sigma^{2}+\mu^{2} \tau^{2}
\end{align}$$

# Branching Processes and Generating Functions

### ChatGPT
A **probability generating function** (PGF) is a tool used in probability theory to describe a **discrete random variable**. Here's a simple breakdown:
- A **random variable** is something that can take on different values, each with a certain chance (probability). For example, the number of heads when flipping a coin three times is a random variable.
- The **probability distribution** tells you how likely each outcome of the random variable is. It shows the probabilities for each possible value the random variable can take.
- The **generating function** is a clever way of packaging this probability information into a mathematical formula. For a discrete random variable $X$, the PGF is a function $G_{X}​(t)$ defined as:
    $$G_{X}(t)=E(t^{X})=\sum\limits_{x=0}^{\infty}P(X=x)t^{x}$$
    In simpler terms, this formula is made by taking each possible value $x$ of the random variable, multiplying its probability $P(X=x)$ by $t^{x}$ (where $t$ is just a variable), and then adding them all up.
#### Why is it useful?
The PGF makes it easier to:
- Calculate probabilities and moments (like the mean or variance).
- Work with sums of independent random variables (like when adding two dice rolls together).
In essence, a PGF helps you encode all the probabilities of a random variable into a single function, which can then be used for various calculations.

## Overview

Consider a nonnegative integer-valued random variable $\xi$ whose probability distribution is given by

$$\begin{align}
\operatorname{P} \left( \xi=k \right)=p_{k}, \quad \text{for } k=0, 1, \dots
\end{align}$$
^prob-mass-func

This random variable $\xi$ (or distribution $\left\{ p_{k} \right\}$) can be associated with a *generating function* $\phi \left( s \right)$. The generating function is defined as 

$$\begin{align}
\phi \left( s \right) = \mathbb{E}\left[s^{\xi}\right]=\sum\limits_{k=0}^{\infty} p_{k} s^{k}, \quad \text{for } s \in [0, 1]
\end{align}$$
^prob-gen-func

Much of the importance of generating functions derives from the following three results.


1. First, the relation between probability mass functions [[#^prob-mass-func]] and generating functions [[#^prob-gen-func]] is one-to-one. Knowing the generating function is equivalent to knowing the distribution and vice versa.

The *expression relating the probability mass function and probability generating function* is

$$\begin{align*}
p_{k} &= \frac{1}{k!} \frac{d^{k} \phi \left( s \right)}{d s^{k}}
\biggr\rvert_{s = 0}
\end{align*}$$
2. Second, if $\xi_{1}, \dots, \xi_{n}$ are independent random variables having generating functions $\phi_{1}(s), \dots , \phi_{n}(s)$, respectively, then *the generating function of their sum $X = \xi_{1}+\dots + \xi_{n}$ is simply the product*
$$\begin{align*}
\phi_{X}(s) &= \phi_{1}(s) \phi_{2}(s)\dots \phi_{n}(s)
\end{align*}$$
Makes dealing with problems involving sums of independent random variables easier. Generating functions provide a major tool in the analysis of branching processes.

3. Third, *the moments of a nonnegative integer-valued random variable may be found by differentiating the generating function*.
Proof:
$$\begin{align}
\text{First derivative: } \frac{d \phi \left( s \right)}{d s} &= p_{1}+2p_{2}s+3p_{3}s^{2}+\dots \\
\frac{d \phi \left( s \right)}{d s}\biggr\rvert_{s = 1} &= p_{1}+2p_{2}+3p_{3}+\dots \\
&\equiv \sum\limits_{k=1}^{\infty} p_{k} \cdot k = \mathbb{E}\left[\xi\right]\\
\text{Second derivative } \frac{d^{2} \phi \left( s \right)}{d s^{2}} &= 2 p_{2}+3 \cdot 2 \cdot p_{3} s + 4 \cdot 3 \cdot p_{4}s^{2}+ \dots \\
\frac{d^{2} \phi \left( s \right)}{d s^{2}}\biggr\rvert_{s = 1} &= 2 p_{2}+3 \cdot 2 \cdot p_{3} + 4 \cdot 3 \cdot p_{4}+ \dots\\
&= \sum\limits_{k=2}^{\infty} k (k-1)p_{k} = \mathbb{E}\left[\xi \left( \xi-1 \right)\right] \\
&= \mathbb{E}\left[\xi^{2}\right] - \mathbb{E}\left[\xi\right]
\end{align}$$
Therefore,
$$\begin{align}
\mathbb{E}\left[\xi^{2}\right] &= \frac{d^{2} \phi \left( s \right)}{d s^{2}}\biggr\rvert_{s = 1} + \mathbb{E}\left[\xi\right] \\
&= \frac{d^{2} \phi \left( s \right)}{d s^{2}}\biggr\rvert_{s = 1} + \frac{d \phi \left( s \right)}{d s}\biggr\rvert_{s = 1}
\end{align}$$
and 
$$
\begin{align}
\operatorname{Var}\left[\xi\right] &= \mathbb{E}\left[\xi^{2}\right]- \left( \mathbb{E}\left[\xi\right] \right)^{2} \\
&= \frac{d^{2} \phi \left( s \right)}{d s^{2}}\biggr\rvert_{s = 1} + \frac{d \phi \left( s \right)}{d s}\biggr\rvert_{s = 1} - \left( \frac{d \phi \left( s \right)}{d s}\biggr\rvert_{s = 1} \right)^{2}
\end{align}
$$
## Generating Functions and Extinction Probabilities

Consider a branching process whose population size at stage $n$ is denoted by $X_{n}$. Assume that the offspring distribution $p_{k}=\operatorname{P} \left( \xi=k \right)$ has the generating function $\phi \left( s \right) = \mathbb{E}\left[s^{\xi}\right]=\sum\limits_{k=0}^{\infty}s^{k}p_{k}$.

If $u_{n}=\operatorname{P} \left( X_{n}=0 \right)$ is the probability of extinction by stage $n$, then the recursion $$u_{n}=\sum\limits_{k=0}^{\infty}p_{k}\left( u_{n-1} \right)^{k}, \quad n=1, 2, \dots$$
becomes (in terms of generating functions)
$$
\begin{align}
u_{n} &= \sum\limits_{k=0}^{\infty} p_{k} \left( u_{n-1} \right)^{k}\\
&= \phi(u_{n-1})
\end{align}
$$
Therefore, knowing the generating function $\phi(s)$, we may successively compute the extinction probabilities $u_{n}$ beginning with $u_{0}=0$ and then $u_{1}=\phi \left( u_{0} \right), u_{2}=\phi \left( u_{1} \right)$, and so on.
## Probability Generating Functions and Sums of Independent Random Variables

