# Content
1. Probability spaces, $\sigma$-fields and measures.
2. Random variables and their distributions.
3. Expectation and Variance.
4. The $\sigma$-field generated by a random variable.
5. Independence and conditional probability.
# Events and Probability
## 1.1 - Expanding and Contracting Events
### Expanding Events
Show that if $A_{1}, A_{2}, \dots$ is an *expanding* sequence of events, 
$$A_{1} \subset A_{2} \subset \dots $$
then 
$$\operatorname{P} \left( A_{1} \cup A_{2} \cup \dots \right) = \lim_{n \rightarrow \infty} \operatorname{P} \left( A_{n} \right)$$
#### Answer 

We can write $A_{1} \cup A_{2} \cup \dots$ as the union of a sequence of disjoint events. We start with $A_{1}$,  and add a disjoint set $B_{1}$ to $A_{2}$. More formally,
$$A_{1}\cup B_{2}=  A_{2} \implies A_{1} \subset A_{2}$$
we can do the same to form $A_{3}$
$$A_{1} \cup B_{2} \cup B_{3} = A_{2} \cup B_{3} = A_{3} \implies A_{2} \subset A_{3}$$
Since the sets $B_{1} \cup B_{2} \cup \dots$ are pairwise disjoint, and belong to $\mathcal{F}$, we can express 
$$\operatorname{P} \left( A_{1} \cup A_{2} \cup \dots  \right)$$
as 
$$\operatorname{P} \left(A_{1} \cup B_{2} \cup B_{3} \cup \dots  \right)$$
Using the fact that, for pairwise disjoint sets belong to the same $\mathcal{F}$ 
$$\operatorname{P} \left( A_{1} \cup B_{2} \cup B_{3} \cup \dots , \cup   B_{n}\right) = \operatorname{P} \left( A_{n} \right)$$
Thus, if we simply take the limit
$$\lim_{n \rightarrow \infty} \operatorname{P} \left( A_{1} \cup B_{2} \cup B_{3} \cup \dots , \cup   B_{n}\right) = \lim_{n \rightarrow \infty}\operatorname{P} \left( A_{n} \right)$$
#### Solution
### Contracting Events
Show that, if $A_{1}, A_{2}, \dots$ is a *contracting* sequence of events, I.e.,
$$A_{1} \supset A_{2} \supset \dots$$
then
$$\operatorname{P} \left( A_{1} \cap A_{2} \cap \dots  \right) = \lim_{n \rightarrow \infty} \operatorname{P} \left( A_{n} \right)$$
#### Answer
Using *De Morgan's law*
$$\begin{align}
  \overline{A \cup B} &= \overline{A} \cap \overline{B}, \\
  \overline{A \cap B} &= \overline{A} \cup \overline{B},
\end{align}$$
We make the following equivalence
$$\overline{A_{1}\cap A_{2} \cap \dots} \equiv \overline{A_{1}} \cup \overline{A_{2}} \cup \dots$$
We know that if we apply a probability measure to some event $A$, then we can express the probability of its complement in the following way
$$\operatorname{P} \left( A \right) \equiv 1-\operatorname{P} \left( \overline{A} \right)$$
Using the same method as [[Review of Probability#1.1 - Expanding and Contracting Events#Answer|outlined above]], 
$$\begin{align}
\lim_{n \rightarrow \infty} \operatorname{P} \left( \overline{A_{1}} \cup B_{2} \cup \dots  \right) &\equiv 
\end{align}$$