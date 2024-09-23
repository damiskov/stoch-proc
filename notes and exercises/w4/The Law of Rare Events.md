This section simply defines Poisson processes, but in terms of the number of occurrences within an interval.


The Poisson distribution occurs commonly in nature. This occurrence is explained by the *law of rare events.* 

The law asserts that: Where a certain event may occur in a large number of possibilities, but where the probability of this event occurring is small, then the total number of events that do happen approximately follow a Poisson distribution.

More, formally

### The Law of Rare Events

- Consider a large number of $N$ independent Bernoulli/Binomial trials 
- Probability of success $p$ on each trial is small and constant from trial to trial.
- Let $X_{N, p}$ denote the total number of success in the $N$ trials.
- $X_{N, p}$ follows the binomial distribution
$$\begin{align}
\operatorname{P} \left( X_{N, p}=k \right) &= \frac{N!}{k! (N-k)!}p^{k}(1-p)^{N-k}, \quad \text{for } k=0, \dots , N
\end{align}$$
Consider the limiting case $N \rightarrow \infty$ and $p \rightarrow 0$, in such a way that $N p = \mu > 0$. The distribution for $X_{N,p}$ becomes the Poisson distribution
$$\begin{align}
\operatorname{P} \left( X_{\mu}=k \right) &= \frac{\exp{\left( -\mu \right) \mu^{k}}}{k!}
\end{align}$$
## The Law of Rare Events and Poisson Processes

**Definition**