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