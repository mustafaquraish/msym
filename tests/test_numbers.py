import pytest
from msym import *

class Test_Numbers:
    def test_create_rational(self):
        s = Rational(1, 6)
        assert isinstance(s, Rational) and s.numerator == 1 and s.denominator == 6
    
    def test_simplify_rational(self):
        s = Rational(2, 6)
        assert s == Rational(1, 3)

    def test_create_int(self):
        s = Int(1)
        assert isinstance(s, Int) and s.value == 1

    def test_create_int_from_rational(self):
        s = Rational(6, 2)
        assert s == Int(3)

    def test_add_int(self):
        s = Int(1) + Int(2)
        assert s == Int(3)

    def test_add_int_convert(self):
        s = Int(1) + 2
        assert s == Int(3)

    def test_add_rational_int(self):
        s = Rational(1, 2) + Int(2)
        assert s == Rational(5, 2)

    def test_add_rational_rational(self):
        s = Rational(1, 3) + Rational(1, 3)
        assert s == Rational(2, 3)

    def test_add_rational_int_convert(self):
        s = Rational(1, 2) + 1
        assert s == Rational(3, 2)

    def test_add_rational_rational_into_int(self):
        s = Rational(1, 3) + Rational(2, 3)
        assert s == Int(1)

    def test_int_ops(self):
        s = Int(1)
        assert s + Int(2) == Int(3)
        assert s - Int(2) == Int(-1)
        assert Int(2) - s == Int(1)
        assert s * Int(2) == Int(2)
        assert s / Int(2) == Rational(1, 2)
        assert s // Int(2) == Int(0)

        s = 1
        assert s + Int(2) == Int(3)
        assert s - Int(2) == Int(-1)
        assert Int(2) - s == Int(1)
        assert s * Int(2) == Int(2)
        assert s / Int(2) == Rational(1, 2)
        assert s // Int(2) == Int(0)

        s = Int(1)
        assert s + 2 == Int(3)
        assert s - 2 == Int(-1)
        assert 2 - s == Int(1)
        assert s * 2 == Int(2)
        assert s / 2 == Rational(1, 2)
        assert s // 2 == Int(0)

    def test_rational_ops(self):
        s = Rational(1, 2)
        assert s + Rational(1, 4) == Rational(3, 4)
        assert s - Rational(3, 4) == Rational(-1, 4)
        assert Rational(1, 2) - s == Int(0)
        assert s * Rational(1, 2) == Rational(1, 4)
        assert s / Rational(1, 2) == Int(1)
        assert s // Rational(1, 9) == Int(4)

        s = Rational(1, 2)
        assert s + 1 == Rational(3, 2)
        assert s - 1 == Rational(-1, 2)
        assert 1 - s == Rational(1, 2)
        assert s * 2 == Rational(1, 1)
        assert s / 2 == Rational(1, 4)
        assert s // 2 == Int(0)