---
title: 'Linear Algebra'
geometry: margin=1in
fontsize: 12pt
colorlinks: true
---

## Matrices

#### Definition

A matrix is a rectangular array of numbers. An $m \times n(m$-by- $n)$ matrix has $m$ rows and $n$ columns.
$$
A=\left(\begin{array}{cccc}
a_{11} & a_{12} & \ldots & a_{1 n} \\
a_{21} & a_{22} & \ldots & a_{2 n} \\
\vdots & \vdots & & \vdots \\
a_{m 1} & a_{m 2} & \ldots & a_{m n}
\end{array}\right)
$$

- the elements of $A$ are $a_{i j}$, notation: $A=\left(a_{i j}\right)$
- The set of the $m \times n$ real matrices is denoted by $\mathbb{R}^{m \times n}$, while the set of the $m \times n$ complex matrices is denoted by $\mathbb{C}^{m \times n}$.

Example.
$$
\left(\begin{array}{rrr}
-1 & 1 & 0 \\
4 & -3 & -1
\end{array}\right) \in \mathbb{R}^{2 \times 3}, \quad\binom{2-i}{3+2 i} \in \mathbb{C}^{2 \times 1}
$$

- If $n=m$, then the matrix is a square matrix.
- The main diagonal of a matrix is the vector $\left(a_{11}, a_{22}, a_{33}, \ldots,, a_{k k}\right)$, where $(k=\min \{m, n\})$.
- Two matrices are equal, if their sizes are equal and their elements in the same position are equal.
- The identity matrix of size $n$ is the $n \times n$ matrix such that the elements on the main diagonal are equal to 1 and all other elements are zero. Notation: $I_{n}$.

$$
I_{2}=\left(\begin{array}{ll}
1 & 0 \\
0 & 1
\end{array}\right) \quad I_{3}=\left(\begin{array}{lll}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right)
$$

### Matrix Addition

We can only add matrices of the same type.

If $A=\left(a_{i j}\right)$ and $B=\left(b_{i j}\right)$ are $m \times n$ matrices, then we calculate the sum elementwise: $C=A+B$, where $c_{i j}=a_{i j}+b_{i j}; \, i=1, \ldots, m, \, j=1, \ldots, n$.

### Scalar Multiplication

We do the scalar multiplication elementwise. That is, if $\lambda$ is a scalar, $A=\left(a_{i j}\right)$ is an $m \times n$ matrix, then $\lambda A=\left(\lambda a_{i j}\right)$, which is an $m \times n$ matrix, too.

Example.

$$
\left(\begin{array}{rr}
1 & -4 \\
0 & -2 \\
3 & 3
\end{array}\right)+\left(\begin{array}{rr}
2 & -1 \\
1 & 2 \\
1 & 5
\end{array}\right)=\left(\begin{array}{rr}
3 & -5 \\
1 & 0 \\
4 & 8
\end{array}\right), \quad 2 \cdot\left(\begin{array}{ll}
1 & 4 \\
0 & 2 \\
3 & 3
\end{array}\right)=\left(\begin{array}{ll}
2 & 8 \\
0 & 4 \\
6 & 6
\end{array}\right)
$$

### Matrix Multiplication

Let $A=\left(a_{i j}\right)$ be an $m \times k$ and $B=\left(b_{i j}\right)$ be a $k \times n$ matrix. Then the product of $A$ and $B \text { is }$ the $m \times n$ matrix $C=\left(c_{i j}\right)$, such that

$$
c_{i j}=\sum_{r=1}^{k} a_{i r} b_{r j}
$$

#### Properties of matrix multiplication

- If $A$ is an $m \times n$ matrix, then $I_{m} \cdot A=A$ and $A \cdot I_{n}=A$.
- If $A, B, C$ are matrices for which $A B$ and $B C$ exist, then $(A B) C=A(B C)$. (associativity)
- If $A$ and $B$ are of the same size and $A C$ exists, then $B C$ exists as well and $(A+B) C=A C+B C$. (distributivity)
- Matrix multiplication is not commutative, that is, in general $A B \neq B A$.

### Transposition

Let $A$ be an $m \times n$ matrix. The $n \times m$ matrix, which has rows as the columns of $A$ is denoted by $A^{T}$ and it is called the transpose of $A$.

Properties of transposition

- $\left(A^{T}\right)^{T}=A$
- $(A B)^{T}=B^{T} \cdot A^{T}$.


$$
\begin{aligned}
& A = \begin{pmatrix}
2 & 1 & -1 \\
0 & -2 & 3 
\end{pmatrix} \quad 2 \times 3 \quad
& A^{\top} = \begin{pmatrix}
2 & 0 \\
1 & -2 \\
-1 & 3 
\end{pmatrix} \quad 3 \times 2
\end{aligned}
$$

#### Definition

Let $A$ be a square matrix of order $n$. $A$ is called symmetric if $A^{T}=A$.

### The Inverse of a Matrix

A square matrix $A$ of order $n$ is called regular or it has an inverse if there exists a square matrix $B$ of order $n$, such that

$$
A B=B A=I_{n}
$$

#### Theorem

If $A$ is regular, then its inverse is uniquely determined. Notation: $A^{-1}$.

Example.

$$
A=\left(\begin{array}{ll}
4 & 3 \\
7 & 5
\end{array}\right) \quad A^{-1}=\left(\begin{array}{rr}
-5 & 3 \\
7 & -4
\end{array}\right)
$$

#### Properties of matrix inverse

- If $A$ is regular, then so is $A^{-1}$, and $\left(A^{-1}\right)^{-1}=A$.
- If $A$ and $B$ are regular and $A B$ exists, then $(A B)^{-1}=B^{-1} A^{-1}$.
- If $A$ is regular, then so is $A^{T}$, and $\left(A^{-1}\right)^{T}=\left(A^{T}\right)^{-1}$.

### Determinant

Let $A = (a_{i j})$ be a square matrix. Let us choose $n$ elements of $A$ such that we choose exactly one element from each row and each column. The chosen elements:

$$
a_{1 \sigma(1)}, a_{2 \sigma(2)}, \ldots, a_{n \sigma(n)}
$$

The determinant of $A$ is

$$
\operatorname{det}(A)=|A|=\sum_{\sigma} \varepsilon(\sigma) a_{1 \sigma(1)} a_{2 \sigma(2)} \ldots a_{n \sigma(n)} \cdot
$$

Here $\varepsilon(\sigma)=\left\{\begin{aligned} 1, & \text { if } \sigma \text { is even, } \\ -1, & \text { if } \sigma \text { is odd. }\end{aligned}\right.$

There are $n!$ terms in the sum above.

#### Theorem

If $A$ and $B$ are square matrices of the same size, then

$$
\operatorname{det}(A B)=\operatorname{det}(A) \cdot \operatorname{det}(B)
$$

#### Remark

- The determinant of an identity matrix is $1 .\left(\operatorname{det} I_{n}=1\right)$
- The determinant of a diagonal matrix is the product of the elements of the main diagonal.
- The determinant of a triangular matrix is the product of the elements in the main diagonal.

#### Properties of the determinant

- $\operatorname{det}(A)=\operatorname{det}\left(A^{T}\right)$
- If $A$ has a row full of zeros, then $\operatorname{det}(A)=0$.
- If we interchange 2 rows of $A$, then the sign of the determinant changes.
- If one row of $A$ is a scalar multiple of another row, then $\operatorname{det}(A)=0$.
- If we multiply a row of $A$ by a real number $\lambda$, then the obtained matrix has determinant $\lambda \cdot \operatorname{det}(A)$.
- If we multiply each row of $A$ by a real number $\lambda$, then the obtained matrix has determinant $\lambda^{n} \cdot \operatorname{det}(A)$.
- The determinant doesn't change if we add a scalar multiple of a row to another row.
- If a row of $A$ is the linear combination of the other rows, then $\operatorname{det}(A)=0$.
- The properties above are true if we consider columns instead of rows.

#### Corollary

If $\operatorname{det}(A) \neq 0$, then the rows (or columns) of $A$ are linearly independent vectors. Then if $A \in \mathbb{R}^{n \times n}$ : its rows form a basis of $\mathbb{R}^{n}$.

### Calculating the Determinant

#### Rule of Sarrus

Only for $2 \times 2$ and $3 \times 3$ determinants. 

for $2 \times 2$ matrices:

$$
A=\left(\begin{array}{ll}
a_{11} & a_{12} \\
a_{21} & a_{22}
\end{array}\right) \Longrightarrow \operatorname{det}(A)=a_{11} a_{22}-a_{12} a_{21}
$$

for $3 \times 3$ matrices:


$$
A=\left(\begin{array}{lll}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33}
\end{array}\right)
$$

To apply the Sarrus rule, we extend the matrix by writing the first two columns to the right of the matrix:
$$
\left(\begin{array}{lll|ll}
a_{11} & a_{12} & a_{13} & a_{11} & a_{12} \\
a_{21} & a_{22} & a_{23} & a_{21} & a_{22} \\
a_{31} & a_{32} & a_{33} & a_{31} & a_{32}
\end{array}\right)
$$
$$
\Longrightarrow \operatorname{det}(A)= a_{11} a_{22} a_{33}+a_{12} a_{23} a_{31}+a_{13} a_{21} a_{32}-a_{13} a_{22} a_{31}-a_{12} a_{21} a_{33}-a_{11} a_{23} a_{32}
$$

#### Gaussian Elimination

Using the following two modifications transform the matrix to triangular form.

- Interchanging two rows (the determinant changes sign).
- Adding a scalar multiple of a row to another row. (the determinant does not change)

The determinant of the original matrix is the product of the elements in the main diagonal of the triangular matrix, multiplied by $(-1)^{k}$, where $k$ is the number of the performed row interchanges.

#### Laplace Expansion

We choose an arbitrary row or column of the matrix. E.g., if we choose the $i^{\text {th }}$ row, then

$$
\operatorname{det}(A)=|A|=\sum_{j=1}^{n} a_{i j} C_{i j}, \quad \text { where }
$$

- $C_{i j}$ is the cofactor of $A$ corresponding to the element $a_{i j}$, that is,

$$
C_{i j}=(-1)^{i+j} A_{i j}
$$

- $A_{i j}$ is the $(n-1) \times(n-1)$ determinant obtained from $A$ by deleting the $i^{\text {th }}$ row and $j^{\text {th }}$ column of $A$.

### Determinant and Matrix Inverse

#### Definition

The square matrix $A$ is called regular if $\operatorname{det}(A) \neq 0$. Otherwise $A$ is said to be singular.

**Theorem:**

A matrix has an inverse if, and only if, it is regular. (That is, its determinant is non-zero.)

**Proposition:**

If $A$ is regular, then

$$
\operatorname{det}(A)^{-1}=\operatorname{det}\left(A^{-1}\right)
$$

If the $2 \times 2$ matrix

$$
A=\left(\begin{array}{ll}
a_{11} & a_{12} \\
a_{21} & a_{22}
\end{array}\right)
$$

is regular, then its inverse is

$$
A^{-1}=\frac{1}{\operatorname{det}(A)}\left(\begin{array}{rr}
a_{22} & -a_{12} \\
-a_{21} & a_{11}
\end{array}\right)
$$

### Rank

The rank of a matrix is the rank of the system of column vectors of the matrix. Notation: $\operatorname{rank}(A)$.

----

## Linear Maps

From the properties of matrix operations:

- $A(u+v)=A u+A v, \forall u, v \in \mathbb{R}^{n}$
- $A(\lambda u)=\lambda(A u), \forall v \in \mathbb{R}^{n}, \lambda \in \mathbb{R}$

### Definition

Let $V$ and $W$ be a vector spaces. $\varphi: V \rightarrow W$ is a linear map if it is

- additive, that is $\forall u, v \in V: \varphi(u+v)=\varphi(u)+\varphi(v)$;
- homogeneous, that is $\forall v \in V, \lambda \in \mathbb{R}: \varphi(\lambda v)=\lambda \varphi(v)$.

If $V=W$ then we call the linear map linear transformation.

----

Hence, in the case of $A \in \mathbb{R}^{m \times n}$ the function $\varphi(u)=A u$ is a linear map from $\mathbb{R}^{n}$ into $\mathbb{R}^{m}$.

When $A \in \mathbb{R}^{n \times n}$, then $\varphi(u)=A u$ is a linear transformation.

Remark: linear maps map the zero vector to the zero vector.

----

A linear transformation is uniquely determined by its action on a basis of $V$. If $\mathcal{B}=\left(b_{1}, b_{2}, \ldots, b_{n}\right)$ is a basis of $V$ and $\varphi\left(b_{i}\right)=w_{i}$, then from $v=\lambda_{1} b_{1}+\lambda_{2} b_{2}+\cdots+\lambda_{n} b_{n}$ follows, that

$$
\varphi(v)=\lambda_{1} w_{1}+\lambda_{2} w_{2}+\cdots+\lambda_{n} w_{n}
$$

----

### Definition

Let $V$ be an $n$-dimensional vector space, $\mathcal{B}=\left(b_{1}, b_{2}, \ldots, b_{n}\right)$ a basis of $V$, and consider a linear transformation $\varphi: V \rightarrow V$. Then the matrix of $\varphi$ with respect to $\mathcal{B}$ is the $n \times n$ matrix, such that in its $i^{\text {th }}$ column there are the coordinates of $\varphi\left(b_{i}\right)$ with respect to the basis $\mathcal{B}$.

$\Longrightarrow$ every $\varphi$ linear transformation can be written in form $\varphi(v)=A v$.

----

## Eigenvalues, Eigenvectors

### Definition

Let $\varphi: V \rightarrow V$ be a linear transformation. A non-zero vector $v \in V$ is called the eigenvector of $\varphi$ if $\exists \lambda \in \mathbb{R}: \varphi(v)=\lambda v$. Then $\lambda$ is the eigenvalue of $\varphi$ associated with $v$.

### Remark

A vector space can be defined over $\mathbb{C}$, too.

If $\varphi: V \rightarrow V$ is a linear transformation, where $V$ is a vector space over $\mathbb{C}$, then a non-zero vector $v \in V$ is called the eigenvector of $\varphi$ if $\exists \lambda \in \mathbb{C}$ : $\varphi(v)=\lambda v$. Then $\lambda$ is the eigenvalue of $\varphi$ associated with $v$.

**Remarks:**

- If $v$ is an eigenvector of $\varphi$, then the associated eigenvalue is uniquely determined.
- If $\lambda$ is an eigenvalue, then the corresponding eigenvectors form a vector subspace of $V$ :
  - $L_{\lambda}:=\{v \in V \mid \varphi(v)=\lambda v\}:$ the eigenspace of $\varphi$ associated with $\lambda$.

### Remark

Let $A$ be an $n \times n$ matrix. A non-zero vector $x$ is an eigenvector of $A$, if there exists a $\lambda$ scalar, for which

$$
A x=\lambda x
$$

Then $\lambda$ is called the eigenvalue of $A$ associated to $x$.

$$
A x=\lambda x \Longleftrightarrow\left(A-\lambda I_{n}\right) x=0
$$

i.e. for a given $\lambda$ we have to solve a homogeneous system of linear equations. It has a non-trivial solution if and only if

$$
\operatorname{det}\left(A-\lambda I_{n}\right)=0
$$

The characteristic polynomial of the $n \times n$ matrix $A$ (or the corresponding linear transformation $\varphi$ ) is the $n$-degree polynomial $\operatorname{det}\left(A-\lambda I_{n}\right)$. The roots of the characteristic polynomial are just the eigenvalues of $A$.

### Example

Determine the eigenvalues of

$$
A=\left(\begin{array}{rr}
-5 & -8 \\
4 & 7
\end{array}\right)
$$

The characteristic equation: $\operatorname{det}(A-\lambda I)=0$ :

$$
\left|\begin{array}{cc}
-5-\lambda & -8 \\
4 & 7-\lambda
\end{array}\right|=(-5-\lambda)(7-\lambda)+32=\lambda^{2}-2 \lambda-3=0
$$

The roots: $\lambda_{1}=-1, \lambda_{2}=3$. (Two different real eigenvalues)

### Remark

- The characteristic polynomial of a matrix $A \in \mathbb{R}^{n \times n}$ is a real polynomial of order $n \Longrightarrow$ a matrix $A \in \mathbb{R}^{n \times n}$ has in $\mathbb{C}$ exactly $n$ eigenvalues (counted with multiplicity).
- If a complex number $\lambda$ is an eigenvalue of $A \in \mathbb{R}^{n \times n}$, then the complex conjugate of $\lambda$ is an eigenvalue, too.
- The eigenvalues of a diagonal matrix are the numbers standing on the main diagonal of the matrix.
- The eigenvalues of a triangular matrix are the numbers standing on the main diagonal of the matrix.
- A matrix has an inverse if and only if 0 is not an eigenvalue of the matrix.

