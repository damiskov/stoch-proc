# Notation and Elements of Probability Theory

The probability triple $\left( \Omega, \mathcal{F}, \mathbb{P} \right)$:
- $\Omega:$ The sample space. I.e., set of all possible outcomes.
	- $w \in \Omega$
	- E.g., The sample space of a coin toss is $\Omega = \left\{ H, T \right\}$
- $\mathcal{F}:$ The set of events, $A \in \mathcal{F} \implies A \subset \Omega$
	- *The set of outcomes of an experiment*
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
$$\mathbb{P} \left( \bigcup_{i \in \mathbb{N}}^{\infty} A_{i} = \sum\limits_{i=1}^{\infty} \mathbb{P} \left( A_{i} \right) \right)$$
A $\mathbb{P}: \ \mathcal{F} \mapsto \left[0,1\right]$ satisfying the above properties is a *probability measure.* The triple $\left( \Omega, \mathcal{F}, \mathbb{P} \right)$ is called a **probability space.**
# Conditional Probabilities 
In stochastic processes, we want to know what to expect from the future, conditional on our past observations.
$$\mathbb{P}\left( A | B \right) = \frac{\mathbb{P}\left( A \cap B \right)}{\mathbb{P}\left( B \right)}$$
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
## Indepee