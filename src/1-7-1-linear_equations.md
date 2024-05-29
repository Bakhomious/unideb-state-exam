---
title: 'System of Linear Equations'
geometry: margin=1in
fontsize: 12pt
colorlinks: true
---

**Example** A manufacturer produces two kinds of toys: wooden cars and wooden trains. The amounts of two raw materials needed to product 1 piece of toys are given in the table.

|  | car | train |
| ---: | ---: | ---: |
| wood | 2 | 3 |
| paint | 5 | 4 |

Determine the number of cars and trains produced on a given day, when we know that for the production there were used 540 units of wood and 1070 units of paint.

## Systems of linear equations (SLE)

### Definition

The system of equations

$$
\begin{aligned}
&\begin{aligned}
& a_{11} x_1+a_{12} x_2+\cdots+a_{1 n} x_n=b_1 \\
& a_{21} x_1+a_{22} x_2+\cdots+a_{2 n} x_n=b_2 \\
& \vdots  
\end{aligned}\\
&a_{m 1} x_1+a_{m 2} x_2+\cdots+a_{m n} x_n=b_m
\end{aligned}
$$

where the numbers $a_{i j}(i \in\{1, \ldots, m\}, j \in\{1, \ldots, n\})$ and $b_{k}$ $(k \in\{1, \ldots, m\})$ are known, the variables $x_{1}, \ldots, x_{n}$ are unknown, is called a system of linear equations.

- $a_{i j}$ : the coefficients of the system of linear equations
- $b_{k}$ : the constant terms

----

The coefficient matrix and the augmented matrix:

$$
A=\left(\begin{array}{ccc}
a_{11} & \ldots & a_{1 n} \\
a_{21} & \ldots & a_{2 n} \\
\vdots & & \vdots \\
a_{m 1} & \ldots & a_{m n}
\end{array}\right) \quad \text { and } \quad A|b=\left(\begin{array}{ccc|c}
a_{11} & \ldots & a_{1 n} & b_{1} \\
a_{21} & \ldots & a_{2 n} & b_{2} \\
\vdots & & \vdots & \vdots \\
a_{m 1} & \ldots & a_{m n} & b_{m}
\end{array}\right).
$$

The right-hand side vector and the solution vector

$$
b=\left(\begin{array}{c}
b_{1} \\
b_{2} \\
\vdots \\
b_{m}
\end{array}\right) \quad \text { and } \quad x=\left(\begin{array}{c}
x_{1} \\
x_{2} \\
\vdots \\
x_{n}
\end{array}\right)
$$

The corresponding matrix-vector equation: $A x=b$.

## Solvability of systems of linear equations

### Definition

The system of linear equations is

- solvable if there exists at least one solution, that is, an $x$ such that $A x=b$ holds; determined if there is exactly 1 solution; undetermined if there are more than 1 solutions;
- inconsistent if it doesn't have a solution.

### Remark

The SLE can be solved if and only if the vector $b$ can be expressed as a linear combination of the column vectors of $A$. This means, that $b$ is in the subspace spanned by the column vectors of $A$.

If $b$ can be expressed uniquely (i.e. the columns vectors of $A$ are linearly independent), then there exists a unique solution.

If the column vectors of $A$ are linearly dependent, and $b$ is in the subspace spanned by the column vectors of $A$, then there are infinitely many solutions.

### Definition

The rank of a matrix is the rank of the system of column vectors of the matrix. Notation: $\operatorname{rank}(A)$.

### Condition on solvability

- A system of lin. eq.s is solvable if, and only if $\operatorname{rank}(A)=\operatorname{rank}(A \mid b)$.
- If it is solvable and $\operatorname{rank}(A)=n$ (where $n$ is the number of unknown parameters), then the system is determined, if $\operatorname{rank}(A)<n$, then undetermined.

## Solutions of a system of linear equations

### Definition

A system of linear equations is homogeneous if $b=0$, thus then the matrix equation has the form $A x=0$. Otherwise it's called nonhomogeneous.

**Remark:** 0 is a solution of any homogenous system of linear equations (it is the trivial solution).

### Theorem

A homogeneous system of linear equations has a nontrivial solution if and only if the column vectors of $A$ are linearly dependent.

### Solutions of a homogeneous system of linear equations

The solutions of a real homogeneous system of linear equations form a vector subspace of $\mathbb{R}^{n}$ with dimension $n-\operatorname{rank}(A)$.

### Solutions of a nonhomogeneous system of linear equations

The solutions of a (solvable) nonhomogeneous system of linear equations $A x=b$ are of the form $x^{*}+y$, where

- $x^{*}$ is a particular solution of the system of linear equations;
- $y$ is an arbitrary solution of the corresponding homogeneous system of linear equation, that is $A x=0$.

### Solving a system of linear equations with Gaussian elimination

The set of solutions of a system of linear equations does not change, if we

- multiply an equation by a nonzero constant;
- add a scalar multiple of an equation to another equation;
- interchange two equations;
- discard an equation which is a scalar multiple of another equation.

We eliminate the numbers under the main diagonal with the modifications above. The resulting system is easier to solve.

----

- If during the process we obtain a row like $(0 \ldots 0 \mid \neq 0)$, then the system of linear equations has no solution.
- If at the end of the process there are $n$ number of not identically 0 rows, then the system is determined (there is a unique solution), if fewer number of rows remains, then undetermined (infinitely many solutions). (Here $n$ is the number of the unknown parameters.)

### Example

Solve the system $A x=b$ using Gaussian elimination. .

$$
A=\left(\begin{array}{rrr}
2 & 2 & 3 \\
-4 & -1 & -5 \\
-2 & 4 & 0
\end{array}\right), \quad b=\left(\begin{array}{r}
-4 \\
12 \\
10
\end{array}\right)
$$

**Solution:**

$$
\begin{gathered}
\left(\begin{array}{rrr|r}
2 & 2 & 3 & -4 \\
-4 & -1 & -5 & 12 \\
-2 & 4 & 0 & 10
\end{array}\right) \longrightarrow\left(\begin{array}{rrr|r}
2 & 2 & 3 & -4 \\
0 & 3 & 1 & 4 \\
0 & 6 & 3 & 6
\end{array}\right) \\
\longrightarrow\left(\begin{array}{rrr|r}
2 & 2 & 3 & -4 \\
0 & 3 & 1 & 4 \\
0 & 0 & 1 & -2
\end{array}\right)
\end{gathered}
$$

$$
\left(\begin{array}{lll|r}
2 & 2 & 3 & -4 \\
0 & 3 & 1 & 4 \\
0 & 0 & 1 & -2
\end{array}\right)
$$

Backward substitution:

$$
\begin{aligned}
& x_{3}=-2 \\
& 3 x_{2}+x_{3}=4 \quad \rightarrow x_{2}=2 \\
& 2 x_{1}+2 x_{2}+3 x_{3}=-4 \quad \rightarrow x_{1}=-1
\end{aligned}
$$

## Rank, Determinant

The following operations do not change the rank of a matrix $A$ :

- Interchanging 2 rows of $A$.
- Multiplying a row of $A$ by a scalar $\lambda \neq 0$.
- Adding a scalar multiple of a row to another row.
- The determinant doesn't change if we add a scalar multiple of a row to another row.
- If we interchange 2 rows of $A$, then the sign of the determinant changes.
- The determinant of a triangular matrix is the product of the elements of the main diagonal.

$\Longrightarrow$ Gaussian elimination can be used for computation of $\operatorname{rank}(A)$ and $\operatorname{det}(A)$.

### Example

Calculate $\operatorname{rank}(A)$ and $\operatorname{det}(A)$.

$$
A=\left(\begin{array}{rrr}
3 & 5 & -6 \\
-1 & -2 & 1 \\
2 & 6 & 5
\end{array}\right)
$$

**Solution:**

$$
\begin{aligned}
& A=\left(\begin{array}{rrr}
3 & 5 & -6 \\
-1 & -2 & 1 \\
2 & 6 & 5
\end{array}\right) \longrightarrow\left(\begin{array}{rrr}
-1 & -2 & 1 \\
3 & 5 & -6 \\
2 & 6 & 5
\end{array}\right) \longrightarrow\left(\begin{array}{rrr}
-1 & -2 & 1 \\
0 & -1 & -3 \\
0 & 2 & 7
\end{array}\right) \\
& \longrightarrow\left(\begin{array}{rrr}
-1 & -2 & 1 \\
0 & -1 & -3 \\
0 & 0 & 1
\end{array}\right) \quad \Longrightarrow \quad \operatorname{rank}(A)=3
\end{aligned}
$$

The determinant of the last matrix is $(-1)(-1) \cdot 1=1$. During the calculations we interchanged the rows of $A$ only once, so $\operatorname{det}(A)=-1$.
