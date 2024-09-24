Summary: Major result [[The Uniform Distribution and Poisson Processes#Theorem 5.7|(theorem 5.7)]] asserts that, conditioned on a fixed total number of events in an interval, the locations of these events are uniformly distributed.

### Set Up
- Line segment $t$ units long.
- Fixed number $n$ of darts.
- Darts are thrown at line segment.
	- Dart's position is uniformly distributed.
	- Independent of each other.

Let $U_{1}$ be position of first dart thrown. $U_{2}$ is position of second dart (so on up to $U_{n}$).

The probability density function is the uniform density 
$$\begin{align}
f_{U}(u) &= \begin{cases} \frac{1}{t},  &  \text{for } 0 \leq u \leq t,\\
0  &  \text{elsewhere} \end{cases}
\end{align}$$
Now let $W_{1} \leq W_{2} \leq \cdots \leq W_{n}$ denote these same positions, not in the order in which they are thrown, but in the order in which they appear on the line segment.

![[Pasted image 20240924104745.png|center|600]]

The *joint probability density function* for $W_{1}, W_{2}, \dots , W_{n}$ is 
$$
\begin{align}
f_{W_{1}, \dots , W_{n}} \left( w_{1}, \dots , w_{n} \right) &= n!t^{-n}, \quad \text{for } 0 < w_{1}<w_{2}<\cdots<w_{n}\leq t
\end{align}
$$
For the case $n=2$, we have

$$\begin{align}
f_{W_{1}, W_{2}} \left( w_{1}, w_{2} \right) \Delta w_{1} \Delta w_{2} \\
&= \operatorname{P} \left( w_{1} < W_{1} \leq w_{1}+\Delta w_{1},  w_{2} < W_{2} \leq w_{2}+\Delta w_{2}\right) \\
&= \operatorname{P} \left( w_{1} < U_{1} \leq w_{1}+\Delta w_{1},  w_{2} < U_{2} \leq w_{2}+\Delta w_{2} \right) + \\
&\operatorname{P} \left( w_{1} < U_{2} \leq w_{1}+\Delta w_{1},  w_{2} < U_{1} \leq w_{2}+\Delta w_{2} \right)\\
&= 2 \left( \frac{\Delta w_{1}}{t} \right) \left( \frac{\Delta w_{2}}{t} \right)\\
&= 2 \cdot t^{-2} \Delta w_{1} \Delta w_{2}
\end{align}$$
$$\begin{align}
\text{Probability that distances of } W_{1}, W_{2} \text{ are within some range} = \\ \text{probability that either darts have landed in either location}
\end{align}$$
Dividing by $\Delta w_{1} \Delta w_{2}$ and passing the limit gives
$$
f_{W_{1}, W_{2}} \left( w_{1}, w_{2} \right) = 2! \cdot t^{-2}
$$
as expected.

### Theorem 5.7
- $W_{1}, W_{2}, \dots$ be the occurrence times in a *Poisson process* with rate $\lambda>0$.
- Conditioned on $N(t) = n,$ the random variables $W_{1}, W_{2}, \dots, W_{n}$ have the *joint probability density function*
$$
f_{W_{1}, \dots , W_{N} \mid X(t)=n} (w_{1}, \dots , w_{n}) = n! t^{-n}
, \quad \text{for } 0 < w_{1}<w_{2}<\cdots<w_{n}\leq t$$
### Example - Customers
- Customers arrive at facility with **Poisson rate of $\lambda$.**
- Each customer pays **$\$ 1$ on arrival.**
- We want to calculate the **expected value of sum collected during the interval $(0, t]$ discounted back to time $0$.**

Quantity to calculate is given by
$$\begin{align}
M &= \mathbb{E} \left[ \sum\limits_{k=1}^{X(t)} \exp{\left( -\beta W_{k} \right)}\right]
\end{align}$$
- $\beta$ is the discount rate.
- $W_{1}, W_{2}, \dots$ are the arrival times.
- $X(t)$ is the total number of arrivals in $(0, t]$.

We evaluate the mean total discounted sum $M$ by conditioning on $X(t)=n$. Then,
$$
M = \sum\limits_{n=1}^{\infty}\mathbb{E} \left[ \sum\limits_{k=1}^{n} \exp{\left( -\beta W_{k} \right)}\right] \cdot \operatorname{P} \left( X(t)=n \right)
$$
($n=1 \rightarrow \infty$ due to initial 1 dollar).Let $U_{1}, \dots , U_{n}$ denote independent random variables that are uniformly distributed on our segment $(0, t]$. 

Because of the symmetry of the functional $\sum\limits_{k=1}^{n}\exp{\left( - \beta W_{k} \right)}$ and [[The Uniform Distribution and Poisson Processes#Theorem 5.7|theorem 5.7]], we have
$$\begin{align}
\mathbb{E} \left[\sum\limits_{k=1}^{n} \exp{\left( - \beta W_{k} \right)} \mid X(t)=n\right] &= \mathbb{E} \left[\sum\limits_{k=1}^{n} \exp{\left( - \beta U_{k} \right)}\right], \quad \text{Convert to uniform dist.} \\
&= n \mathbb{E} \left[\exp{\left( -\beta U_{1} \right)}\right], \quad \text{Consequence of uniform dist.} \\
&= n t^{-1} \int_{0}^{t}\exp{\left( -\beta u \right)}du, \quad \text{Using uniform dist. } p(u)= \frac{1}{t}\\
&= \frac{n}{\beta t} \left[1- \exp{\left( -\beta t \right)}\right]
\end{align}$$
Substituting this into our expression for $M$
$$
\begin{align}
M &= \sum\limits_{n=1}^{\infty}\mathbb{E} \left[ \sum\limits_{k=1}^{n} \exp{\left( -\beta W_{k} \right)}\right] \cdot \operatorname{P} \left( X(t)=n \right)\\
&= \sum\limits_{n=1}^{\infty} \frac{n}{\beta t} \left[1- \exp{\left( -\beta t \right)}\right]  \operatorname{P} \left( X(t)=n \right)\\
&= \frac{1}{\beta t} \left[1- \exp{\left( -\beta t \right)}\right] \sum\limits_{n=1}^{\infty} n \operatorname{P} \left( X(t)=n \right)\\
&= \frac{\mathbb{E} \left[X(t)\right]}{t} \cdot \frac{1}{\beta} \cdot \left[1- \exp{\left( -\beta t \right)}\right] \\
&= \frac{\lambda}{\beta} \left[1- \exp{\left( -\beta t \right)}\right]
\end{align}
$$
