# Definitions 

## Markov Process

A *Markov process* $\left\{ X_{t} \right\}$ is a stochastic process with the property that, given the value of $X_{t}$, the values of $X_{s}$ for $s > t$ are not influenced by the values of $X_{u}$ for $u < t$.

I.e., The probability of any particular future behaviour of the process, when its current state is known exactly, is not altered by additional knowledge concerning its past behaviour. **Future behaviour is only dependent on current state. Not prior history.**

## Markov Chain

A *discrete-time Markov chain* is a Markov process whose *state space* is a finite/countable set, with time index $T = \left( 0, 1, \dots  \right)$. Defined formally 

$$
\begin{align}
&\operatorname{Pr} \left\{ X_{n+1} =  j \ \vert \ X_{0}= i_{0}, \dots ,\ X_{n-1}= i_{n-1}, \ X_{n}=i\right\} \\
&= \operatorname{Pr} \left\{ X_{n+1} = j \ \vert \ X_{n}= i\right\} 
\end{align}
$$
^markov-property

for all time points $n$ and all states $i_{0}, \dots , i_{n-1}, i, j$. ^8349f6

## One-Step Transition Probability

The probability of $X_{n+1}=j$ given that $X_{n}=i$  is called the *one-step transition probability* and is denoted by $P_{ij}^{n, n+1}$. That is,

$$P_{ij}^{n,n+1} = \operatorname{Pr} \left\{ X_{n+1}=j \vert X_{n}=i \right\}$$
- Transitions are functions of initial, final states and time of transition.
- When transition probabilities are independent of the time variable $n$, we say that the Markov chain has *stationary transition probabilities*.
	- $P_{ij}^{n,n+1}=P_{ij}$ is independent of $n$, and $P_{ij}$ is simply a conditional probability.

## Transition Probability Matrix

Customary to arrange the numbers $P_{ij}$ in a matrix.

$$\mathbf{P} = \begin{bmatrix}  P_{00} & P_{01} & \cdots  \\ P_{10} & P_{11} &\cdots  \\  \vdots & \vdots &  \\ P_{i0} & P_{i1} & \cdots  \\ \vdots & \vdots &  \end{bmatrix}$$
 Here, $\mathbf{P} = \Vert P_{ij} \Vert$ is the *Markov matrix* or *transition probability matrix*. 

The $i$th row of $\mathbf{P}$, for $i = 0, 1, \dots ,$ is the probability distribution of the values of $X_{n+1}$ under the condition that $X_{n}=i$. The quantities $P_{ij}$ satisfy the conditions 
$$\begin{align}
P_{ij} &\geq 0, \quad \text{for } i,j=0,1,2,\dots , \\
\sum\limits_{j=0}^{\infty}P_{ij} &= 1, \quad \text{for } i, j = 0,1, \dots , 
\end{align}$$
# Transition Probability Matrices of a Markov Chain

A Markov chain is completely defined by its one-step transition probability matrix and the specification of a probability distribution on the state of the process at time $0$. 

## n-step Transition Probability Matrices

$$\mathbf{P}^{\left( n \right)}= \left\Vert P_{ij}^{\left( n  \right)} \right\Vert$$
Here, $P_{ij}^{(n)}$ denotes that the process goes from state $i$ to $j$ in $n$ transitions. Formally,
$$P_{ij}^{(n)} = \operatorname{Pr} \left\{ X_{m+n} = j \ \vert \ X_{m}=i \right\}$$
- Still only dealing with stationary transition probabilities.

### Theorem 3.1

*The n-step transition probabilities of a Markov chain satisfy*
$$P_{ij}^{\left( n \right)} = \sum\limits_{k=0}^{\infty}P_{ik}P_{kj}^{(n-1)}$$
*where we define*
$$P_{ij}^{(0)} = \begin{cases} 1 & \text{if } i = j \\ 0 & \text{if } i \neq j \end{cases}$$
We can see that this is essentially just matrix multiplication $\mathbf{P}^{(n)}= \mathbf{P} \times \mathbf{P}^{(n-1)}$.

I.e., the $n$-step transition probabilities $P_{ij}^{\left( n \right)}$ are the entries in the matrix $\mathbf{P}^{n}$, the $n$th power of $\mathbf{P}$.


# Markov Chain Models

Markov chains are used to quantify a large number of phenomena that can be described by them.

## Inventory Model

- A commodity is stocked in order to meet certain demand.
- Replenishment of stock takes place at the end of period $n=0, 1, 2, \dots ,$
- Total demand for commodity in period $n$ is $\xi_{n}$, whose distribution function is independent of time period (stationary)

$$\operatorname{Pr} \left\{ \xi_{n} = k \right\}=a_{k}, \quad \text{for } k=0,1,2,\dots , $$
Where $a_{k} \geq 0$ and $\sum\limits_{k=0}^{\infty}a_{k}=1$. 
- Replenishment policy is prescribed by specifying two nonnegative critical numbers $s$ and $S > s$
	- If $X_{n}$ (stock at $n$) is less than $s$ $\implies$ Amount of stock $S-X_{n}$ is procured (stock reaches $S$) .
	- else, no replenishment occurs.

The states of the process $\left\{ X_{n} \right\}$ consist of the possible values of stock size
$$S, S-1, \dots , +1, 0, -1, -2, \dots , $$
Where negative values indicate an unfulfilled demand which will be fulfilled immediately upon restocking.

The stock levels at two consecutive periods are connected by the relation
$$X_{n+1} = \begin{cases} X_{n}-\xi_{n+1} & \text{if } s < X_{n} \leq S,  \\ 
 S-\xi_{n+1}  & \text{if } X_{n} \leq s,
 \end{cases}$$
 Where $\xi_{n}$ is the quantity demanded in the $n$th period.

If we assume that two successive demands are independent random variables, then the stock values $X_{0}, X_{1}, X_{2}, \dots$ constitute a Markov chain whose transition probability matrix can be calculated in accordance with the above relation. More explicitly,

$$\begin{align}
P_{ij} &= \operatorname{Pr} \left\{ X_{n+1} = j \ \vert \ X_{n}=i \right\}\\
&= \begin{cases} \operatorname{Pr} \left\{ \xi_{n+1}=i-j \right\}  &  \text{if } s < i \leq S \\
\operatorname{Pr} \left\{ \xi_{n+1} = S-j  \right\}  &  \text{if } i \leq s \end{cases} 
\end{align}$$
Consider a spare parts inventory with either $0, 1$ or $2$ repair parts demanded in any given period with probabilities
$$\operatorname{Pr} \left\{ \xi_{n}=0 \right\} = 0.5, \quad \operatorname{Pr} \left\{ \xi_{n}=1 \right\} = 0.4, \quad \operatorname{Pr} \left\{ \xi_{n}=2 \right\} = 0.1$$
and that $s=0$ and $S=2$.

The possible states therefore are $\left\{ 2,1,0,-1 \right\}$. We get the following transition probability matrix

$$\mathbf{P} = \begin{bmatrix} 0  & 0.1 & 0.4 & 0.5  \\ 0  & 0.1 & 0.4 & 0.5  \\ 0.1  & 0.4 & 0.5 & 0  \\ 0 & 0.1 & 0.4 & 0.5 \end{bmatrix}$$
Example: suppose $X_{n}=1$. No replenishment takes place. The probability that the demand $\xi_{n+1} = 2$ is $\operatorname{Pr} \left\{ \xi_{n+1}=2 \right\}=0.1$. Therefore, the probability that the inventory quantity will transition from $1 \rightarrow -1$ is $\operatorname{Pr} \left\{ X_{n+1}=-1 \ \vert \ X_{n}=1 \right\}=0.1$. Hence, $\mathbf{P}_{1,-1}=0.1$. (Note that the indices have been changed to reflect the Markov states $\left\{ 0,1,2,3 \right\} \rightarrow \left\{ -1,0,1,2 \right\}$).

# First Step Analysis

Method proceeds by analysing the possibilities that can arise at the end of the first transition, and then invoking the law of total probability $(P(A) = \sum\limits_{n}^{} P(A \cap B_{n}))$ coupled with the [[#^8349f6|Markov property]] to establish a relationship among the unknown variables.

## Simple First Step Analysis

Consider the following Markov chain $\left\{ X_{n} \right\}$ with transition probability matrix

|     | 0        | 1       | 2        |
| --- | -------- | ------- | -------- |
| 0   | 1        | 0       | 0        |
| 1   | $\alpha$ | $\beta$ | $\gamma$ |
| 2   | 0        | 0       | 1        |
We can see that process gets trapped in states $0$ and $2$. But which state does it get trapped in and how long on average does it take to reach one of these states?

More formally,

$$T = \min \left\{ n \geq 0; X_{n}= 0 \text{ or } X_{n} = 2\right\}$$
is the time of absorption of the process. In terms of this *random absorption time*, we must find 
$$u = \operatorname{Pr} \left\{ X_{T}= 0 \vert X_{0}=1 \right\}$$
and
$$\nu = \mathbb{E} \left[T \vert X_{0}=1\right]$$
Procedure:

Considering the three different states after one step $X_{1}=0, X_{1}=1, X_{1}=2$, with respective probabilities $\alpha, \beta, \gamma$.

Claim the following:
- $\operatorname{Pr} \left\{ X_{t}=0 | X_{1}=0 \right\} =1$
- $\operatorname{Pr} \left\{ X_{t}=0 | X_{1}=2\right\} =0$
- $\operatorname{Pr} \left\{ X_{t}=0 | X_{1}=1 \right\} =u$

Inserting into the law of total probability

$$\begin{align}
u &= \operatorname{Pr} \left\{ X_{t}=0 | X_{0}=1 \right\}\\
&= \sum\limits_{k=0}^{2} \operatorname{Pr} \left\{ X_{t}=0 | X_{0}=1, X_{1}=k \right\} \operatorname{Pr} \left\{ X_{1}=k| X_{0}=1 \right\} \\
&= \sum\limits_{k=0}^{2} \operatorname{Pr} \left\{ X_{t}=0 |X_{1}=k \right\} \operatorname{Pr} \left\{ X_{1}=k| X_{0}=1 \right\}  \\
&= 1 \cdot \alpha + u \cdot \beta + 0 \cdot \gamma
\end{align}$$
Which gives us the equation
$$\begin{align}
u &= \alpha + \beta u \\\\
	\implies u &= \frac{\alpha}{1-\beta} = \frac{\alpha}{\alpha+ \gamma}
\end{align}$$

Determining mean time for absorption:

$$\nu= \mathbb{E} \left[T | X_{0}=1\right]$$
Absorption time is always at least 1. If either $X_{1}=0$ or $X_{1}= 2$, no further steps are required. If $X_{1}=1$, then the process is back at its starting point, and on average $\nu=\mathbb{E} \left[T|X_{0}=1\right]$ steps are required for absorption. These components are weighted by their respective probabilities:

$$\begin{align}
\nu &= 1 + \alpha \cdot 0 + \beta \cdot \nu + \gamma \cdot 0 \\
&= 1 + \beta \nu
\end{align}$$
Giving
$$\nu = \frac{1}{1- \beta}$$


# Lecture Notes

## Recap of Probability

**Probability triple:** $\left( \Omega, \mathcal{F}, P \right)$

- $\omega \in \Omega$ 
- Sets of $\omega \rightarrow \mathcal{F}$ (Events e.g, $A, B, \dots$)  ($\mathcal{F}$ and $\mathcal{A}$ interchangeable)
- Set of events constitute a $\sigma$-algebra
	- $\Omega \in \mathcal{A}$ 
	- $A \in \mathcal{A} \implies A^{c} \in \mathcal{A}$
	- $A_{i} \in \mathcal{A} \implies\bigcup_{i}^{\infty} A_{i} \text{ (countable union) }\in \mathcal{A}$

Borel-algebra: *smallest* $\sigma$-algebra containing all open sets.

What is a probability? 
- $P: \  A \in \mathcal{A} \mapsto \left[0, 1\right]$
	- $P(\Omega) = 1$
	- $A_{i} \in \mathcal{A}: \ i \neq j \implies A_{i} \cap A_{j}= \emptyset$ (Mutually exclusive)
	- $P(\bigcup_{i} A_{i}) = \sum\limits_{i}^{}P(A_{i})$

$$
P \left( A \cap B \right) \leq P(A) \implies \exists c \in \left[0, 1\right]: \ P(A \cap B) = c \cdot P(A)
$$
**Conditional probability:**
$$\begin{align}
c = \frac{P \left( A \cap B \right)}{P \left( A \right)}= P(B|A)
\end{align}$$
- Division by $P(A)$ can be thought of a *renormalisation* of the sample space $\Omega$ (to only include $A$)

**Independence:**

$$P \left( B \vert A \right) = P(B)$$

Knowing something about $A$ does not influence the probability of event $B$.

**Partitioning:**

For mutually exclusive events $A_{i}, \ i = 1, \dots$
$$\bigcup_{i}A_{i}= \Omega$$
Law of total probability 
$$P(B) = \sum\limits_{i}^{}P(A_{i})P(B|A_{i}) = \sum\limits_{i}^{}P(B \cap A_{i})$$

$$\begin{align}
P(A \cap B \cap C) &= P(C | A \cap B)P(A \cap B) \\
&= P(C|A \cap B)P(B|A) P(A)
\end{align}$$
**Random variables:**

- A mapping $X: \ \Omega \mapsto \mathbb{R}$
- $P \left( \left\{ \omega \vert \ X \left( \omega \right) = x \right\} \right) = P(X=x) =f (x)$ *probability mass function*
- $P(X \leq x) =P \left( \left\{ \omega \vert X \left( \omega \right) \leq x \right\} \right) = \sum\limits_{t \leq x}^{} f(t) = F(x)$ *cumulative distribution function*

Finite set of random variables $\implies$ multivariate distribution

Stochastic processes deal with infinite sequences of random variables.

**Markov Chains**

$$\left\{ X_{n}; \ n \in \mathbb{N} \right\} $$
Frog example:
$$\begin{align}
X_{n}&: \text{ Position of frog at } t = n\\
X_{n} &\in  S \text{ possible states}
\end{align}$$
Markov property:
$$\begin{align}
&\operatorname{P} \left\{ X_{n+1} =  j \ \vert \ X_{0}= i_{0}, \dots ,\ X_{n-1}= i_{n-1}, \ X_{n}=i\right\} \\
&= \operatorname{Pr} \left\{ X_{n+1} = j \ \vert \ X_{n}= i\right\} 
\end{align}$$
Time-homogeneous processes *stationary transition probabilities*
$$P \left( X_{n+1} = j | X_{n} = i \right) = P(X_{1}=j | X_{0}=i) = p_{ij}$$
Matrix notation:
$$\mathbf{P} = \left\Vert p_{ij} \right\Vert$$
What happens with 

$$P_{ij}^{\left( n \right)} = \sum\limits_{k \in S}^{}P(X_{n}=j, X_{1}=k |X_{0}=i)$$
? Make a partitioning
$$= \sum\limits_{k \in S}^{} P \left( X_{n}=j | X_{0}=i, X_{1}=k \right)P(X_{1}=k | X_{0}=i)$$
Apply Markov property
$$\begin{align}
&= \sum\limits_{k \in S}^{} P \left( X_{n}=j | X_{1}=k \right)P(X_{1}=k | X_{0}=i ) \\
\end{align}$$
Using *time-homogeneity* property
$$\begin{align}
&= \sum\limits_{k \in S}^{} P \left( X_{n-1}=j | X_{0}=k \right)P(X_{1}=k | X_{0}=i ) \\
\end{align}$$
And then re-writing in terms of $p_{ij}$
$$\begin{align}
&= \sum\limits_{k \in S}^{} p_{kj} p_{ik} \\
&= p_{ij}^{n}
\end{align}$$
## First-step analysis

### Probability of Absorption in state $k$

$$\begin{align}
u_{i} &= \operatorname{P} \left( \text{Absorption in } k \mid X_{0}=i \right) \\
&= \sum\limits_{j=0}^{N} \operatorname{P} \left( \text{Absorption in } k \mid X_{0}=i, X_{1}=j \right) P_{ij}\\
&= P_{ik}+\sum\limits_{j=r, j \neq k}^{N} P_{ij} \times 0 + \sum\limits_{j=0}^{r-1} P_{ij}u_{j}
\end{align}$$
In summary, for a fixed absorbing state $k$, the quantities
$$u_{i}=U_{ik}=\operatorname{P} \left( \text{Absorption in } k \mid X_{0}=i \right) \quad \text{for } 0 \leq i < r$$
satisfy the inhomogeneous system of linear equations 
$$
\mathrm{U}_{ik}=\mathrm{P}_{ik}+\sum\limits_{j=0}^{r-1}\mathrm{P}_{ij} \mathrm{U}_{jk}, \quad i=0, 1, \dots , r-1
$$
### Mean Number of Visits

Random absorption time
$$T = \min \left\{ n \geq 0 ; \ X_{n} \geq r \right\}$$
Mean total rate
$$w_{i} = \mathbb{E} \left[\sum\limits_{n=0}^{T-1} g \left( X_{n} \right) \mid X_{0}=i\right]$$
The choice $g(i)=1$ for all $i$ yields $\sum\limits_{n=0}^{T-1}g \left( X_{n} \right) = \sum\limits_{n=0}^{T-1} 1 = T$, which would make $w_{i}$ identical to $\nu_{i} \equiv \mathbb{E}\left[T \mid X_{0}=i\right]$. For a transient state $k$, the choice
$$
g(i) = \begin{cases} 1 & \text{if } i = k \\
0  &  \text{if } i \neq k \end{cases}
$$
gives $w_{i} = \mathrm{W}_{ik}$, the mean number of visits to state $k$ $\left( 0 \leq k < r \right)$ prior to absorption. Proceeding with first step analysis

The sum $\sum\limits_{n=0}^{T-1} g \left( X_{n} \right)$ always includes the first term $g \left( X_{0} \right) = g(i)$.
- If a transition is made from $i$ to a transient state $j$, then the sum includes future terms as well.
- Through the Markov property we can deduce that this future sum proceeding from state $j$ has an expected value equal to $w_{j}$
- This is then weighted by the corresponding transition probability $\mathrm{P}_{ij}$
- All the contributions are then summed in accordance with the law of total probability.

The joint relations can be obtained
$$w_{i}=g(i) + \sum\limits_{j=0}^{r-1} \mathrm{P}_{ij}w_{j} \quad \text{for } i=0, \dots , r-1$$
The special case in which $g(i)=1$ for all $i$ determines $\nu_{i}=\mathbb{E}\left[T \mid X_{0}=i\right]$ as solving 
$$\nu_{i}=1 + \sum\limits_{j=0}^{r-1}\mathrm{P}_{ij}\nu_{j}, \quad \text{for } i =0,1,\dots , r-1$$
The case in which 
$$g(i) = \delta_{ik}=\begin{cases} 1 & \text{if } i=k, \\
0 & \text{if } i \neq k \end{cases}$$
determines $W_{ik}$, the mean number of visits to state $k$ prior to absorption starting from state $i$, as solving
$$
\mathrm{W}_{ik}=\delta_{ik}+\sum\limits_{j=0}^{r-1} \mathrm{P}_{ij} \mathrm{W}_{jk}
$$

### Law of Total Probability

For mutually exclusive events $A_{i}, \ i = 1, \dots$
$$\bigcup_{i}A_{i}= \Omega$$
Law of total probability 
$$P(B) = \sum\limits_{i}^{}P(A_{i})P(B|A_{i}) = \sum\limits_{i}^{}P(B \cap A_{i})$$

$$\begin{align}
P(A \cap B \cap C) &= P(C | A \cap B)P(A \cap B) \\
&= P(C|A \cap B)P(B|A) P(A)
\end{align}$$