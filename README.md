# Homework
## HW 1: Calculus & Numerical Approximation
Exploration of derivatives, integrals, and the Fundamental Theorem of Calculus using numerical approximation methods.

* **Derivative:** Approximated using difference quotients with $h = 0.00001$.
    * For $f(x) = x^3$ at $x=2$, calculated $\approx 12.000$, matching analytical $3x^2$.
* **Integral:** Riemann sum approximation.
    * $\int_{0}^{2} x^3 dx \approx 3.999$, matching analytical result $4$.
* **Fundamental Theorem:** Verified relationship between the accumulated area function and the original function.

## HW 2: Quadratic Equations
Solver for quadratic equations $ax^2 + bx + c = 0$ where $a \neq 0$.
Handles complex roots using the standard formula:

$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

```python
# Solving x^2 - 2x + 3 = 0
print(root(1, -2, 3))
# Output: (1+1.414j), (1-1.414j)
```
## HW  3: Cubic EquationsObjective
General solver for $ax^3 + bx^2 + cx + d = 0$1.Normalization: Transforms equation to monic form ( $a=1$ ).Depression: Substitutes $x = t - b/3$ to remove the $x^2$ term, resulting in $t^3 + pt + q = 0$.Cardano's Formula: Solves for $t$ using complex cube roots and maps back to $x$.

```python
roots = root3(1, -6, 11, -6)
# Output: [1.0, 2.0, 3.0] (Approximated)
```

## HW 4: Polynomial Roots via Linear Algebra
Objective: Solving high-degree polynomials using Eigenvalues.

Instead of iterative root-finding (Newton-Raphson), this implementation constructs a Companion Matrix. The eigenvalues of this matrix are mathematically equivalent to the roots of the polynomial .

```python
# Constructing the Companion Matrix
companion = np.zeros((n, n))
companion[1:, :-1] = np.eye(n-1)
companion[0, :] = -np.array(c[:-1])
roots = np.linalg.eigvals(companion)
```

## HW 5: Rational Numbers Class
Objective: Exact arithmetic implementation (avoiding floating point errors).
* Class: Rational(numerator, denominator)
* Simplification: Automatically reduces fractions using math.gcd upon initialization.
* Operator Overloading: Implements __add__, __mul__, __eq__, and inverse methods to allow standard Python operators (+, *) to work on Rational objects .

```python
a = Rational(1, 2)
b = Rational(1, 3)
# a + b -> Rational(5, 6)
```

## HW 6: Computational Geometry EngineObjective
Object-oriented 2D geometry library for collision detection and analysis.
* Primitives: Custom classes for Point, Line ( $Ax+By+C=0$ ), Circle, and Triangle.
* Triangle Analysis: Implements the Shoelace Formula for area calculation.
* Intersection Algorithms:
  * Line-Line: Determinant-based solver (Cramer's Rule logic).
  * Circle-Line: Calculates perpendicular distance from circle center to line.
  * Circle-Circle: Uses radical axis logic.

## HW 7: Statistical Hypothesis Testing
Objective: Manual implementation of parametric tests (No scipy.stats black-box).
* Z-Test: For known population $\sigma$.
* One-Sample T-Test: Estimates $\sigma$ using sample standard deviation ($S$) with DOF $n-1$.
* Independent T-Test: Calculates Pooled Variance ($S_p^2$) for two groups.
* Paired T-Test: Analyzes difference vectors ( $D = X_{after} - X_{before}$ ).

## HW 8: Information Theory & Coding
Objective: Entropy metrics and Error Correction Codes.
* Probability Underflow: Demonstrates the use of Log-Probability (n * log2(p)) to handle extremely small numbers.
* Entropy: Manual calculation of Shannon Entropy and KL-Divergence.
* Hamming Code (7,4):
  * Full implementation of Generator Matrix ($G$) and Parity Check Matrix ($H$).
  * Includes error simulation (bit flipping) and Syndrome Decoding to locate and correct errors.
 
## HW 9: Linear Algebra & Decompositions
Objective: Deep dive into matrix algorithms.
* Recursive Determinant: Implementation using Laplace Expansion ( $O(n!)$ ).
* LU Decomposition: Used to calculate determinants efficiently ( $O(n^3)$ ) via $det(P) \cdot det(U)$.
* SVD Manual Implementation: Computes Singular Value Decomposition by finding Eigenvalues of $A^TA$ and $AA^T$ .
* PCA (Principal Component Analysis):
  * Covariance Matrix computation.
  * Eigen decomposition.
  * Projection of data onto principal vectors.

## HW 10: Signal Processing (DFT)
Objective: Fourier Transform from first principles.
* DFT: Implements the summation formula $X[k] = \sum x[n] e^{-j2\pi kn/N}$ without FFT libraries.
* IDFT: Reconstruction algorithm to verify losslessness.
* Verification: Validated against Constant, Cosine, and Impulse signals.

## HW 11: ODE Solver
Objective: Symbolic solver for homogeneous linear ODEs.
* Input: Coefficients of the differential equation.
* Logic: Solves the characteristic equation and formats the general solution string.
* Features:
  * Handles Complex Conjugate roots ( $e^{\alpha x}\cos(\beta x)$ ) .
  * Handles Root Multiplicity (repeated roots) by injecting $x^k$ terms using a counter system.
