import pytest
from msym import *

class Test_Differentiation:
    def test_differentiate_constant(self):
        x = Symbol('x')
        assert Int(1).diff(x) == 0
        assert Rational(1, 4).diff(x) == 0

    def test_differentiate_other_variable(self):
        x = Symbol('x')
        y = Symbol('y')
        assert x.diff(y) == 0
        assert y.diff(x) == 0

    def test_differentiate_symbol(self):
        x = Symbol('x')
        y = Symbol('y')
        assert x.diff(x) == 1
        assert y.diff(y) == 1

    def test_differentiate_addition(self):
        x = Symbol('x')
        y = Symbol('y')
        assert (x + y).diff(x) == 1
        assert (x + y).diff(y) == 1
        assert (x + x + x + y).diff(x) == 3
        assert (x + x + x + y).diff(y) == 1

    def test_differentiate_subtraction(self):
        x = Symbol('x')
        y = Symbol('y')
        assert (x - y).diff(x) == 1
        assert (x - y).diff(y) == -1
        assert (x - x - x - y).diff(y) == -1

    def test_differentiate_multiplication(self):
        x = Symbol('x')
        y = Symbol('y')
        assert (x * y).diff(x) == y
        assert (x * y).diff(y) == x
        assert (x * x).diff(x) == x + x
        assert (x * x * x).diff(x) == 3 * (x ** 2)
        assert (x ** 9).diff(x) == 9 * (x ** 8)

    def test_differentiate_power(self):
        x = Symbol('x')
        assert (x ** Rational(1, 2)).diff(x) == Rational(1, 2) * x ** Rational(-1, 2)

    def test_differentiate_log(self):
        x = Symbol('x')
        assert (x.log()).diff(x) == 1 / x
        assert log(x).diff(x) == 1 / x
        assert ((x ** 2).log()).diff(x) == 2 / x
        assert log(x ** 2).diff(x) == 2 / x

        y = log(x + 1)
        assert y.diff(x) == 1 / (x + 1)
    