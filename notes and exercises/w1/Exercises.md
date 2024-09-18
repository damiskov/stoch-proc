# 3.1 - Definitions

#### **3.1.1**

$$\begin{align}
\operatorname{P} \left( X_{0}=0, X_{1}=1, X_{2}=2 \right) &= \operatorname{P} \left( X_{2}=1 \mid X_{1}=1, X_{0}=0 \right) \operatorname{P} \left( X_{1}=1 \mid X_{0}=0 \right) \operatorname{P} \left( X_{0}=0 \right)\\
\end{align}$$
Using the *Markov chain property*, and the values provided to us
$$\begin{align}
\operatorname{P} \left( X_{0}=0, X_{1}=1, X_{2}=2 \right) &=  \operatorname{P} \left( X_{2}=2  \mid X_{1}=1 \right) \mathbf{P}_{0, 1} p_{0} \\
&= \mathbf{P}_{1,2} \mathbf{P}_{0,1} p_{0}\\
&= 0 \cdot 0.2 \cdot 0.3\\
&=0 \left( \checkmark \right)
\end{align}$$
#### **3.1.2**

**a)**
$$\begin{align}
\operatorname{P} \left( X_{2}=2, X_{3}=1 \mid X_{1}=0 \right) &= \operatorname{P} \left( X_{3}=1 \mid X_{2}=1, X_{1}=0 \right) \cdot \operatorname{P} \left( X_{2}=1 \mid X_1 =0 \right) \\
&= \mathbf{P}_{1, 1} \cdot \mathbf{P}_{0, 1}\\
&= 0.6 \cdot 0.2 \\
&= 0.12
\end{align}$$
**b)**
$$\begin{align}
\operatorname{P} \left( X_{1}=1, X_{2}=1 \mid X_{0}=0 \right) &= \operatorname{P} \left( X_{2}=1 \mid X_{1}=1, X_{0}=0 \right) \cdot \operatorname{P} \left( X_{1}=1 \mid X_{0}=0 \right) \\
&= \mathbf{P}_{1,1} \cdot \mathbf{P}_{0,1}\\
&= 0.6 \cdot 0.2\\
&= 0.12
\end{align}
$$

#### **3.1.3**
$$\begin{align}
\operatorname{P} \left( X_{0}=1, X_{1}=0, X_{2}=2 \right) &= \operatorname{P} \left( X_{2}=2 \mid X_{1}=0, X_{0}=1 \right) \cdot \operatorname{P} \left( X_{1}=0 \mid X_{0}=1 \right) \cdot \operatorname{P} \left( X_{0}=1 \right) \\
&= \mathbf{P}_{0,2} \cdot \mathbf{P}_{1,0} \cdot 1\\
&= 0.1 \cdot 0.3 \\
&= 0.03
\end{align}$$
#### **3.1.4**

**a)**
$$\begin{align}
\operatorname{P} \left( X_{1}=1, X_{2}=1  \mid X_{0}=0 \right) &= \operatorname{P} \left( X_{2}=1 \mid X_{1}=1, X_{0}=0 \right) \cdot \operatorname{P} \left( X_{1}=1 \mid X_{0}=0 \right) \\
&= \mathbf{P}_{1,1} \cdot \mathbf{P}_{0,1} \\
&= 0.2 \cdot 0.1 \\
&= 0.02 \left( \checkmark \right)
\end{align}$$
**b)**
$$\begin{align}
\operatorname{P} \left( X_{2}=1, X_{3}=1 \mid X_{1}=0 \right) &= \operatorname{P} \left( X_{3}=1 \mid X_{2}=1, X_{1}=0 \right) \cdot \operatorname{P} \left( X_{2}=1 \mid X_{1}=0 \right) \\
&= \mathbf{P}_{1,1} \cdot \mathbf{P}_{0,1} \\
&= 0.02 \left( \checkmark \right)
\end{align}$$
#### **3.1.5**
**a)**
$$\begin{align}
\operatorname{P} \left( X_{0}=1, X_{1}=1, X_{2}=0 \right) &= \operatorname{P} \left( X_{2}=0 \mid X_{1}=1, X_{0}=1 \right) \cdot \operatorname{P} \left( X_{1}=1 \mid X_{0}=1 \right) \cdot \operatorname{P} \left( X_{0}=1 \right) \\
&= \mathbf{P}_{1,0} \cdot \mathbf{P}_{1,1} \cdot p_{1}\\
&= 0.5 \cdot 0.1 \cdot 0.5\\
&= 0.025
\end{align}$$
**b)**
$$\begin{align}
\operatorname{P} \left( X_{1}=1, X_{2}=1, X_{3}=0 \right) &= \operatorname{P} \left( X_{3}=0 \mid X_{2}=1, X_{1}=1 \right) \cdot \operatorname{P} \left( X_{2}=1 \mid X_{1}=1 \right) \cdot \operatorname{P} \left( X_{1}=1 \right)
\end{align}$$
Now,
$$\begin{align}
\operatorname{P} \left( X_{1}=1 \right) &= \sum\limits_{k}^{} \operatorname{P} \left( X_{1}=1,  X_{0}=k \right) \\
&= \sum\limits_{k=0}^{2} \operatorname{P} \left( X_{1}=1 \mid X_{0}=k \right) \cdot \operatorname{P} \left( X_{0}=k \right) \\
&= 0.5 \cdot \left( \mathbf{P}_{0, 1} + \mathbf{P}_{1,1} \right) \\
&= 0.5 \cdot \left( 0.2 + 0.1 \right)\\
&= 0.15
\end{align}$$

# **3.2 - Transition Probabilities**

#### **3.2.1**
**a)**
$$\begin{align}
\mathbf{P}&= \begin{bmatrix} 0.1  & 0.2  &  0.7  \\ 0.2  & 0.2  & 0.6  \\ 0.6 & 0.1 & 0.3 \end{bmatrix} \\
\mathbf{P}^{2} &= \begin{bmatrix} 0.47 & 0.13  & 0.4  \\
0.42  & 0.14  & 0.44  \\
0.26  & 0.17  & 0.57 \end{bmatrix} \\
\mathbf{P}^{3}&= \begin{bmatrix} 0.313  &  0.16  & 0.527\\
 0.334  &  0.156  & 0.51  \\
0.402  & 0.143  & 0.455 \end{bmatrix} \\
&\left( \checkmark \right)
\end{align}$$
**b)**
$$\begin{align}
\operatorname{P} \left( X_{3}=1 \mid X_{1}=0 \right) &= \mathbf{P}_{0,1}^{2} \\
&= 0.13 \left( \checkmark \right)
\end{align}$$
**c)**
$$\begin{align}
\operatorname{P} \left( X_{3} =1 \mid X_{0}=0 \right)&=\mathbf{P}_{0,1}^{3}\\
&= 0.16 \left( \checkmark \right)
\end{align}$$
#### **3.2.2**

$$
\mathbf{P} = \left\Vert \begin{matrix} 0  &  \frac{1}{2} & \frac{1}{2} \\ \frac{1}{2} & 0 & \frac{1}{2} \\ \frac{1}{2} & \frac{1}{2} & 0 \end{matrix} \right\Vert
$$

| $n$                                        | $0$ | $1$ | $2$           | $3$           | $4$           |
| ------------------------------------------ | --- | --- | ------------- | ------------- | ------------- |
| $\operatorname{P}(X_{n} = 0 \mid X_{0}=0)$ | $1$ | $0$ | $\frac{1}{2}$ | $\frac{1}{4}$ | $\frac{3}{8}$ |
#### **3.2.3**

$$\begin{align}
\operatorname{P} \left( X_{3}=1 \mid X_{0}=0 \right) &= \mathbf{P}^{3}_{0, 1}\\
&= 0.478
\end{align}$$
#### **3.2.4**

$$\begin{align}
\mathbf{P} &= \left\Vert \begin{matrix} 0.6  & 0.3  & 0.1  \\ 0.3  & 0.3  & 0.4  \\ 0.4  & 0.1  & 0.5 \end{matrix} \right\Vert \\
\mathbf{P}^{2}&= \left\Vert \begin{matrix} 0.49 &  0.28 &  0.23 \\
0.43  &  0.22 &  0.35\\ 0.47 &  0.2 &  0.33  \end{matrix} \right\Vert
\end{align}$$
$$\begin{align}
\operatorname{P} \left( X_{2}=2 \mid X_{0}= 1\right) &= \mathbf{P}^{2}_{1,2} \\
&= 0.35 \left( \checkmark \right)
\end{align}$$
#### **3.2.5**
**a)**

$$\begin{align}
\operatorname{P} \left( X_{3}=1 \mid X_{1}=0 \right) &= \mathbf{P}_{0, 1}^{2}\\
\end{align}$$
**b)**
$$\begin{align}
\operatorname{P} \left( X_{2} = 1 \mid X_{0}=0 \right) &= \mathbf{P}_{0, 1}^{2}
\end{align}$$
#### **3.2.6**
**a)**
$$\begin{align}
\operatorname{P} \left( X_{2}=0 \right) &= \sum\limits_{k=0}^{2} \operatorname{P} \left( X_{2}=0, X_{0}=k \right) \\
&= \sum\limits_{k=0}^{2} \operatorname{P} \left( X_{2}= 0 \mid X_{0}=k \right) \operatorname{P} \left( X_{0}=k \right) \\
&= \operatorname{P} \left( X_{2}= 0 \mid X_{0}=0 \right) \cdot p_{0} + \operatorname{P} \left( X_{2}= 0 \mid X_{0}=1 \right) \cdot p_{1}\\
&= 0.5 \cdot (\mathbf{P}_{0,0}^{2} + \mathbf{P}_{1,0}^{2})\\
&= 0.5 \cdot \left( 0.44 + 0.4 \right)\\
&= 0.5 \cdot 0.84\\
&= 0.42
\end{align}$$
**b)** Same calculations as above, but with $\mathbf{P}^{3}$.

# **3.3 - Some Markov Chain Models**

#### **3.3.1**

Spare parts inventory model with $s=0$ (Threshold at which restocking occurs), $S=3$ (Amount of stock after resupply) and possible daily demands of $\left\{ 0, 1, 2 \right\}$ with
$$\operatorname{P} \left( \xi_{n}=0 \right)=0.4, \quad \operatorname{P} \left( \xi_{n}=1 \right) = 0.3, \quad \operatorname{P} \left( \xi_{n}=2 \right)=0.3$$
The possible states are therefore $X_{n}=\left\{-2, -1, 0, 1, 2, 3  \right\}$. 

$$\mathbf{P} = \left\Vert \begin{matrix} 0  & 0 & 0 & 0.3 & 0.3 & 0.4  \\  0  & 0 & 0 & 0.3 & 0.3 & 0.4  \\ 0.3  & 0.3 & 0.4 & 0 & 0 & 0  \\ 0  & 0.3 & 0.3 & 0.4 & 0 & 0  \\ 0  & 0 & 0.3 & 0.3 & 0.4 & 0  \\ 0 & 0 & 0 & 0.3 & 0.3 & 0.4  \end{matrix}
\right\Vert$$
#### **3.3.2**

Two urns, $A$, $B$ containing a total of $N$ balls. Experiment is performed where each ball is equally likely to be selected $\operatorname{P} \left( \text{selected} \right)=\frac{1}{N}$. Then, an urn is selected at random $\operatorname{P} \left( A \right) = p$ and $\operatorname{P} \left( B \right) = q.$ The ball drawn is placed in the selected urn. State of the system is based on the number of balls in $A$.

States: $X_{n}= \left\{ N, N-1, \dots , 1, 0 \right\}$ 

Transitions:
- Ball selected from $A$, and placed in $A$: $\frac{N_{A}}{N} \cdot \frac{1}{2} = \frac{N_{A}}{2 N}$. Change in $A: \ 0$
- Ball selected from $A$, and placed in $B$: $\frac{N_{A}}{N} \cdot \frac{1}{2}=\frac{N_{A}}{2 N}.$ Change in $A: \ -1$ 
- Ball selected from B, and placed in $A: \ \frac{N_{B}}{N} \cdot  \frac{1}{2} = \frac{N_{B}}{2N}$. Change in $A: +1$
- Ball selected from $B$ and placed in $B: \ \frac{N_{B}}{N} \cdot  \frac{1}{2} = \frac{N_{B}}{2N}.$ Change in $A: \ 0$ 

Therefore,
- $\operatorname{P} \left( X_{n+1}=X_{n}\right) = \frac{N_{A}+N_{B}}{2N}= \frac{1}{2}$
- $\operatorname{P} \left( X_{n+1}=X_{n}+1 \right) = \frac{N_{B}}{2N}$
- $\operatorname{P} \left( X_{n+1}=X_{n}-1 \right) = \frac{N_{A}}{2N}$

Probability transition matrix: $\begin{matrix} 0  & \rightarrow  & N \\ \downarrow  &   & \\ N  &   &  \end{matrix}$ 

$$\mathbf{P}=\left\Vert \begin{matrix}  \frac{1}{2}  &   \frac{1}{2}  & 0  & 0  & \cdots  & 0  & 0 & 0  \\ \frac{1}{2N}  &   \frac{1}{2}  &  \frac{N-1}{2N} & 0  & \cdots  & 0  & 0 & 0 \\ 0 & \frac{2}{2N}  &  \frac{1}{2}  & \frac{N-2}{2N}  & \cdots  & 0 & 0 & 0  \\ \vdots  &   &   & \ddots  &   &   &   & \vdots  \\ 0 & 0 & 0 & 0 & \cdots  &  \frac{N-1}{2N}  &    \frac{1}{2}  &  \frac{1}{2N}  \\ 0 & 0 & 0 & 0 & \cdots  & 0 &  \frac{1}{2}  &  \frac{1}{2}  \end{matrix} \right\Vert$$

# **3.4 - First Step Analysis**

#### **3.4.1**

Mean time to reach state $3$  starting at state $0$ for the Markov chain with transition probability matrix:
$$\mathbf{P} = \left\Vert \begin{matrix} 0.4 & 0.3 & 0.2 & 0.1 \\ 0  & 0.7 & 0.2 & 0.1  \\ 0 & 0 & 0.9 & 0.1 \\ 0 & 0 & 0 & 1 \end{matrix} \right\Vert$$
$$T = \min \left\{ n \geq 0 \mid X_{n}=3 \right\}$$
Given that $X_{0}=0:$
$$u_{i} = \operatorname{P} \left( X_{T}=3 \mid X_{0}=0 \right)$$ $$\nu = \mathbb{E} \left[T \mid X_{0}=0\right]$$
First step analysis: **Transition probabilities to a absorbing state are treated as constants. Transition probabilities to non-absorbing states are coefficients**
- $u_{0}=0.4 u_{0} + 0.3 u_{1}+0.2 u_{2}+0.1$
- $u_{1}=0.7u_{1}+0.2 u_{2} +0.1$
- $u_{2}=0.9u_{2}+0.1$ 

We have the following system of equations:
$$\begin{align}
\begin{bmatrix} u_{0} \\ u_{1} \\ u_{2}  \end{bmatrix} &= \begin{bmatrix}  0.4  & 0.3 & 0.2 \\
0 & 0.7 & 0.2 \\
0 & 0 & 0.9\end{bmatrix} \cdot \begin{bmatrix} u_{0} \\ u_{1} \\ u_{2}  \end{bmatrix} + \begin{bmatrix} 0.1\\
0.1\\
0.1 \end{bmatrix} \\
\implies \left( I-A \right) \mathrm{u} &= \begin{bmatrix} 0.1\\
0.1\\
0.1 \end{bmatrix}\\
\implies \mathrm{u} &= \left( I-A \right)^{-1}\begin{bmatrix} 0.1\\
0.1\\
0.1 \end{bmatrix}\\
\mathrm{u} &= \begin{bmatrix} 1\\
1\\
1 \end{bmatrix}
\end{align}$$

**Re-doing:**

Mean time to reach state $3$  starting at state $0$ for the Markov chain with transition probability matrix:
$$\mathbf{P} = \left\Vert \begin{matrix} 0.4 & 0.3 & 0.2 & 0.1 \\ 0  & 0.7 & 0.2 & 0.1  \\ 0 & 0 & 0.9 & 0.1 \\ 0 & 0 & 0 & 1 \end{matrix} \right\Vert$$
$$T = \min \left\{ n \geq 0 \mid X_{n}=3 \right\}$$
and 
$$\nu_{0}=\mathbb{E} \left[T \mid X_{0}=0\right]$$

  - $\nu_{0}=1+0.4 \nu_{0}+0.3 \nu_{1} + 0.2 \nu_{2}$
	  - $0.6 \nu_{0}=6, \ \implies \nu_{0}=10$
  - $\nu_{1}=1+0.7 \nu_{1}+0.2 \nu_{2}$
	  - $\implies 0.3 \nu_{1}=3 \ \therefore \nu_{1}=10$
  - $\nu_{2}=1+0.9 \nu_{2}$
	  - $\implies 0.1 \nu_{2}=1, \ \therefore \nu_{2}=10$

Thus, 
$$\nu_{0}=\mathbb{E} \left[T \mid X_{0}=0\right] = 10 \left( \checkmark \right)$$
#### **3.4.2**
Markov chain transition probability matrix is given
$$
\mathbf{P} = \left\Vert \begin{matrix} 1 & 0 & 0 \\ 0.1 & 0.6 & 0.3 \\ 0 & 0 & 1 \end{matrix} \right\Vert
$$
**a) Starting in state 1, determine the probability that the Markov chain ends in state 0.** 
Given that $T = \min \left\{ n \geq 0 \mid X_{n}=0 \right\}$
$$\operatorname{P} \left( X_{T}=0 \mid X_{0}=1 \right)$$
First,
$$
\begin{align}
u &= \operatorname{P} \left( X_{T} \mid X_{0}=1 \right) \\
u &=  1 \cdot 0.1 +0.6 u + 0 \cdot 0.3 \\
\implies u &= 0.25 \left( \checkmark \right)
\end{align}
$$
**b) Determine the mean time to absorption.**
$$\nu_{i} = \mathbb{E} \left[T \mid X_{0}=i\right]$$
- $\nu_{0}=0$
- $\nu_{1}=1+0 \cdot 0.1 + \nu_{1} \cdot 0.6 + 0 \cdot 0.3$
	- $\nu_{1}=\frac{1}{0.4}=2.5 \left( \checkmark \right)$
- $\nu_{2}=0$
#### **3.4.3**
Markov chain transition probability matrix is given as 
$$\mathbf{P}=\left\Vert \begin{matrix} 1 & 0 & 0 & 0  \\ 0.1 & 0.6 & 0.1 & 0.2 \\ 0.2 & 0.3 & 0.4 & 0.1 \\ 0 & 0 & 0 & 1 \end{matrix} \right\Vert$$
**a) Starting in state 1, determine the probability that the Markov chain ends in state 0.**

$T = \min \left\{ n \geq 0 \mid X_{n}=0 \right\}$

Need to consider other probabilities
$$u_{i} = \operatorname{P} \left( X_{T}=0 \mid X_{0}= i \right)$$
- $u_{1}=0.1+0.6u_{1}+0.1u_{2}$
- $u_{2}=0.1+0.3u_{1}+0.4u_{2}$

We have the following system of equations
$$\begin{align}
\mathrm{u}&=\begin{bmatrix} 0.6  & 0.1  \\ 0.3  & 0.4 \end{bmatrix} \mathrm{u} +\begin{bmatrix} 0.1  \\ 0.1 \end{bmatrix} \\
\left( I-A \right) \mathrm{u} &= \begin{bmatrix} 0.1  \\ 0.1 \end{bmatrix} \\
\mathrm{u} &= \left( I-A \right)^{-1}\begin{bmatrix} 0.1  \\ 0.1 \end{bmatrix}\\
\mathrm{u} &= \begin{bmatrix} \frac{1}{3} \\
\frac{1}{3} \end{bmatrix}
\end{align}$$
**b) Determine the mean time to absorption.**
$$T = \min \left\{ n \geq 0 \mid X_{n}=0 \ \lor \ X_{n}=3   \right\}$$
$$\nu_{i}= \mathbb{E} \left[T \mid X_{0}=i\right]$$
- $\nu_{0}=0$
- $\nu_{1} = 1 + 0.6 \nu_{1}+ 0.1 \nu_{2}$ 
- $\nu_{2}=1+0.3 \nu_{1}+0.4 \nu_{2}$
- $\nu_{3}=0$

Solving system of equations
$$\begin{align}
\nu &= \begin{bmatrix} 0.6 & 0.1\\
0.3  & 0.4 \end{bmatrix} \nu + \begin{bmatrix} 1 \\
1 \end{bmatrix}\\
\implies \nu &= \begin{bmatrix} \frac{4}{3} \\ \frac{4}{3} \end{bmatrix}
\end{align}$$
#### **3.4.4**
$$T = \min \left\{ n \geq 0 \mid X_{n}=2 \right\}$$
want to find
$$\nu = \mathbb{E} \left[T \mid X_{0}=0\right]$$
- $\nu_{0}= \frac{1}{2} \nu_{0} + \frac{1}{2} \nu_{1}$
	- $\implies \nu_{0}= \frac{1}{2} \nu_{0}+ \frac{1}{2} \left(  \frac{1}{2} \nu_{0}+1 \right)$
	- $\nu_{0}=\frac{3}{4}\nu_{0}+ \frac{1}{2}$
	- $\nu_{0}=2$
- $\nu_{1}=\frac{1}{2}\nu_{0}+1$

#### **3.4.6**
Markov chain with probability transition matrix:
$$\mathbf{P} = \left\Vert \begin{matrix} 1 & 0 & 0 & 0 \\ 0.1 & 0.4 & 0.1 & 0.4 \\ 0.2 & 0.1 & 0.6 & 0.1 \\ 0 & 0 & 0 & 1 \end{matrix} \right\Vert$$
**a) Starting in state 1, determine the probability that the Markov chain ends in state 0.**

$$T = \min \left\{ n \geq 0 \mid X_{n}=0 \right\}$$
We want to find 
$$u = \operatorname{P} \left( X_{T}=0 \mid X_{0}=1 \right)$$
- $u_{1}=0.1+0.4u_{1}+0.1u_{2}$
- $u_{2}=0.2+0.1u_{1}+0.6u_{2}$

System of equations:
$$\begin{align}
\mathrm{u} &= \begin{bmatrix} 0.4  & 0.1  \\ 0.1  & 0.6 \end{bmatrix} \mathrm{u}  + \begin{bmatrix} 0.1 \\ 0.2 \end{bmatrix} \\
\implies \left( I-\begin{bmatrix} 0.4  & 0.1  \\ 0.1  & 0.6 \end{bmatrix} \right) \mathrm{u} &= \begin{bmatrix} 0.1 \\ 0.2 \end{bmatrix} \\
\mathrm{u} &= \left( I-\begin{bmatrix} 0.4  & 0.1  \\ 0.1  & 0.6 \end{bmatrix} \right)^{-1}\begin{bmatrix} 0.1 \\ 0.2 \end{bmatrix} \\
\mathrm{u} &= \begin{bmatrix} 0.261\\
0.565 \end{bmatrix} \left( \checkmark \right)
\end{align}$$
**b) Determine the mean time for absorption**

$$T = \min \left\{ n \geq 0 \mid X_{n}=0 \ \lor \ X_{n}=3 \right\}$$
and 
$$\nu_{i} = \mathbb{E} \left[T \mid X_{0}=i, \ i \in \left\{ 0,1,2,3 \right\} \right]$$
- $\nu_{0}=0$
- $\nu_{1} = 0.4 \nu_{1} + 0.1 \nu_{2}$
- $\nu_{2} = 0.1 \nu_{1}+0.6 \nu_{3}$
- $\nu_{3}=0$

# **3.6 - Functionals of Random Walks and Success Runs**

$$X_{n+1}=X_{n}+Z_{n+1}, \quad Z_{n} \ \text{ is } \ i.i.d$$
## **Simple Random Walk**

$$X_{n+1}=X_{n}+\Delta_{n+1}, \quad \left\vert \Delta_{n}   \right\vert \leq 1 \ \text{ and } \ i.i.d$$
## **Unrestricted/Restricted Random Walks**

Defining an upper + lower bound on the state $X_{n}$

## **Gambler's Ruin Problem**

$$\mathbf{P} = \left\Vert \begin{matrix} 1 & 0 & 0 & 0 & \cdots & 0 \\ q & 0 & p & 0 & \cdots  & 0 \\ 0 & q & 0 & p & \cdots  & 0 \\ \vdots  & \vdots  & \vdots  & \vdots  &   &  \vdots  \\ 0 & 0 & 0 & 0 & \cdots  & 1 \end{matrix} \right\Vert$$
Time of absorption:
$$T = \min \left\{ n \geq 0; X_{n}=0 \text{ or } X_{n}=N \right\}$$
Considering the probability of being absorbed in state $0$.

$$u_{k}=\operatorname{P} \left( X_{T}=0 \mid X_{0}=k \right)$$

Performing a first-step analysis leas to the equation:
$$u_{k} = p u_{k+1} + q u_{k-1}$$
With the boundary conditions
$$u_{0}=1, \quad u_{N}=0$$
Formulating recursive definition of $u_{k+1}$

We know that $p+q=1$, therefore:
$$\begin{align}
(p+q)u_{k} &= p u_{k+1} + q u_{k-1} \\
\implies q \left( u_{k}-u_{k-1} \right) &= p \left( u_{k+1}-u_{k} \right)\\
\implies u_{k+1}-u_{k} &= \frac{q}{p} \left( u_{k}-u_{k-1} \right)
\end{align}$$
$$\vdots$$
$$u_{k} = \begin{cases} \dfrac{N-K}{N}  & p=q \\ \dfrac{\left( \dfrac{q}{p} \right)^{k}-\left( \dfrac{q}{p} \right)^{N}}{1-\left( \dfrac{q}{p} \right)^{N}}  &  p \neq q \end{cases}$$

**Indicator function:**
$$\mathbb{1} \left( X_{k}=j \right) = \begin{cases}0,  &  X_{k}\neq j \\ 1,  & X_{k}=j  \end{cases}$$


**Expected time in transient state:**

$$\begin{align}
W_{ij} &= \mathbb{E} \left( \sum\limits_{k=0}^{n} \mathbb{1} \left( X_{k}=j \right) \mid X_{0}=i \right) \\
&= \sum\limits_{k=0}^{n} \mathbb{E} \left( \mathbb{1}\left( X_{n} =j\right) \mid X_{0}=i \right)
\end{align}$$






- Transient states $0 \rightarrow r$

## **Exercises**
#### **3.6.1**

Rat in a maze. States are $X_{n} \in \left\{ 0 (\text{shock}),1,2,3,4,5 (\text{food})\right\}$.

**a) Assume that the rat is equally likely to move right or left at each step. What is the probability that the rat finds the food before getting shocked?**

Probability transition matrix:

$$\mathbf{P}= \left\Vert \begin{matrix} 0 & 1 & 0 & 0 & 0 & 0 \\ \frac{1}{2} &  0  &  \frac{1}{2}  & 0 & 0 & 0  \\ 0 &  \frac{1}{2}  & 0 &  \frac{1}{2}  & 0  & 0 \\ 0 & 0 &  \frac{1}{2}  & 0 &  \frac{1}{2}  & 0 \\  0 & 0 & 0 &  \frac{1}{2}  & 0 &  \frac{1}{2}  \\ 0 & 0 & 0 & 0 & 1  & 0 \end{matrix} \right\Vert$$
Probability to be found, is the probability of reaching state $X_{n}=5$ before reaching state $X_{n}=0$.

$$\begin{align}
u_{1} &= \frac{1}{2} u_{2} \\
u_{2} &= \frac{1}{2}u_{1} + \frac{1}{2}u_{3}\\
u_{3} &= \frac{1}{2}u_{2}+\frac{1}{2}u_{4} \\
u_{4}&=  \frac{1}{2} u_{3} +  \frac{1}{2} 
\end{align}$$
System of equations
$$\begin{align}
\mathrm{u} &= \begin{bmatrix} 0 & \frac{1}{2}  & 0 & 0  \\ \frac{1}{2} & 0 & \frac{1}{2} & 0 \\ 0  & \frac{1}{2} & 0 & \frac{1}{2}  \\ 0 & 0 & \frac{1}{2} & 0 \end{bmatrix} \mathrm{u + \begin{bmatrix} 0 \\ 0 \\ 0 \\ \frac{1}{2} \end{bmatrix}} \\
\implies \mathrm{u} &= \begin{bmatrix} 0.2\\ 0.4\\ 0.6 \\0.8 \end{bmatrix}
\end{align}$$
**Actual question**

Probability transition matrix:

$$\mathbf{P}= \left\Vert \begin{matrix} 1 & 0 & 0 & 0 & 0 & 0 \\ \frac{1}{2} &  0  &  \frac{1}{2}  & 0 & 0 & 0  \\ 0 &  \frac{1}{2}  & 0 &  \frac{1}{2}  & 0  & 0 \\ 0 & 0 &  \frac{1}{2}  & 0 &  \frac{1}{2}  & 0 \\  0 & 0 & 0 &  \frac{1}{2}  & 0 &  \frac{1}{2}  \\ 0 & 0 & 0 & 0 & 0  & 1 \end{matrix} \right\Vert$$
Formally:

$$T = \min \left\{ n \geq 0 \mid X_{n}=5 \right\}$$
Probability of ending up in state $5$, starting in any state $k \in \left\{ 1,2,3,4 \right\}$
$$\begin{align}
\operatorname{P} \left( X_{T}=5 \mid X_{0}=k \right) &=1-\operatorname{P} \left( X_{T}=0 \mid X_{0}=k \right)\\
\implies \operatorname{P} \left( X_{T}=5 \mid X_{0}=k \right) &= 1-u_{k} \\
\end{align}$$
Since $\theta=\frac{q}{p}=1 \implies u_{k} = \frac{N-k}{N}$
$$\begin{align}
\therefore \operatorname{P} \left( X_{T}=5 \mid X_{0}=k \right) &= 1-\frac{5-3}{5}\\
&= 1- \frac{2}{5}\\
&= \frac{3}{5}
\end{align}$$
**b) As a result of learning, at each step the rat moves to the right with probability $p > \frac{1}{2}$ and to the left with probability $q=1−p<\frac{1}{2}$ . What is the probability that the rat finds the food before getting shocked?**

Probability now becomes 