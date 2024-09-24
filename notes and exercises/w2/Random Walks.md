## The General Random Walk

The general random walk probability transition matrix
$$\begin{align}
\mathbf{P}=\left\Vert \begin{matrix} 1 & 0 & 0 & 0 & \cdots  & 0\\
q_{1} & r_{1} & p_{1} & 0 & \cdots  & 0\\
0 & q_{2} & r_{2} & p_{2} & \cdots  & 0\\
\vdots  & \vdots  & \vdots & \vdots  &   & \vdots\\
0 & 0 & 0 & 0 & \cdots  & 1  \end{matrix} \right\Vert
\end{align}$$
Where $q_{k} > 0$ and $p_{k}>0$ for $k=1, \dots , N-1$. Let $T = \min \left\{ n \geq 0; X_{n}=0 \ \lor \ X_{n}=0 \right\}$, i.e., the hitting time for states $0$ and $N$.

**Case where transition probabilities are the same from row to row:**

$$p \geq 0, \quad q \geq 0, \quad p+q+r = 1$$
Making some abbreviations

$$\rho_{k}= \frac{q_{1}q_{2}\cdots q_{k}}{p_{1}p_{2}\cdots p_{k}}= \left( \frac{q}{p} \right)^{k}=\theta^{k}, \quad \text{for } k=1, \dots , N-1$$
The **probability of gambler's ruin** (i.e., the process being absorbed in state $0$ before reaching state $N$) becomes
$$\begin{align}
u_{k} &= \operatorname{P} \left( X_{T}=0 \mid X_{0}=k \right) \\
&= \frac{\theta^{k}+\cdots + \theta^{N-1}}{1+\theta+\cdots +\theta^{N-1}} \\
&= \begin{cases} \dfrac{\theta^{k}-\theta^{N}}{1-\theta^{N}}, \quad \text{if } p \neq q \\
\dfrac{N-k}{N}, \quad \text{if } p=q\end{cases}
\end{align}$$
**Mean time** before absorption
$$\nu_{k}=\mathbb{E}\left[T \mid X_{0}=k\right], \quad \text{for } k=1, \dots , N-1$$
by first substituting $\rho_{i}=\theta_{i}$ into 

$$\vdots  \text{ (a lot of workings)}$$
$$\begin{align}
\nu_{i} &= \mathbb{E} \left[T \mid X_{0}=i\right] \\
&= \begin{cases} \dfrac{i \left( N-i \right)}{2p}, \quad \text{if } p=q \\
\dfrac{1}{p \left( 1-\theta \right)} \left[N \left( \dfrac{1-\theta^{i}}{1- \theta^{N}} \right)-i\right], \quad q \neq p \end{cases}
\end{align}$$
