## The Poisson Distribution

Given a parameter $\mu > 0$, the *Poisson distribution* is given by
$$p_{k} = \frac{\exp{\left( - \mu \right) \mu^{k}}}{k!}, \quad \text{for } k = 0, 1, 2, \dots$$
### Mean of the Poisson Distribution
Let $X$ be a stochastic variable having the Poisson distribution
$$\begin{align}
\mathbb{E} \left[X\right]&= \sum\limits_{k=0}^{\infty} k p_{k} \\
&= \sum\limits_{k=0}^{\infty} k \cdot \frac{\exp{\left( - \mu \right) \mu^{k}}}{k!} \\
&=  \sum\limits_{k=1}^{\infty} \frac{k \cdot \exp{\left( - \mu \right) \mu^{k}}}{k!} \\
&= \sum\limits_{k=1}^{\infty} \frac{k}{k \times  (k-1) \times  \cdots \times  1} \cdot \exp{\left( - \mu \right)} \cdot \mu^{k} \\
&= \exp{\left( -\mu \right)} \sum\limits_{k=1}^{\infty} \frac{1}{(k-1)!} \cdot \mu \cdot \mu^{k-1}\\
&= \mu \cdot \exp{\left( - \mu \right)} \sum\limits_{k=1}^{\infty} \frac{\mu^{k-1}}{(k-1)!}
\end{align}$$
Using the definition of $\exp{\left( x \right)} = \sum\limits_{k=0}^{\infty} \frac{x^{k}}{k!}$, we have 
$$\begin{align}
&= \mu \cdot \exp{\left( -\mu \right)} \cdot \exp{\left( \mu \right)}\\
&= \mu
\end{align}$$
### Variance of Poisson Distribution

We first determine
$$\begin{align}
\mathbb{E}\left[X(X-1)\right] &= \sum\limits_{k=2}^{\infty} k (k-1) p_{k}\\
&= \mu^{2} \exp{\left( -\mu \right)} \sum\limits_{k=2}^{\infty} \frac{\mu^{k-2}}{(k-2)!}\\
&= \mu^{2} 
\end{align}$$
Then 
$$\begin{align}
\mathbb{E} \left[X^{2}\right] &=\mathbb{E}\left[X(X-1)\right] + \mathbb{E}\left[X\right] \\
&= \mu^{2}+\mu
\end{align}$$
Using the definition of variance
$$\begin{align}
\sigma_{X}^{2}&= \operatorname{Var} \left[X\right]= \mathbb{E} \left[X^{2}\right] - \left\{ \mathbb{E} \left[X\right] \right\}^{2}\\
&= \mu^{2}+\mu-\mu^{2}\\
&= \mu
\end{align}$$
### Theorem 5.1 - Sum of Poisson Distributions

- Let $X$ and $Y$ by independent random variables having Poisson distributions with parameters $\mu$ and $\nu$, respectively.
- The *sum* $X+Y$ is also poisson distributed with parameter $\mu+\nu$.

#### Proof

### Theorem 5.2 - Unconditional Distribution

- $N$ is a Poisson random variable, with parameter $\mu$ which is also conditional on $N$. 
- $M$ is a binomially distributed variable, with parameters $N$ and $p$. 
- The *unconditional* distribution of $M$ is Poisson distributed with parameter $\mu p$.

#### Proof

## The Poisson Process

**Definition:** A Poisson process of *intensity/rate* $\lambda > 0$ is an integer-valued stochastic process $\left\{ X(t); t \geq 0 \right\}$ for which

1. For any time points $t_{0}=0 < t_{1}, t_{2} < \dots < t_{n}$, *the process increments*
$$X(t_{1})-X(t_{0}),\ X(t_{2})-X(t_{1}), \dots , \ X(t_{n})-X(t_{n-1})$$
*are independent, random variables.*

2. For $s \geq 0$ and $t > 0$, the random variable $X(s+t)-X(s)$ has the Poisson distribution

$$\operatorname{P} \left( X (s+t)-X(s)=k \right) = \frac{(\lambda t)^{k} \exp{\left( - \lambda t \right)}}{k!}, \quad \text{for } k=0,1,2,\dots$$

3. $X(0)=0$

### Moments at $X(t)$

$$\mathbb{E}\left[X(t)\right] = \lambda t$$
and 
$$\operatorname{Var}\left[X(t)\right] = \sigma_{X(t)}^{2}=\lambda t$$

## Nonhomogeneous Processes

The *rate $\lambda$* in a Poisson process $X(t)$ is the *proportionality constant in the probability of an event occurring during an arbitrarily small interval. (h)*

More formally,

$$\begin{align}
\operatorname{P} \left( X(t+h)-X(t)=1 \right) &= \frac{\left( \lambda h \right) \exp{\left( - \lambda h \right)}}{1 !}\\
&= \left( \lambda h \right) \left( 1 - \lambda h + \frac{1}{2} \lambda^{2}h^{2}- \dots  \right)\\
&= \lambda h + o(h)
\end{align}$$
Many applications consider rates that vary with time. I.e, 
$$\begin{align}
\lambda &= \lambda(t)
\end{align}$$
This is known as a *nonhomogeneous* or *nonstationary* Poisson process. 


## Cox Processes 

