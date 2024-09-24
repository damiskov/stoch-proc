
A model for fluctuations in electrical currents, due to chance arrival of electrons to an anode. 
## Assumptions
1. Electrons arrive at an anode according to a *Poisson process* $\left\{ X(t); t \geq 0 \right\}$ of constant rate $\lambda$.
2. An arriving electron produces a current whose intensity $x$ time units after arrival is given by the impulse response function $h(x)$.
## Model

### Shot Noise

The intensity of the current at time $t$ is, then, *the shot noise*
$$
I(t) = \sum\limits_{k=1}^{X(t)} h(t-W_{k})
$$
where $W_{1}, W_{2}$ are the arrival times of the electrons.

Where $h$ can take various forms. We consider the *power law* shot noise 
$$h(x)=x^{-\theta}, \quad \text{for } x >0$$
#### Target in Proof

Will attempt to demonstrate that, *for a fixed time point* $t$, the shot noise $I(t)$ has the same probability distribution as the following *random sum*

- Let $U_{1}, U_{2}, \dots$ be independent random variables, uniformly distributed over $(0, t]$ and independent of the Poisson process.
- **Define: $\epsilon_{k}=h(U_{k})$ for $k=1,2,\dots$**

We claim that the shot noise has the $I(t)$ has the same probability distribution as the random sum
$$S(t)=\epsilon_{1}+\dots+\epsilon_{X(t)}$$
Now proceed calculating the mean, variance and distribution of the shot noise $I(t)$ using the techniques from [[Random Sums|week 2]].

#### Expectation of Random Sum

$$\begin{align}
\mathbb{E} \left[I(t)\right] &= \mathbb{E} \left[S(t)\right] \\
&= \lambda t \mathbb{E} \left[h (U_{1})\right]\\
&= \lambda \int_{0}^{t} h(u) du
\end{align}$$
#### Variance of Random Sum
 $$\begin{align}
\operatorname{Var} \left[I(t)\right] &= \lambda t \left\{ \operatorname{Var} \left[ h (U_{1})\right]+\mathbb{E}\left[h(U_{1})\right]^{2} \right\}, \quad \text{(Not sure how this is derived?)}\\
&= \lambda t \mathbb{E} \left[h \left( U_{1} \right)^{2}\right]\\
&= \lambda \int_{0}^{t} h(u)^{2}du
\end{align}$$

#### Proof that Shot Noise shares the same distribution as a random sum

- Need to show that $\operatorname{P} \left( I(t) \leq x \right) = \operatorname{P} \left( S(t) \leq x \right)$ for a fixed $t>0$ and arbitrary $x$.

Start with,
$$\begin{align}
\operatorname{P} \left( I(t) \leq x \right) &= \operatorname{P} \left( \sum\limits_{k=1}^{X(t)} h(t-W_{k}) \leq x \right) 
\end{align}$$
Make a very similar step as in the [[The Uniform Distribution and Poisson Processes#Example - Customers|customers example]] (although $n$ can start at 0)
$$\begin{align}
&= \sum\limits_{n=0}^{\infty} \operatorname{P} \left( \sum\limits_{k=1}^{n} h(t-W_{k}) \leq x \mid X(t)=n\right)\cdot \operatorname{P} \left( X(t)=n \right) \\
\end{align}$$
We now invoke [[The Uniform Distribution and Poisson Processes#Theorem 5.7|theorem 5.7]]
$$\begin{align}
&= \sum\limits_{n=0}^{\infty} \operatorname{P} \left( \sum\limits_{k=1}^{n} h(t-U_{k}) \leq x\right)\cdot \operatorname{P} \left( X(t)=n \right) \\
\end{align}$$
and, due to symmetry ($U_{k}$ and $t-U_{k}$ have the same symmetry)
$$\begin{align}
&= \sum\limits_{n=0}^{\infty} \operatorname{P} \left( \sum\limits_{k=1}^{n} h(U_{k}) \leq x\right)\cdot \operatorname{P} \left( X(t)=n \right) \\
&= \sum\limits_{n=0}^{\infty} \operatorname{P} \left( \epsilon_{1}+\cdots+\epsilon_{n} \leq x  \right) \cdot \operatorname{P} \left( X(t)=n \right) \\
&= \operatorname{P} \left( \epsilon_{1}+\cdots+\epsilon_{X(t)} \leq x \right)\\
&= \operatorname{P} \left( S(t) \leq x \right)
\end{align}$$
Completing the claim.

