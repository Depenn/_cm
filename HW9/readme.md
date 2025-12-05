# HW9: Linear Algebra & Matrix Decomposition

This repository contains the Python implementation and conceptual answers for the Week 10 Linear Algebra assignment.

## 📂 Files
* `hw9.py`: Python script implementing Recursive Determinant, LU Decomposition, SVD, and PCA from scratch.
* `README.md`: Conceptual answers to the homework questions.

## 📝 Conceptual Answers

### 1. Linearity & Algebra
* **Linearity:** In Linear Algebra, a function $f(x)$ is linear if it satisfies two properties:
    1.  **Additivity:** $f(x + y) = f(x) + f(y)$
    2.  **Homogeneity:** $f(ax) = a f(x)$
    * *Intuitively:* The output changes proportionally to the input, without curvature or powers.
* **Algebra:** Derived from the Arabic *al-jabr* (meaning "reunion of broken parts"). It refers to the study of mathematical symbols and the rules for manipulating these symbols (vectors, matrices) to solve equations.

### 2. Space & Vector Space
* **Space:** In mathematics, a "space" is a set with some added structure (like distance, order, or operations).
* **Vector Space:** A collection of objects (vectors) that can be added together and multiplied by scalars while staying within the same set (closure property), adhering to specific axioms like associativity and distributivity.

### 3. Matrix vs. Vector
* **Matrix:** Represents a **linear transformation** (or a function). It maps one vector space to another.
* **Vector:** Represents the **data** or the input to that function.
* **Relationship:** In the equation $Ax = b$, the matrix $A$ acts upon the vector $x$ to transform it into vector $b$.

### 4. Geometric Operations (Translation, Scaling, Rotation)
* **Scaling:** Represented by a diagonal matrix.
* **Rotation:** Represented by orthogonal matrices involving $\sin$ and $\cos$.
* **Translation:** Unlike scaling/rotation, translation is **not linear** in standard coordinates (the origin moves). To represent it as a matrix multiplication, we must use **Homogeneous Coordinates** (adding an extra dimension, e.g., $(x, y) \to (x, y, 1)$).

### 5. Determinant
* **Meaning:** The determinant measures the **scaling factor of the volume** (or area in 2D) after the linear transformation.
* **Interpretation:**
    * If $\det(A) = 2$, the transformation doubles the volume.
    * If $\det(A) = 0$, the volume collapses to zero (the matrix is singular/non-invertible).

### 6. LU Decomposition for Determinants
* Decomposes matrix $A$ into Lower ($L$) and Upper ($U$) triangular matrices: $A = LU$.
* Since the determinant of a triangular matrix is just the product of its diagonal elements:
  $$\det(A) = \det(L) \times \det(U) = 1 \times \prod diag(U)$$
* This is computationally much faster $O(n^3)$ than the recursive Laplace expansion $O(n!)$.

### 7. Eigenvalues & Eigenvectors
* **Eigenvector ($v$):** A non-zero vector that changes only in scale (not direction) when a linear transformation is applied.
* **Eigenvalue ($\lambda$):** The factor by which the eigenvector is scaled.
* **Equation:** $Av = \lambda v$.
* **Significance:** They reveal the "axes of rotation" or the fundamental frequencies of a system (used in vibrations, stability analysis,
