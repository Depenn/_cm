# Geometry Calculations (2D Analytic Geometry)

## 📘 Objective
This program implements the concepts of **Analytic Geometry and Linear Algebra** using object-oriented Python. Through well-structured classes and functions, users can perform geometric calculations and transformations on 2D objects such as points, lines, circles, and triangles.

---

## 🧩 Program Structure

### 1. Classes and OOP Design
The program defines four main classes:

#### 🟢 **Class Point**
- **Attributes:** `x`, `y`
- **Methods:**
  - `distance_to(other)`: calculates the Euclidean distance to another point.
  - `translate(dx, dy)`: translates the point by `(dx, dy)`.
  - `scale(factor, center)`: scales the point relative to a given center.
  - `rotate(angle, center)`: rotates the point by a given `angle` (in degrees) around a center.

#### 🔵 **Class Line**
- **Representation:** `Ax + By + C = 0`
- **Methods:**
  - `from_points(p1, p2)`: classmethod that creates a line from two points.
  - `translate(dx, dy)`: translates the line by `(dx, dy)`.

#### 🔴 **Class Circle**
- **Attributes:** `center (Point)`, `radius`
- **Methods:**
  - `translate(dx, dy)`: moves the circle.
  - `scale(factor, center)`: scales the circle relative to a given center.
  - `rotate(angle, center)`: rotates the circle’s center while keeping the radius unchanged.

#### 🟡 **Class Triangle**
- **Attributes:** `p1`, `p2`, `p3` (instances of Point)
- **Methods:**
  - `side_lengths()`: calculates the lengths of all three sides.
  - `perimeter()`: computes the triangle’s perimeter.
  - `area()`: calculates area using **Heron’s formula** or the **Shoelace formula**.
  - `triangle_type()`: determines the triangle type (right, equilateral, isosceles, scalene).
  - Supports geometric transformations (`translate`, `scale`, `rotate`) on all points.

---

## 🔢 Global Computational Functions

### 1. `intersect_lines(line1, line2)`
Finds the intersection point of two lines. If parallel → no solution; if coincident → infinite solutions.

### 2. `intersect_circles(c1, c2)`
Finds intersection points between two circles based on their centers and radii. May return 0, 1, or 2 points.

### 3. `intersect_line_circle(line, circle)`
Solves the system of equations between a line and a circle using a **quadratic discriminant**.

### 4. `perpendicular_line_from_point(line, point)`
Constructs a line perpendicular to a given line that passes through a given point.

### 5. `find_foot_of_perpendicular(line, point)`
Finds the **foot of the perpendicular** from a point to a line.

### 6. `verify_pythagorean_theorem(p1, p2, p3)`
Verifies whether three points form a **right triangle** using the relationship:
\[ a^2 + b^2 ≈ c^2 \]
Uses a small tolerance `EPS = 1e-9` for floating-point precision.

---

## ⚙️ Numerical Precision
- All floating-point comparisons use a small **epsilon (`EPS = 1e-9`)**.
- This prevents errors caused by binary representation of floating-point values.

---

## 🔬 Mathematical Principles Behind the Program
1. **2D Analytic Geometry:** each object is represented using coordinate equations.
2. **Linear Algebra:** used in rotation and scaling transformations.
3. **Trigonometry:** used in point rotations and distance computations.
4. **Pythagorean Theorem:** used to verify right triangles.

---

## 💻 How to Verify the Pythagorean Theorem in Code
1. Define three points, e.g. `A(0,0)`, `B(3,0)`, `C(0,4)`.
2. Call the function:
   ```python
   verify_pythagorean_theorem(A, B, C)
   ```
3. The program will calculate the side lengths AB, BC, and AC.
4. It checks whether \( a^2 + b^2 ≈ c^2 \).
5. If true, the function returns **True**, indicating the triangle is **right-angled**.

---

## 🧠 Example Execution (Main Block)
```python
if __name__ == "__main__":
    # Example usage of Point class
    p1 = Point(0, 0)
    p2 = Point(3, 4)
    print("Distance from p1 to p2:", p1.distance_to(p2))

    # Line from two points
    L1 = Line.from_points(Point(0, 0), Point(1, 1))
    L2 = Line.from_points(Point(0, 1), Point(1, 0))
    print("Intersection of L1 and L2:", intersect_lines(L1, L2))

    # Circles intersection
    C1 = Circle(Point(0, 0), 5)
    C2 = Circle(Point(4, 0), 3)
    print("Intersection points of two circles:", intersect_circles(C1, C2))

    # Verify right triangle
    A, B, C = Point(0, 0), Point(3, 0), Point(0, 4)
    print("Is triangle ABC right-angled?", verify_pythagorean_theorem(A, B, C))
```

---

## 📖 Conclusion
This program integrates **mathematical principles** and **object-oriented programming (OOP)** to solve geometric problems systematically. All computations are grounded in **Analytic Geometry**, **Pythagorean Theorem**, and **Trigonometry**, making it an excellent example for learning 2D computational mathematics.
