# Notation and Elements of Probability Theory

A probability space is defined as a triple $\left( \Omega, \mathcal{F}, \mathbb{P} \right)$:
- $\Omega:$ The sample space. I.e., set of all possible outcomes.
	- $w \in \Omega$
	- E.g., The sample space of a coin toss is $\Omega = \left\{ H, T \right\}$
- $\mathcal{F}:$ The set of events, $A \in \mathcal{F} \implies A \subset \Omega$
	- *The set of outcomes of an experiment*
	- This is a $\sigma-$algebra.
- $\mathbb{P}:$ The probability measure, $A \in \mathcal{F} \implies \mathbb{P}\left( A \right) \in \left[0, 1\right]$
	- *a [real-valued function](https://en.wikipedia.org/wiki/Real-valued_function "Real-valued function")defined on a set of events in a [σ-algebra](https://en.wikipedia.org/wiki/%CE%A3-algebra "Σ-algebra") that satisfies [measure](https://en.wikipedia.org/wiki/Measure_(mathematics) "Measure (mathematics)")properties* \

- Random variables.
- Distribution functions.
- Condtitioning.
# The Set-Up of Probability Theory
- We perform a *stochastic experiment*.
- $w$ is used to denote the outcome.
- The **sample space** $\Omega$ is the set of all possible outcomes,

## The Sample Space

$\Omega$ can be a very simple set. E.g., 

- $\left\{ H, T \right\}$ tossing a coin (Bernoulli experiment).
- $\left\{ 1,2,3,4,5,6 \right\}$, throwing a die once.
- $\mathbb{N}$, for single discrete stochastic variables.
- $\mathbb{R}^{d}$, multivariate continuous stochastic variables.

Or a more complicated set, e.g.,
- The set of all functions $\mathbb{R} \rightarrow \mathbb{R}^d$ with some regularity properties.

Often times it will not be needed to specify what $\Omega$ is.
## Events
Sets of outcomes/subsets of $\Omega$. Correspond to statements about the outcome. E.g.,  for a die thrown once, the event
$$A = \left\{ 1,2,3 \right\}$$
Corresponds to the statement *"The die showed no more than three."*
## Probability
**A Probability is a set measure of an event.** If $A$ is an event then 
$$\mathbb{P}(A)$$
Is the probability that the event $A$ occurs in the stochastic experiment - a number between $0$ and $1$. 
## Logical Operators as Set Operators
Which events are measurable (can have a probability assigned to them).

If $A$ and $B$ are legal statements represented by measurable subsets of $\Omega$. then so are

- Not $A$, i.e., $A^{c}=\Omega \backslash A$ 
- $A$ or $B$, i.e., $A \cup B$
## Statements and Sets

| Set                              | Statement                                |
| -------------------------------- | ---------------------------------------- |
| $A$                              | "The event $A$ has occurred" $(w \in A)$ |
| $A^c$                            | Not $A$                                  |
| $A \cap B$                       | $A$ and $B$                              |
| $A \cup B$                       | $A$ or $B$                               |
| $(A \cup B)\backslash(A \cap B)$ | $A$ exclusive-or $B$                     |

## An infinite, yet countable number of statements
If $A_{i}$ are events for $i \in \mathbb{N}$, then so is $\bigcup_{i \in \mathbb{N}} A_{i}$.
- A set is said to be countable, if you can make a list of its members. **The natural numbers are themselves countable - you can assign each integer to itself**.
## All Events Considered form a $\sigma$-field $\mathcal{F}$
**Definition:**
- The empty set is an event $\emptyset \in \mathcal{F}$
- Given a countable set of events $A_{1}, A_{2}, \dots,$ its union is also an event.
	- $\bigcup_{i \in \mathbb{N}} A_{i} \in \mathcal{F}$
- If $A$ is an event, so is its complement.
	- $A \in \mathcal{F} \implies A^{c} \in \mathcal{F}$
**Examples:**
- $\mathcal{F} = \left\{ \emptyset, \Omega \right\}$
	- The deterministic case: All statements are either true $\left( \forall w \right)$ or false $\left( \forall w \right)$.
- $\mathcal{F} = \left\{ \emptyset, A, A^{c}, \Omega \right\}$
	- Corresponds to the Bernoulli experiment or tossing a coin. Event $A$ corresponds to "heads".
- $\mathcal{F} = 2^{\Omega} =$ set of all subsets of $\Omega$
When $\Omega$ is finite or enumerable, we can work with $2^\Omega$. Otherwise not.
## Defining Probabilities for all Events $A$
- $\mathbb{P}(\emptyset) = 0, \ \mathbb{P}\left( \Omega \right) = 1$
- If $A_{1}, A_{2}, \dots$ are mutually excluding events (i.e., $A_{i} \cap A_{j} = \emptyset$ for $i \neq j$), then
$$\mathbb{P} \left( \bigcup_{i \in \mathbb{N}}^{\infty} A_{i}\right) = \sum\limits_{i=1}^{\infty} \mathbb{P} \left( A_{i} \right)$$
A $\mathbb{P}: \ \mathcal{F} \mapsto \left[0,1\right]$ satisfying the above properties is a *probability measure.* The triple $\left( \Omega, \mathcal{F}, \mathbb{P} \right)$ is called a **probability space.**
# Conditional Probabilities 
In stochastic processes, we want to know what to expect from the future, conditional on our past observations.
$$
\mathbb{P}\left( A | B \right) = \frac{\mathbb{P}\left( A \cap B \right)}{\mathbb{P}\left( B \right)}
$$
### Caution
Must be precise when specifying the events involved, otherwise wrong conclusions can be reached.

Example: Family has two children. $50\%$ chance of boy for each of them (independent). **Given that at least one is a boy,** what is the probability that they are both boys?

**WRONG answer:**
$$P(\text{two boys } | \text{ at least one boy}) = P(\text{other child is a boy}) = \frac{1}{2}$$
**Set-up:**
- $B_{1}, B_{2}:$ Event that the first, second child is a boy.
- $A:$ Event that at least one is a boy.
- Need to find: $P(B_{1}\cap B_{2}|A)$.
**Conditional Probability Formula:**
$$P(B_{1}\cap B_{2}|A) = \frac{P(B_{1} \cap B_{2})}{P(A)}$$
- $P(B_{1} \cap B_{2}) = \frac{1}{2} \cdot \frac{1}{2} = \frac{1}{4}$ (independent events)
- $P(A) = 1-P(A^{c}) =1 - P(G_{1} \cap G_{2}) = \frac{3}{4}$ (complement rule)
$$P(B_{1}\cap B_{2}|A) = \frac{\frac{1}{4}}{\frac{3}{4}}=\frac{1}{3}$$
**Visualising:**

|     | B      | G      |
| --- | ------ | ------ |
| B   | **BB** | **GB** |
| G   | **BG** | GG     |

## Lemma: Law of total probability
Online:

In [probability theory](https://en.wikipedia.org/wiki/Probability_theory "Probability theory"), the **law** (or **formula**) **of total probability** is a fundamental rule relating [marginal probabilities](https://en.wikipedia.org/wiki/Marginal_probability "Marginal probability") to [conditional probabilities](https://en.wikipedia.org/wiki/Conditional_probabilities "Conditional probabilities"). It expresses the total probability of an outcome which can be realised via several distinct [events](https://en.wikipedia.org/wiki/Event_(probability_theory) "Event (probability theory)"), hence the name.

 *If you want to find $P(A)$, you can look at a partition of $\Omega$, and add the amount of probability of $A$ that falls in each partition.*

We know that for any two events $A$ and $B$:

$$P(A) = P(A \cap B) + P(A \cap B^{c})$$
Using the definition of **conditional probabilities:**
$$\begin{align}
P\left( A | B \right) &=  \frac{P\left( A \cap B \right)}{P\left( B \right)}\\
\implies P(A \cap B) &= P \left( A | B \right) \cdot P(B)
\end{align}$$
Stating in a more general fashion:

Let $B_{1}, \dots, B_{n}$ be a **partition** of $\Omega$. I.e., mutually disjoint and $\bigcup_{i=1}^{n}B_{i}=\Omega$ . Then, for any event $A$:
$$P(A) = \sum\limits_{i=1}^{n}P(A|B_{i})P(B_{i})$$
## Independence

Events $A$ and $B$ are called independent if 
$$P(A \cap B) = P(A) \cdot P(B)$$
When $0 < P(B) < 1$, this is equivalent to 
$$P(A|B) = P(A) = P(A | B^{c})$$
A *family* $\left\{ A_{i}: \ i \in  I \right\}$ of events is called independent if
$$P \left( \bigcap_{i \in J} A_{i} \right) = \prod_{i \in J} P \left( A_i \right)$$
for any finite subset $J$ of $I$.

# Stochastic Variables

## Definition

**Informally:** A quantity which is assigned by a stochastic experiment.
**Formally:** A mapping $X: \ \Omega \rightarrow \mathbb{R}$ (sample space -> real-value)

**Technical comment:** We want the probabilities $P(X \leq x)$ to be well defined. So we require
$$\forall x \in \mathbb{R} : \ \left\{ \omega : \ X(\omega) \leq x \right\} \in \mathcal{F}$$
The mapping of an outcome $\omega$ in the sample space $\Omega$, which results in a probability less than or equal to some real value $x$ is an element of the set of events.

## Examples

- Indicator functions: 
$$X(\omega) = I_{A}(\omega) = \begin{cases} 1 \text{ when } \omega \in A,  \\
0 \text{ else} \end{cases}$$
(Outputs $1$ when $\omega$ belongs to some specific set of outcomes/events $A$)

- Bernoulli variables:
$$\Omega = \left\{ H, T \right\}, \quad X(H)=1, \quad X(T)=0$$
# $F_{X}$,  the Cumulated Distribution Function

$$F(x) = P(X \leq x)$$
**Properties**:
1. $\lim_{x \rightarrow - \infty} F(X) = 0$, $\lim_{x \rightarrow +\infty} F(x) = 1$
2. $x < y \implies F(x) < F(y)$
3. $F$ is right-continuous. Ie. $F(x+h) \rightarrow F(x)$ as $h \downarrow 0$. 

# Discrete and Continuous Variables 

**Discrete variables:** $\mathbf{Im}\left( X \right)$ is a countable set. So $F_{X}$ is a *step function*. Typically $\mathbf{Im} \left( X \right) \subset  \mathbb{Z}$. Image of $X: \Omega \mapsto \mathbb{R}$ is a subset of the set of all integers.

**Continuous variables:** $X$ has a *probability density function* (pdf) $f$, 
$$F(X) = \int^{x}_{-\infty} f(u) \ du$$
so $F$ is differentiable.

## Variables that are neither continuous or discrete

Let $X \sim U(0,1)$. I.e., uniform on $\left[0, 1\right]$ so that 
$$F_{X}(x) = x, \quad \forall x \in \left[0,1\right]$$
Toss a fair coin. If heads, then set $Y=X$. If tails, then set $Y=0$.
$$F_{Y}(y)=\frac{1}{2}+ \frac{1}{2}x, \quad \forall y \in \left[0,1\right]$$
We say that $Y$ has an *atom* at $0$

## Mean and Variance

The **mean** of a stochastic variable in the *discrete case*
$$\mathbb{E}\left( X \right) = \sum\limits_{i \in Z}^{} i P \left( X = i \right)$$
and, in the *continuous case*
$$\mathbb{E}\left( x \right) = \int^{\infty}_{-\infty}f(x) \ dx$$
**Variance:**
$$\begin{align}
\mathbb{V}\left( X \right) &=  \mathbb{E}\left( X - \mathbb{E}\left( X \right) \right)^{2} \\
		&= \mathbb{E}\left( X^{2} \right) - \left( \mathbb{E}\left( X \right) \right)^{2}
\end{align} $$
# Conditional Expectation

The conditional expectation is the mean in the conditional distribution.

$$\mathbb{E}\left( Y | X =x \right) = \sum\limits_{y}^{}f_{Y|X}(y|x)$$
It can be seen as a stochastic variable: Let $\psi \left( x \right) = \mathbb{E}\left( Y|X=x \right)$ then $\psi \left( X \right)$ is the conditional expectation of $Y$ given $X$.
$$\psi(X) = \mathbb{E}\left( Y|X \right)$$
We have
$$\mathbb{E}\left( \mathbb{E} \left( Y|X \right) \right) = \mathbb{E} \left( Y \right)$$
- **Measurability**: $\mathbb{E}[Y∣X]$ is $X$-measurable, meaning that the value of $\mathbb{E}[Y|X]$ depends only on the information contained in $X$.
- **Expectation Matching**: For any set $x \in X$,
$$\int_{x}\mathbb{E}[Y∣X] \ dP = \int_{x} Y \ dP$$
this property ensures that the conditional expectation $\mathbb{E}[Y∣X]$ behaves like the original random variable $Y$ in terms of average behaviour when restricted to events in $X$.

## Conditional Variance

$$\mathbb{V}\left( Y | X=x \right) = \sum\limits_{y}^{}\left( y-\psi \left( x \right) \right)^{2}f_{Y|X}\left( y|x \right)$$
This can also be written as 
$$\mathbb{V}\left( Y|X \right) = \mathbb{E}\left( Y^{2}|X \right)-\left( \mathbb{E}\left( Y|X \right) \right)^{2}$$
### Proof: Law of total variance

$$\begin{align}
\mathbb{V}\left( Y \right) &= \mathbb{E}\left( Y^{2} \right) - \left( \mathbb{E} \left( Y \right) \right)^{2}\\
\implies \mathbb{E}\left( Y^{2} \right) &= \mathbb{V}\left( Y \right) + \left( \mathbb{E} \left( Y \right) \right)^{2}
\end{align}$$

- Applying the **law of total expectation**
$$\begin{align}
\mathbb{E}\left( Y^{2} \right) &= \mathbb{E}\left( \mathbb{V}\left( Y|X \right)+\mathbb{E}\left( Y|X \right)^{2} \right)
\end{align}$$
- Substituting into original equation
$$\begin{align}
\mathbb{E}\left( Y^{2} \right) - \mathbb{E}\left( Y \right)^{2} &= \mathbb{E}\left[\mathbb{V}\left( Y|X \right)+\mathbb{E}\left( Y|X \right)^{2}\right] - \mathbb{E}\left( Y \right)^{2}
\end{align}$$
- Applying the law of total expectation to rightmost term
$$
\begin{align}
\mathbb{E}\left( Y^{2} \right) - \mathbb{E}\left( Y \right)^{2} &= \mathbb{E}\left[\mathbb{V}\left( Y|X \right)+\mathbb{E}\left( Y|X \right)^{2}\right] - \mathbb{E} \left[\mathbb{E} \left( Y|X \right)\right]^{2}
\end{align}
$$
- Linearity of expected values property
$$\begin{align}
\mathbb{E}\left( Y^{2} \right) - \mathbb{E}\left( Y \right)^{2} &= \mathbb{E}\left[\mathbb{V}\left( Y|X \right)\right]+ \left(\mathbb{E} \left[\mathbb{E}\left( Y|X \right)^{2}\right] -\mathbb{E} \left[\mathbb{E} \left( Y|X \right)\right]^{2} \right) 
\end{align}$$
- Decomposition of variance into expected values
$$\mathbb{V}\left( Y \right)=\mathbb{E}\left[\mathbb{V}\left( Y|X \right)\right]+\mathbb{V}\left[\mathbb{E}\left( Y|X \right)\right]$$
This *partitions* the variance of $Y$.

## Random Vectors

When a stochastic experiment defines the value of several stochastic variables.

**Example:**
- Throw a dart. Record both vertical and horizontal distance from center.
$$X = \left( X_{1}, \dots, X_{n} \right): \ \Omega \mapsto \mathbb{R}^n$$
Also, random vectors are characterised by the cumulative distribution function $F: \ \mathbb{R}^{n}\mapsto \left[0,1\right]$:
$$F(x) = P \left( X_{1}\leq x_{1}, \dots, X_{n} \leq x_{n} \right)$$
where $x=\left( x_{1}, \dots, x_{n} \right)$

### Example

- Two fair coins are tossed. Results are assigned to $V$ and $Z$.
- In another experiment, we one fair coin. Results are assigned to $Y$ and $Z$.
- $V, X, Y$ and $Z$ are all identically distributed.
- But, $\left( V, X \right)$ and $\left( Y, Z \right)$ are *not* identically distributed.

E.g., $P(V=X=\text{heads})=\frac{1}{4} = P(V=\text{heads}) \cdot P(X=\text{heads}) = \frac{1}{4}$, while $P(Y=Z=\text{heads}) = \frac{1}{2}$

# The Bernoulli Process

- Start with working out one single **Bernoulli experiment**
- Then consider a finite number of Bernoulli experiments: **The binomial distribution**
- Then, a sequence of Bernoulli experiments: **The Bernoulli process**
- Waiting times in the Bernoulli process: **The negative binomial distribution**

## The Bernoulli Experiment

A Bernoulli experiment models. E.g., tossing a coin.

- The sample space is $\Omega = \left\{ H, T \right\}$.
- Events are $\mathcal{F} = \left\{ \emptyset, \left\{ H \right\}, \left\{ T \right\}, \Omega\right\} = 2^{\Omega} = \left\{ 0, 1 \right\}^{\Omega}$
- The Probability $P: \mathcal{F} \mapsto \left[0, 1\right]$ is defined by
$$P \left( \left\{ H \right\} \right) = p$$
The stochastic variable $X: \ \Omega \mapsto \mathbb{R}$ with 
$$X \left( H \right) = 1, \quad X \left( T \right)=0$$
Is *Bernoulli distributed* with parameter $p$.

## A Finite Number of Bernoulli Variables

- We toss a coin $n$ times.
- The sample space is $\Omega = \left\{ H, T \right\}^{n}$
- For the case $n=2$, this is $\left\{ TT, TH, HT, HH \right\}$
- Events are $\mathcal{F}=2^{\Omega}=\left\{ 0, 1 \right\}^\Omega$
- How many events are there? $\left\vert \mathcal{F} \right\vert = 2^{\left\vert \Omega \right\vert} = 2^{2^{n}}$

Introduce $A_{i}$ for the event *"the $i$'th toss showed heads"*.

The probability $P: \mathcal{F} \mapsto \left[0,1\right]$ is defined by
$$P(A_{i}) = p$$
and by requiring that the events $\left\{ A_{i}: \ i = 1, \dots , n \right\}$ are independent, we derive
$$P(\left\{ \omega \right\}) = p^{k}(1-p)^{n-k}, \quad \text{if } \omega \text{ has } k \text{ heads and } n-k \text{ tails}$$
and from that the probability of *any* event.

Define the stochastic variable $X$ as the number of heads (Sum of the number of heads in a sequence of tosses)
$$X = \sum\limits_{i=1}^{n}1(A_{i})$$
To find the **probability mass function** of $X$, consider the events
$$
P(X=x), \quad \text{shorthand for } P \left( \left\{ \omega: \ X(\omega)=x \right\} \right)
$$
The event $\left\{ X=x \right\}$ has $\begin{pmatrix} n \\ x \end{pmatrix}$ elements. Each $\omega \in \left\{ X = x \right\}$ has probability 
$$P \left( \omega \right) = p^{x} \left( 1 - p \right)^{n-x}$$
so the probability is 
$$P \left( X = x \right) = \begin{pmatrix} n \\ x \end{pmatrix} p^{x} \left( 1 - p \right)^{n-x}$$
### Summary
1. Defined the sample space $\Omega$ as well as the events $\mathcal{F}$
2. The defined a probability $P: \ \mathcal{F} \mapsto \left[0, 1\right]$ for a single event.
3. Extended this probability to the entire sample space.
4. Defined a stochastic variable, in terms of events.
5. Found the *probability mass function* of the stochastic variable, using the probability found in step $3$ and the number of combinations in a sequence of elements.

## Properties of $B \left( n, p \right)$

**Probability mass function**
$$\operatorname{pdf} = f_{X}\left( x \right) = P \left( X=x \right) = \begin{pmatrix} n \\ x \end{pmatrix} p^{x} \left( 1-p \right)^{n-x}$$
**Cumulative distribution function**
$$\operatorname{cdf} = F_{X}\left( x \right)=P \left( X \leq x \right) = \sum\limits_{i=0}^{x} f_{X} \left( i \right)$$
**Mean value**
$$\mathbb{E}\left[X\right] = \mathbb{E} \left[ \sum\limits_{i=1}^{n}1 \left( A_{i} \right)\right]=\sum\limits_{i=1}^{n} P \left( A_{i} \right) = np$$
**Variance**
$$\mathbb{V} \left[X\right] = \sum\limits_{i=1}^{n} \mathbb{V} 1 \left( A_{i} \right)=np(1-p)$$

because $\left\{ A_{i}: i = 1, \dots , n \right\}$ are (pairwise) independent.

### Problem

Let $X \sim B \left( n, p \right)$ and $Y \sim B \left( m, p \right)$ be independent. Show that $Z=X+Y \sim B \left( n+m, p \right)$.

**Solution:** Consider $n+m$ independent Bernoulli trials, each with probability $p$.

Set $X = \sum\limits_{i=1}^{n}1 \left( A_{i} \right)$ and $Y = \sum\limits_{i=n+1}^{n+m} 1 \left( A_{i} \right)$

Then $X$ and $Y$ are as in the problem, and
$$Z = \sum\limits_{i=1}^{n+m} 1 \left( A_{i} \right) \sim B \left( n, p \right)$$
## The Bernoulli Process

- Sample space $\Omega$ is the set of functions $\mathbb{N} \mapsto \left\{ 0, 1 \right\}$
- Introduce events $A_{i}$ for the "$i$'th toss showed heads".
	- Strictly $A_{i} = \left\{ \omega : \ \omega \left( i \right) = 1\right\}$
- Let $\mathcal{F}$ be the smallest $\sigma$-field that contains **all** $A_{i}$
- Define $P: \ \mathcal{F} \mapsto \left[0,1\right]$ by
$$P \left( A_{i} \right)=p$$
and
$$\left\{ A_{i}: \ i \in \mathbb{N} \right\} \text{ are independent}$$
## Waiting Times

Let $W_{r}$ be the waiting time for the $r$'th success.
$$W_{t}= \min \left\{ i: \ \sum\limits_{j=1}^{i} 1 \left( A_{j} \right) = r \right\}$$
To find the probability mass function of $W_{r}$, note that $W_{r}=k$ is the same event as 
$$\left( \sum\limits_{i=1}^{k-1} 1 \left( A_{j} \right) = r-1 \right) \cap A_{k}$$
Since the two events involved here are independent, we get
$$f_{W} \left( k \right) = P(W_{r}=k) = \begin{pmatrix} k-1 \\ r-1 \end{pmatrix} p^{r} \left( 1-p \right)^{k-r}$$
## Geometric Distribution

The waiting time $W$ to the first success 
$$P(W=k) = \left( 1-p \right)^{k-1}p$$
(first $k-1$ failures and then one success)

The *survival function* is 
$$G_{W} \left( k \right) = P \left( W > k \right) = \left( 1-p \right)^{k}$$

# Problems

# Notes on Notation

The notation $2^{\Omega}$ represents the **power set** of the sample space $\Omega$.
### Power Set Definition

The power set of a set $\Omega$, denoted by $2^{\Omega}$, is the set of all possible subsets of $\Omega$, including the empty set $\emptyset$ and $\Omega$ itself. In other words, if $\Omega$ is a set, then $2^{\Omega}$ is the collection of every subset of $\Omega$.
