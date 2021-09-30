"""
Tests is combining Int + Rational + Symbol works as expected.
"""

import pytest
from msym import *
from msym.core.addition import Addition
from msym.core.subtraction import Subtraction
from msym.core.multiplication import Multiplication
from msym.core.division import Division
from msym.core.power import Power

class Test_Mixing:
    def test_symbol_symbol_ops(self):
        assert Symbol('x') + Symbol('y') == Addition(Symbol('x'), Symbol('y'))
        assert Symbol('x') - Symbol('y') == Subtraction(Symbol('x'), Symbol('y'))
        assert Symbol('x') * Symbol('y') == Multiplication(Symbol('x'), Symbol('y'))
        assert Symbol('x') / Symbol('y') == Division(Symbol('x'), Symbol('y'))
        assert Symbol('x') ** Symbol('y') == Power(Symbol('x'), Symbol('y'))

    def test_symbol_int_ops(self):
        assert Symbol('x') + 1 == Addition(Symbol('x'), Int(1))
        assert Symbol('x') - 1 == Subtraction(Symbol('x'), Int(1))
        assert Symbol('x') * 2 == Multiplication(Symbol('x'), Int(2))
        assert Symbol('x') / 2 == Division(Symbol('x'), Int(2))
        assert Symbol('x') ** 2 == Power(Symbol('x'), Int(2))

        assert 1 + Symbol('x') == Addition(Int(1), Symbol('x'))
        assert 1 - Symbol('x') == Subtraction(Int(1), Symbol('x'))
        assert 2 * Symbol('x') == Multiplication(Int(2), Symbol('x'))
        assert 1 / Symbol('x') == Division(Int(1), Symbol('x'))
        assert 1 ** Symbol('x') == Power(Int(1), Symbol('x'))

    def test_symbol_rational_ops(self):
        assert Symbol('x') + Rational(1, 2) == Addition(Symbol('x'), Rational(1, 2))
        assert Symbol('x') - Rational(1, 2) == Subtraction(Symbol('x'), Rational(1, 2))
        assert Symbol('x') * Rational(1, 2) == Multiplication(Symbol('x'), Rational(1, 2))
        assert Symbol('x') / Rational(1, 2) == Division(Symbol('x'), Rational(1, 2))
        assert Symbol('x') ** Rational(1, 2) == Power(Symbol('x'), Rational(1, 2))

        assert Rational(1, 2) + Symbol('x') == Addition(Rational(1, 2), Symbol('x'))
        assert Rational(1, 2) - Symbol('x') == Subtraction(Rational(1, 2), Symbol('x'))
        assert Rational(1, 2) * Symbol('x') == Multiplication(Rational(1, 2), Symbol('x'))
        assert Rational(1, 2) / Symbol('x') == Division(Rational(1, 2), Symbol('x'))
        assert Rational(1, 2) ** Symbol('x') == Power(Rational(1, 2), Symbol('x'))


    