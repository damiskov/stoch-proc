
- A *Poisson point process* $N \left( (s, t] \right)$ counts the number of events occurring in an interval $(s, t]$.
- A *Poisson counting process*, or more simply a *Poisson process* $X(t)$, counts the number of events occurring up to time $t$.
$$X(t) = N \left( (0, t] \right)$$
Poisson events occurring in space are best modelled as a point process. For Poisson events occurring on the positive time, the usage of point processes or counting process is a matter of convenience. 


## Waiting and Soujorn Times

![[Pasted image 20240923114005.png|center|600]]
### Waiting Times

For a Poisson process $W_{n}$ is the time of occurrence of the nth event. $W_{0}$ is always set to $0$. 

#### Theorem 5.4 - Gamma Distribution of Waiting Times

The waiting time $W_{n}$ has the gamma distribution, whose probability density function is 
$$\begin{align}
f_{W_{n}}(t) &= \frac{\lambda^{n} t^{n-1}}{(n-1)!}\exp{\left( - \lambda t \right)}, \quad n=1,2, \dots , t \geq 0
\end{align}$$
Looking at $W_{1}:$
$$\begin{align}
f_{W_{1}}(t) &= \frac{\lambda}{0!} \exp{\left( -\lambda t \right)}\\
&= \lambda \exp{\left( -\lambda t \right)}
\end{align}$$
So, *the time to the first event is exponentially distributed.*

### Sojourn Times 

The Soujorn times are defined as the differences between consecutive waiting times. Formally,
$$S_{n}= W_{n}-W_{n-1}$$
We say that $S_{n}$ measures the duration that a Poisson process *sojourns* in state $n$.

#### Theorem 5.5 - Exponential Distribution of Sojourn Times

The Sojourn times $S_{0}, S_{1}, \dots , S_{n-1}$ are independent random variables, each having the exponential probability density function

$$\begin{align}
f_{S_{k}}(s) &= \lambda \exp{\left( -\lambda s  \right)}, \quad s \geq 0
\end{align}$$
## The Binomial Distribution in a Poisson Process

### Theorem 5.6 - Looking into the Past

Let $\left\{ X(t) \right\}$ be a Poisson process of rate $\lambda > 0$. Then for $0 < u < t$ and $0 \leq k \leq n$ 
$$
\operatorname{P} \left( X(u) = k \mid X(t) = n \right) = \frac{n!}{k! (n-k)!} \left( \frac{u}{t} \right)^{k} \left( 1-\frac{u}{t} \right)^{n-k}
$$
