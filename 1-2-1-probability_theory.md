---
title: 'Probability Theory'
geometry: margin=1in
fontsize: 12pt
colorlinks: true
---

**Random experiment**: the outcome of the experiment is not determined before performing the experiment.

**Outcome:** An outcome of an experiment is any possible observation of that experiment. 

**Sample Space:** The sample space of an experiment is the finest-grain, mutually exclusive, collectively exhaustive set of all possible outcomes. ($\Omega$)

**Event:** An event is a set of outcomes of an experiment. Subset of $\Omega$.

**Event Space:** An event space is a collectively exhaustive, mutually exclusive set of events.

### Axioms of Probability

$\text{Axiom 1: For any event A, } P[A] \geq 0$

$\text{Axiom 2: } P[S] = 1$

$\text{Axiom 3: For any countable collection } A_1, A_2, \dots \text {of mutually exclusive events}$

$$
P[A_1 \,\cup A_2 \, \cup \dots] = P[A_1] + P[A_2] + \dots
$$

### Theorem

$\text{For an experiment with sample Space } S = \{s_1,\dots,s_n\} \text { in which each outcome } s_i \text{ is equaly likely}$

$$
P[s_i] = 1/n \quad 1\leq i\leq n
$$

Proof using axiom 2.

### Theorem

$\text{The probability measure } P[\cdot] \text{ satisfies}$

$\textit{(a) } P[\phi] = 0$

$\textit{(b) } P[A^c] = 1 - P[A]$

$\textit{(c) } \text {For any A and B (not necessarily disjoint), }$

$$
P[A \cup B] = P[A] + P[B] - P[A \cap B]
$$

$\textit{(d) } \text{If } A \subset B \text{ ,then } P[A] \leq P[B]$

### Conditional Probability

*The conditional probability of the event A given the occurrence of the event B is*

$$
P[A|B] = \frac{P[AB]}{P[B]}
$$

### Law of Total Probability

$\textit{For an event space } \{B_1, B_2, \dots, B_m\} \, \, with P[B_i] > 0 \text{ for all i,}$

$$P[A] = \sum_{i=1}^{m} P[A|B_i] \, \,P[B_i]$$

### Bayes’ Theorem

In many situations, we have advance information about ***P[A|B]*** and need to calculate ***P[B|A]***. To do so we have the following formula: *proved using Conditional Probability.*

$$
P[B|A] = \frac{P[A|B] \, \, P[B]}{P[A]}
$$

### Independence

Events A and B are independent if and only if

$$
P[AB] = P[A] \, \, P[B]
$$

When events A and B have nonzero probabilities, the following formulas are equivalent to the definition of independent events:

$$P[A|B] = P[A], \quad P[B|A] = P[B]$$

**3 Independent Events**

$A_1, A_2 \text{, and } A_3$ are ***independent*** if and only if

(a) $A_1$ and $A_2$ are independent,

(b) $A_2$ and $A_3$  are independent,

(c) $A_1$ and $A_3$ are independent,

(d) $P[A_1 \cap A_2 \cap A_3] = P[A_1] P[A_2]P[A_3].$

**More than Two Independent Events**

If $n \geq 3$, the sets $A_1, A_2, \dots,A_n$  are independent if and only if

(a) every set on $n-1$ sets taken from $A_1, A_2, \dots,A_n$ is independent,

(b) $P[A_1 \cap A_2 \cap \dots \cap A_3 ] = P[A_1] P[A_2]\dots P[A_n]$

---

## **Fundamental Principle of Counting**

If subexperiment *A* has *n* possible outcomes, and subexperiment *B* has *k* possible outcomes, then there are *nk* possible outcomes when you perform both subexperiments.

### Theorem

The number of *k*-permutations of *n* distinguishable objects is

$$(n)_k = \frac{n!}{(n-k)!}$$

## Sample without Replacement

### Theorem

The number of ways to choose **k** objects out of **n** distinguishable objects is

$$
{n \choose k} = {n \choose n-k}
$$

$\text{n choose k}$

$\text {For an integer} \geq 0 \text{, we define}$

$$
{n \choose k} = \begin{cases}
{\frac{n!}{k!(n-k)!}} \quad k = 0,1, \dots, n\\
0 \quad \quad \quad \quad \text{otherwise.}
\end{cases}
$$

## Sample with Replacement

### Theorem

Given *m* distinguishable objects, there are $m^n$ ways to choose with replacement an ordered sample of *n* objects.

---

## Permutations:

**Definition:** An ordered sequence of *n* distinguishable objects is called an *n*-permutation.
**Theorem:** The number of *n*-permutations is *n*-factorial, that is $n! = n \cdot (n-1) \cdots 2 \cdot 1$ 
$0! = 1$ 

### Identical Elements

Let *h* red, *k* blue and *m* white elements *(h + k + m = n)*. Denote by *X* the number of permutations of these *n* elements. Then
$$
X h! k! m! = n!
$$
So,
$$
X = \frac{n!}{h!k!m!}
$$

## Ordered Selections

### Without Replacement

**Theorem:** The number of ordered selections without replacement is
$$
n \cdot(n-1) \cdot (n-2) \cdots (n-k+1) = \frac{n!}{(n-k)!}
$$

### With Replacement

**Theorem:** The number of ordered selections with replacement is
$$
n \cdot n \cdots n \cdot n = n^k
$$

## Combinations

*Order is not important.*
**Theorem:** The number of ways to choose *k* objects out of *n* distinguishable objects is
$$ {n \choose k} \text{, where }{n \choose k} = \frac{n!}{k!(n-k)!}$$

### With Replacement

**Theorem:** The number of ways to choose *k* objects out of *n* distinguishable objects when we replace the chosen elements is
$${n+k-1 \choose k}$$

## Binomial Theorem

$$
(a+b)^n = \sum^{n}_{k=0} {n \choose k} a^{n-k}b^k = {n \choose 0}a^nb^0 + {n \choose 1}a^{n-1}b^1 + \dots + {n \choose n} a^0b^n.
$$
The binomial coefficients are contained in the Pascal triangle. 
**Remark:** The rule of the Pascal triangle is
$$
{n+1 \choose k+1} = {n \choose k+1} + {n \choose k}
$$

## Number of Subsets

**Theorem:** The number of subsets of an *n*-element set is $2^n$.
