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

