from .decorators import handle_only
from .expression import Expression
from math import gcd

class Rational(Expression):
    from .integer import Int
    def __new__(cls, numerator, denonimator):
        from .integer import Int
        if (denonimator == 0):
            raise ZeroDivisionError
        factor = gcd(numerator, denonimator)
        if (denonimator == factor):
            return Int(numerator // factor)
        return super().__new__(cls)
    
    def __init__(self, numerator, denominator):
        factor = gcd(numerator, denominator)
        self.numerator = numerator // factor
        self.denominator = denominator // factor

    def __repr__(self):
        return f'{self.numerator}/{self.denominator}'

    def __neg__(self):
        return Rational(-self.numerator, self.denominator)

    @handle_only(Int)
    def __add__(self, other):
        from .integer import Int

        if isinstance(other, Int):
            num = self.numerator + other.value * self.denominator
            return Rational(num, self.denominator)
        num = self.numerator * other.denominator + other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Rational(num, den)

    @handle_only(Int)
    def __radd__(self, other):
        return self + other

    @handle_only(Int)
    def __mul__(self, other):
        from .integer import Int
        if isinstance(other, Int):
            return Rational(self.numerator * other.value, self.denominator)
        return Rational(self.numerator * other.numerator, self.denominator * other.denominator)

    @handle_only(Int)
    def __rmul__(self, other):
        return self * other

    @handle_only(Int)
    def __sub__(self, other):
        return self + (-other)

    @handle_only(Int)
    def __rsub__(self, other):
        return (-self) + other

    @handle_only(Int)
    def __truediv__(self, other):
        from .integer import Int
        if isinstance(other, Int):
            return Rational(self.numerator, self.denominator * other.value)
        return Rational(self.numerator * other.denominator, self.denominator * other.numerator)

    @handle_only(Int)
    def __rtruediv__(self, other):
        from .integer import Int
        if isinstance(other, Int):
            return Rational(self.denominator * other.value, self.numerator)
        return Rational(self.denominator * other.numerator, self.numerator * other.denominator)

    @handle_only(Int)
    def __floordiv__(self, other):
        return (self / other).floor()

    @handle_only(Int)
    def __rfloordiv__(self, other):
        return (self / other).floor()

    def floor(self):
        from .integer import Int
        return Int(self.numerator // self.denominator)

    def ceil(self):
        from .integer import Int
        return Int(self.numerator // self.denominator + 1)

    def __eq__(self, other):
        return isinstance(other, Rational) and self.numerator == other.numerator and self.denominator == other.denominator

    def diff(self, var):
        from .integer import Int
        return Int(0)

    def is_constant(self):
        return True

    def is_negative(self):
        return self.numerator / self.denominator < 0

    def eval(self, env):
        return self