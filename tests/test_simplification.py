import pytest
from msym import *

class Test_Simplification:

    def test_simplify_addition(self):
        s = Symbol('s')
        assert s + 0 == s
        assert 0 + s == s
        assert s + (-s) == 0
        assert s + (0-s) == 0
        assert s + (1-s) == 1
        assert s + Rational(0, 1) == s
        assert (s - 1) + 1 == s
        assert 1 + (s - 1) == s
        assert s + 2 == 2 + s   # Note, this only works for constants...
        assert s + s == 2 * s
        assert s + s + s + s == 4 * s
        assert (5 * s) + s == 6 * s
        assert s + (5 * s) == 6 * s

    def test_simplify_subtraction(self):
        s = Symbol('s')
        assert s - 0 == s
        assert 0 - s == -s
        assert s - (-s) == 2 * s
        assert s - (0-s) == 2 * s
        assert s - (1-s) == 2*s - 1
        assert s - Rational(0, 1) == s
        assert s - (s - 1) == 1
        assert s - 1 == s + (-1)
        assert s - s == 0
        assert s - s - s == -s
        assert (5 * s) - s == 4 * s
        assert s - (5 * s) == -4 * s

    def test_simplify_multiplication(self):
        s = Symbol('s')
        t = Symbol('t')

        assert s * 0 == 0 * s == 0
        assert s * 1 == 1 * s == s
        assert s * -1 == -1 * s == -s
        assert s * s * s * s == s ** 4

        assert (s * 5) * t == 5 * (s * t)
        assert s * (5 * t) == 5 * (s * t)

        assert s * (s * t) == s**2 * t
        assert (s * t) * t == s * t**2

        assert s * (1 / t) == s / t
        assert (1 / t) * s == s / t

        assert s**7 * s == s**8
        assert s**7 * s * s == s**9
        assert s * s**7 == s**8
        assert s**5 * s**7 == s**12

    def test_simplify_division(self):
        pass