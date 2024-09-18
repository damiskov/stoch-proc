# 4.1.1 - Limiting Distribution

Find the limiting distribution of the following transition probability matrix
$$
\begin{align}
\mathrm{P}&= \left\Vert \begin{matrix} 0.7 & 0.2 & 0.1 \\ 0 & 0.6 & 0.4 \\  0.5 & 0 & 0.5 \end{matrix} \right\Vert \\
\end{align}
$$
taking the limit 
$$\begin{align}
\lim_{n \rightarrow \infty} \mathrm{P}^{n} = \begin{bmatrix} 0.476  & 0.238 &  0.286 \\
0.476 &  0.238 &  0.286 \\
0.476 &  0.238 &  0.286 \end{bmatrix} 
\end{align}$$
So we have the limiting distribution

$$
\left[\pi_{0}, \pi_{1}, \pi_{2}\right] = \left[0.476, 0.238, 0.286\right]
$$
# 4.3.1 - Equivalence Classes

A Markov Chain has a transition probability matrix 
$$\begin{align}
\mathrm{P}=\left\Vert \begin{matrix} 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 \\ 0.5 & 0 & 0 & 0 & 0 & 0.5 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 \\ 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ \end{matrix} \right\Vert
\end{align}$$
## a) Find the equivalence classes

*The states in an equivalence class are those that communicate with each other.* I.e, for **for some integer** $n \geq 0$, $P_{ij}^{(n)} > 0$ and $P_{ji}^{(n)} >0$.

Using code:
```
Communicating states for P:

{(0, 7), (0, 4), (2, 1), (6, 5), (4, 3), (5, 4), (7, 6), (1, 0), (3, 2)}
```
## b)  Is it true that $P_{00}^{(n)} >0$ ($n \in \left\{ 1, 2, \dots , 20 \right\}$)

See script:
```
P_n[0,0] = 0.5 at n = 5
```

# 4.4.2 

Markov chain with following transition probability matrix
$$\begin{align}
\mathrm{P} &= \left\Vert \begin{matrix} 0 & 1 & 0 & 0 \\
0.1 & 0.4 & 0.2 & 0.3\\
0.2 & 0.2 & 0.5 & 0.1\\
0.3 & 0.3 & 0.4 & 0 \end{matrix} \right\Vert
\end{align}$$
## a) Determine the limiting probability that the process is in state $0$
$$\begin{align}
\lim_{n \rightarrow \infty} \mathrm{P}^{n}_{00} = \pi_{0}=0.145 
\end{align}$$
## b) By pretending that state 0 is absorbing, use a first step analysis (Chapter 3, Section 3.4) and calculate the mean time $m_{10}$ for the process to go from state $1$ to state $0$.

Using method outlined in [[Markov Chains 1#First Step Analysis|week 1]].

- $\nu_{0} = 0$
- $\nu_{1}=1 + 0.4 \nu_{1} + 0.2 \nu_{2} + 0.3 \nu_{3}$
- $\nu_{2} = 1+ 0.2 \nu_{1}+0.5 \nu_{2}+0.1 \nu_{3}$
- $\nu_{3} = 1 + 0.3 \nu_{1} + 0.4 \nu_{2}$

Converting this system of equations into matrix form
$$
\begin{align}
\nu &= \begin{bmatrix}0.4 & 0.2 & 0.3\\
0.2 & 0.5 & 0.1\\
0.3 & 0.4 & 0\end{bmatrix} \nu + \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix}\\
\implies \nu &= \left( I-A \right)^{-1} \cdot \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix}
\end{align}
$$
Which, when solved, gives us the result
$$
\begin{align}
\nu &= \begin{bmatrix} 5.90\\ 5.34\\ 4.91 \end{bmatrix}
\end{align}
$$
and the mean time to absorption from state $0$ to state $1$ is clearly 
$$\nu_{0}=5.90$$
# c) Because the process always goes directly to state $1$ from state $0$, the mean return time to state $0$ is $m_{0} = 1 + m_{10}$ . Verify equation ($4.26$), $π_0 = 1/m_0$

Equation $4.26$ is given in [[Markov Chains 3#The Basic Limit Theorem of Markov Chains#Theorem 4.3 - The basic limit theorem of Markov Chains|Theorem 4.3 - The basic limit theorem of Markov Chains]]:
$$\lim_{n \rightarrow \infty}P_{ii}^{(n)} = \frac{1}{\sum\limits_{n=0}^{\infty} n \cdot f_{ii}^{(n)}}= \frac{1}{m_{i}}$$
Getting the limiting distribution:
$$\pi\approx \begin{bmatrix} 0.14 & 0.41 & 0.29 & 0.15 \end{bmatrix}$$
Therefore, $\pi_{0} = 0.14$. Given that $m_{0}=1+m_{10}=1+5.90=6.90$, we also have that $\pi_{0}=\frac{1}{m_{0}}=\frac{1}{6.90}\approx 0.14$.





