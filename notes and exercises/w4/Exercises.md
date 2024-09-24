# 5.1.1 - Basic Poisson Question
----
Defects occur along the length of a filament at a rate of $\lambda=2$ per foot. 

a) Calculate the probability that there are no defects in the first foot of the filament.

We know that, for a Poisson process of rate $\lambda$, the first moment is 
$$\mathbb{E}\left[X(t)\right] = \lambda t$$
We then use this to calculate the probability of this event, according to a Poisson distribution with $\mu=\lambda t$
$$\begin{align}
\operatorname{P} \left( X(1)=0 \right) &= \operatorname{P} \left( X(0+1)-X(0) = 0 \right) \\
&= \frac{\left( \lambda t \right)^{k} \exp{\left( - \lambda t \right)}}{k!}\\
&= \frac{(2 \cdot 1)^{0} \cdot \exp{\left( -2 \right)}}{0!}\\
&= \exp{\left( -2 \right)}\\
&\approx 0.135 \checkmark
\end{align}$$
b) Calculate the conditional probability that there are no defects in the second foot of the filament, given that the first foot contained a single defect.
$$\operatorname{P} \left( X(2)=0 \mid X(1)=1 \right)$$
Due to the definition of a Poisson process, we know that the process increments are independent. Thus, we can re-write the probability required as 
$$\begin{align}
\operatorname{P} \left( X(2)-X(1)=0 \mid X(1)-X(0)=1 \right)
\end{align}$$
Due to independence, the conditional probability is the same as the unconditional probability. We are finally able to write the probability as
$$\begin{align}
\operatorname{P} \left( X(2)-X(1)=0 \mid X(1)-X(0)=1 \right) &= \operatorname{P} \left(X(2)-X(1)=0  \right)
\end{align}$$
and solve accordingly
$$\begin{align}
\operatorname{P} \left(X(2)-X(1)=0  \right)  &= \frac{(2)^{0} \exp{\left( -2 \right)}}{0!} \\
&= \exp{\left( -2 \right)} \\
&\approx 0.135 \checkmark
\end{align}$$
# 5.3.2 - Radiation
-----
A radioactive source emits particles according to a Poisson process of rate $\lambda=2$ particles per minute.

a) What is the probability that the first particle appears some time after $3$ min, but before $5$ min.

More formally, this is asking us for the following probability
$$\operatorname{P} \left( 3 \leq W_{1} <5 \right)$$
Thus, we have to make use of the *exponentially distributed* first waiting time
$$
\begin{align}
f_{W_{1}}(t) &=  \lambda \exp{\left( -\lambda t \right)} \\
&= 2 \exp{\left( -2t \right)}
\end{align}
$$
and calculate the following 
$$\begin{align}
\operatorname{P} \left( 3 \leq W_{1} <5 \right) &= \int_{3}^{5} f_{W_{1}}(t) dt\\
&= 2 \int_{3}^{5}\exp{\left( -2t \right)}dt \\
&= 2 \cdot \left[\frac{\exp{\left( -2t \right)}}{-2}\right]_{3}^{5} \\
&= - \left( \exp{\left( -10 \right)} - \exp{\left( -6 \right)}\right)\\
&\approx 0.00243 \ \checkmark
\end{align}$$
b) What is the probability that exactly one particle is emitted in the interval from $3$ to $5$ minutes?

$$\begin{align}
\operatorname{P} \left( X(3+2) - X(3) = 1 \right) &= \frac{(2 \cdot 2)^{1} \cdot \exp{\left( -2 \cdot 2 \right)}}{1!}\\
&= 4 \exp{\left( -4 \right)}\\
&\approx 0.0733 \ \checkmark
\end{align}$$
# 5.4.1 - Mean of First Arrival Time
----
Let $\left\{ X(t); t>0 \right\}$ be a Poisson process of rate $\lambda$. Suppose it is known that $X(1)=n$. For $n=1,2,\dots$ determine the mean of the first arrival time $W_{1}$.

We know that the mean arrival time is exponential distributed in the following way
$$\begin{align}
f_{W_{1}}(t) &= \lambda \exp{\left( -\lambda t \right)}
\end{align}$$
We want to find $\mathbb{E}\left[W_{1}\right]$. Using the standard definition of expectation
$$\begin{align}
\mathbb{E}\left[x\right] &= \sum\limits_{i=1}^{\infty} x_{i} p(x=i)
\end{align}$$
we create an expression in terms of $W_{1}...$
$$\begin{align}
\mathbb{E}\left[W_{1}\right] &= \int_{t=0}^{\infty} X(1) \cdot \lambda \exp{\left( -\lambda t \right)} dt\\
&= n \lambda \int_{t=0}^{\infty} \exp{\left( -\lambda t \right)} dt\\
&= n  \lambda \frac{1}{-\lambda} \left[\exp{\left( -\lambda \cdot \infty \right)} - \exp{\left( -\lambda \cdot 0 \right)}\right]\\
&= n \cdot \exp{\left( 0 \right)}\\
&= n \ \times 
\end{align}$$
## 5.4.1 - Re-do
- Need to use $f_{W} \left( w \mid X(t)=n \right)=n! t^{-n}$ and apply $\mathbb{E}\left[W_{1} \mid X(1)=n\right]$
