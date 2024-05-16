---
title: 'Probability Distributions'
geometry: margin=1in
fontsize: 12pt
colorlinks: true
---

## Random Variables

A random variable $X$ is a function from the sample space to the real numbers.

$$
X : S \to \mathbb{R}
$$

The range of a random variable $X$, shown by Range($X$) or $R_X$, is the set of possible values of $X$.

### Discrete Random Variables

$X$ is a discrete random variable, if its range is countable. For example, rolling a dice which results in 6 different outputs ($1, 2, \dots 6$) with equally likely chances of being rolled (i.e. $\frac{1}{6}$).

It has a discrete probability which is calculated on exact points.

Examples of distributions: [Binomial](#binomial-distribution), [Poisson](#poisson-distribution)

#### Probability Mass Function

Let *X* be a discrete random variable with range $R_X = \{ x1,x2,x3, \dots \}$ (finite or countably infinite). The function

$$
P_X(x_k) = P(X = x_k), \text{ for } k = 1, 2, 3, \dots
$$

is called the probability mass function (PMF) of $X$.

### Continuous Random Variables

$X$ is a continuous random variable, if its range is uncountable. For example, the time it takes to complete an exam is 60 minutes, possible values are all the real numbers on the interval $[0,60]$.

It has a continuous probability which is measured over intervals.

Examples of distributions: [Exponential](#exponential-distribution), [Uniform](#uniform-distribution), [Normal](#normal-distribution)

#### Probability Density Function

Consider a continuous random variable $X$ with PDF $f_{X}(x)$. We have

1. $f_{X}(x) \geq 0$ for all $x \in \mathbb{R}$.

2. $\int_{-\infty}^{\infty} f_{X}(u) \, \, d u=1$.

3. $P(a<X \leq b)=F_{X}(b)-F_{X}(a)=\int_{a}^{b} f_{X}(u) \, \, d u$.

----

## Expectation

If you have a collection of numbers $a_1, a_2, \ldots, a_N$, their average is a single number that describes the whole collection. Now, consider a random variable $X$. We would like to define its average, or as it is called in probability, its expected value or mean. The expected value is defined as the weighted average of the values in the range.

### Definition

Let $X$ be a discrete random variable with range $R_X=\left\{x_1, x_2, x_3, \ldots\right\}$ (finite or countably infinite). The expected value of $X$, denoted by $E X$ is defined as

$$
E X=\sum_{x_k \in R_X} x_k \mathrm{P}\left(X=x_k\right)=\sum_{x_k \in R_X} x_k P_X\left(x_k\right) .
$$

----

## Variance

The variance is a measure of how spread out the distribution of a random variable is.

### Definition

The variance of a random variable $X$, with mean $E X=\mu_{X}$, is defined as

$$
\operatorname{Var}(X)=E\left[\left(X-\mu_{X}\right)^{2}\right] .
$$

with the computational formula

$$
\operatorname{Var}(X)=E\left[X^{2}\right]-[E X]^{2}
$$

----

## Binomial Distribution

The random experiment behind the binomial distribution is as follows. Suppose that I have a coin with $P(H)=p$. I toss the coin $n$ times and define $X$ to be the total number of heads that I observe. Then $X$ is binomial with parameter $n$ and $p$, and we write $X \sim \operatorname{Binomial}(n, p)$. The range of $X$ in this case is $R_X=\{0,1,2, \ldots, n\}$.

$$
P_X(k)=\binom{n}{k} p^k(1-p)^{n-k}, \text { for } k=0,1,2, \ldots, n
$$

### Definition

A random variable $X$ is said to be a binomial random variable with parameters $n$ and $p$, shown as $X \sim \operatorname{Binomial}(n, p)$, if its PMF is given by

$$
P_X(k)= \begin{cases}\binom{n}{k} p^k(1-p)^{n-k} & \text { for } k=0,1,2, \cdots, n \\ 0 & \text { otherwise }\end{cases}
$$
where $0<p<1$

### Expectation

Using the *linearity of expectation* we can deduce the expectation of a binomial distribution to be $EX = np$.

$$
\begin{aligned}
E X & =E\left[X_1+X_2+\cdots+X_n\right] \\
& =E X_1+E X_2+\cdots+E X_n \\
& =p+p+\cdots+p \\
& =n p
\end{aligned}
$$

### Variance

$$
\operatorname{Var}\left(X_i\right)=E\left[X_i^2\right]-\left(E X_i\right)^2=1^2 \cdot p+0^2 \cdot(1-p)-p^2=p(1-p)
$$

Thus,
$$
\begin{aligned}
\operatorname{Var}(X) & =p(1-p)+p(1-p)+\cdots+p(1-p) \\
& =n p(1-p) .
\end{aligned}
$$

## Poisson Distribution

In practice, it is often an approximation of a real-life random variable. Here is an example of a scenario where a Poisson random variable might be used. Suppose that we are counting the number of customers who visit a certain store from $1 \mathrm{pm}$ to $2 \mathrm{pm}$. Based on data from previous days, we know that on average $\lambda=15$ customers visit the store. Of course, there will be more customers some days and fewer on others. Here, we may model the random variable $X$ showing the number customers as a Poisson random variable with parameter $\lambda=15$.

### Definition

A random variable $X$ is said to be a Poisson random variable with parameter $\lambda$, shown as $X \sim \operatorname{Poisson}(\lambda)$, if its range is $R_{X}=\{0,1,2,3, \ldots\}$, and its PMF is given by

$$
P_{X}(k)= \begin{cases}\frac{e^{-\lambda} \lambda^{k}}{k !} & \text { for } k \in R_{X} \\ 0 & \text { otherwise }\end{cases}
$$

### Expectation

$$
\begin{aligned}
E X & =\sum_{x_{k} \in R_{X}} x_{k} P_{X}\left(x_{k}\right) \\
& =\sum_{k=0}^{\infty} k \frac{e^{-\lambda} \lambda^{k}}{k !} \\
& =e^{-\lambda} \sum_{k=1}^{\infty} \frac{\lambda^{k}}{(k-1) !} \\
& =e^{-\lambda} \sum_{j=0}^{\infty} \frac{\lambda^{(j+1)}}{j !} \quad(\text { by letting } j=k-1) \\
& =\lambda e^{-\lambda} \sum_{j=0}^{\infty} \frac{\lambda^{j}}{j !} \quad\left(\text { Taylor series for } e^{\lambda}\right) \\
& =\lambda e^{-\lambda} e^{\lambda} \\
& =\lambda .
\end{aligned}
$$

### Variance

$$
\begin{aligned}
\mathrm{E}[X(X-1)] & =\sum_{x=0}^{\infty} x(x-1) \cdot \frac{\lambda^{x} e^{-\lambda}}{x !} \\
& =\sum_{x=2}^{\infty} x(x-1) \cdot \frac{\lambda^{x} e^{-\lambda}}{x !} \\
& =e^{-\lambda} \cdot \sum_{x=2}^{\infty} x(x-1) \cdot \frac{\lambda^{x}}{x \cdot(x-1) \cdot(x-2) !} \\
& =\lambda^{2} \cdot e^{-\lambda} \cdot \sum_{x=2}^{\infty} \frac{\lambda^{x-2}}{(x-2) !} .
\end{aligned}
$$

Substituting $z=x-2$, such that $x=z+2$, we get:

$$
\mathrm{E}[X(X-1)]=\lambda^{2} \cdot e^{-\lambda} \cdot \sum_{z=0}^{\infty} \frac{\lambda^{z}}{z !} .
$$

Using the power series expansion of the exponential function

$$
e^{x}=\sum_{n=0}^{\infty} \frac{x^{n}}{n !},
$$

the expected value of $X(X-1)$ finally becomes

$$
\mathrm{E}[X(X-1)]=\lambda^{2} \cdot e^{-\lambda} \cdot e^{\lambda}=\lambda^{2} .
$$

Note that this expectation can be written as

$$
\mathrm{E}[X(X-1)]=\mathrm{E}\left(X^{2}-X\right)=\mathrm{E}\left(X^{2}\right)-\mathrm{E}(X),
$$

such that, we have:

$$
\mathrm{E}\left(X^{2}\right)-\mathrm{E}(X)=\lambda^{2} \Rightarrow \mathrm{E}\left(X^{2}\right)=\lambda^{2}+\lambda .
$$

The variance of a Poisson random variable finally becomes

$$
\operatorname{Var}(X)=\lambda^{2}+\lambda-\lambda^{2}=\lambda .
$$

## Uniform Distribution

A continuous random variable $X$ is said to have a Uniform distribution over the interval $[a, b]$, shown as $X \sim \operatorname{Uniform}(a, b)$, if its PDF is given by

$$
f_{X}(x)= \begin{cases}\frac{1}{b-a} & a<x<b \\ 0 & x<a \text { or } x>b\end{cases}
$$

### Expectation

$$
E X = \int_{a}^{b} \frac{x}{b-a} dx = \frac{1}{b-a}\left[\frac{b^2-a^2}{2}\right] = \frac{a + b}{2}
$$

### Variance

$$
\begin{aligned}
E X^{2} & =\int_{-\infty}^{\infty} x^{2} f_{X}(x) d x \\
& =\int_{a}^{b} x^{2}\left(\frac{1}{b-a}\right) d x \\
& =\frac{a^{2}+a b+b^{2}}{3} .
\end{aligned}
$$

Therefore,

$$
\begin{aligned}
\operatorname{Var}(X) & =E X^{2}-(E X)^{2} \\
& =\frac{(b-a)^{2}}{12} .
\end{aligned}
$$

## Exponential Distribution

A continuous random variable $X$ is said to have an exponential distribution with parameter $\lambda>0$, shown as $X \sim \operatorname{Exponential}(\lambda)$, if its PDF is given by

$$
f_{X}(x)= \begin{cases}\lambda e^{-\lambda x} & x>0 \\ 0 & \text { otherwise }\end{cases}
$$

### Expectation

$$
\begin{aligned}
E X & =\int_{0}^{\infty} x \lambda e^{-\lambda x} d x \\
& =\frac{1}{\lambda} \int_{0}^{\infty} y e^{-y} d y \\
& =\frac{1}{\lambda}\left[-e^{-y}-y e^{-y}\right]_{0}^{\infty} \\
& =\frac{1}{\lambda} .
\end{aligned}
$$

### Variance

$$
\begin{aligned}
E X^{2} & =\int_{0}^{\infty} x^{2} \lambda e^{-\lambda x} d x \\
& =\frac{1}{\lambda^{2}} \int_{0}^{\infty} y^{2} e^{-y} d y \\
& =\frac{1}{\lambda^{2}}\left[-2 e^{-y}-2 y e^{-y}-y^{2} e^{-y}\right]_{0}^{\infty} \\
& =\frac{2}{\lambda^{2}} .
\end{aligned}
$$

Thus, we obtain

$$
\operatorname{Var}(X)=E X^{2}-(E X)^{2}=\frac{2}{\lambda^{2}}-\frac{1}{\lambda^{2}}=\frac{1}{\lambda^{2}} .
$$

$$
\text { If } X \sim \text { Exponential }(\lambda) \text {, then } E X=\frac{1}{\lambda} \text { and } \operatorname{Var}(X)=\frac{1}{\lambda^{2}} \text {. }
$$

## Normal Distribution

We say a random variable has a normal distribution $X \sim \operatorname{N}(\mu, \sigma^2)$ if its PDF is given by: 

$$
f_{X}(x)= \frac{1}{\sigma \sqrt{2 \pi}} \exp \left\{-\frac{(x-\mu)^{2}}{2 \sigma^{2}}\right\}
$$

![PDF of the standard normal random variable](https://cdn.mathpix.com/cropped/2023_01_07_73c4fd5ec57186ac775cg-16.jpg?height=716&width=1155&top_left_y=1309&top_left_x=412)

### Expectation

$$
E X = 0
$$

### Variance

$$
\operatorname{Var}(X) = 1
$$
----

