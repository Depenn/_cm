# Homework 5 — Finite Field (有限體)

This project is part of the **Algebraic Structures & Python Programming** course assignment.  
It extends the previous homework on `rational_number.py` and `field_rational.py`, focusing on implementing **finite fields (有限體)** using modular arithmetic.

---

## 🧩 Objective

To implement and verify the algebraic structure of a **finite field** — a mathematical system in which addition, subtraction, multiplication, and division (except by zero) are all well-defined and satisfy the field axioms.

A finite field (also called a *Galois Field*) has a finite number of elements, typically denoted as **GF(p)** where `p` is a prime number.

---

## 🧠 Key Concepts

| Concept | Description |
|----------|--------------|
| **Closure** | The result of any operation (+, ×) stays within the field. |
| **Associativity** | `(a + b) + c = a + (b + c)` and `(a × b) × c = a × (b × c)` |
| **Commutativity** | `a + b = b + a` and `a × b = b × a` |
| **Identity Elements** | Additive identity: `0`; Multiplicative identity: `1` |
| **Inverses** | Additive inverse: `a + (-a) = 0`; Multiplicative inverse: `a × a⁻¹ = 1` (for a ≠ 0) |
| **Distributivity** | `a × (b + c) = (a × b) + (a × c)` |

---

## 🧮 Implementation Overview

The implementation is divided into several files:

| File | Description |
|------|--------------|
| `finite_field.py` | Defines the `FiniteField` and `FiniteFieldElement` classes implementing modular arithmetic. |
| `field_axioms.py` | Contains helper functions to verify field axioms (associativity, distributivity, etc). |
| `field_test.py` | Unit tests ensuring the field axioms hold for chosen prime modulus `p`. |
| `rational_number.py` | Previous homework reference implementing rational numbers as a field. |

### Example Structure

```python
# finite_field.py
class FiniteFieldElement:
    def __init__(self, value, p):
        self.value = value % p
        self.p = p

    def __add__(self, other):
        return FiniteFieldElement((self.value + other.value) % self.p, self.p)

    def __mul__(self, other):
        return FiniteFieldElement((self.value * other.value) % self.p, self.p)

    def inverse(self):
        # Using Fermat's Little Theorem for modular inverse
        if self.value == 0:
            raise ZeroDivisionError("0 has no multiplicative inverse")
        return FiniteFieldElement(pow(self.value, self.p - 2, self.p), self.p)
```

---

## ✅ Tests & Verification
Each axiom is automatically verified through assertions or helper functions:

```python
assert (a + (b + c)) == ((a + b) + c)       # Associative
assert (a * (b * c)) == ((a * b) * c)       # Associative
assert (a + b) == (b + a)                   # Commutative
assert a * (b + c) == (a * b) + (a * c)     # Distributive
assert a + zero == a                        # Additive identity
assert a * one == a                         # Multiplicative identity
assert a + (-a) == zero                     # Additive inverse
assert a * a.inverse() == one               # Multiplicative inverse
```

If all assertions pass, it confirms the structure satisfies **all field axioms**.
