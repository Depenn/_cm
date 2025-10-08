import math

class Rational:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        self.num = numerator
        self.den = denominator
        self._reduce()

    def _reduce(self):
        # menyederhanakan pecahan
        g = math.gcd(self.num, self.den)
        self.num //= g
        self.den //= g
        if self.den < 0:
            self.num *= -1
            self.den *= -1
    def __add__(self, other):
        return Rational(self.num * other.den + self.den * other.num,
                        self.den * other.den)

    def __mul__(self, other):
        return Rational(self.num * other.num,
                        self.den * other.den)
    def __neg__(self):
        return Rational(-self.num, self.den)

    def inverse(self):
        if self.num == 0:
            raise ZeroDivisionError("Zero has no multiplicative inverse")
        return Rational(self.den, self.num)

    def __eq__(self, other):
        return self.num == other.num and self.den == other.den
    def __repr__(self):
        return f"{self.num}/{self.den}"

a = Rational(1, 2)
b = Rational(1, 3)
c = Rational(1, 4)

# Asosiatif
assert (a + (b + c)) == ((a + b) + c)
# Identitas
assert (a + Rational(0, 1)) == a
# Invers
assert (a + (-a)) == Rational(0, 1)
# Komutatif
assert (a + b) == (b + a)


# Asosiatif
assert (a * (b * c)) == ((a * b) * c)
# Identitas
assert (a * Rational(1, 1)) == a
# Invers
assert (a * a.inverse()) == Rational(1, 1)
# Distributif
assert a * (b + c) == (a * b) + (a * c)

print("All tests passed!")
