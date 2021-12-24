from .decorators import symbolicate

class Expression:

    @symbolicate
    def __add__(self, other):
        from .addition import Addition
        return Addition(self, other).simplify()

    @symbolicate
    def __radd__(self, other):
        from .addition import Addition
        return Addition(other, self).simplify()

    @symbolicate
    def __sub__(self, other):
        from .subtraction import Subtraction
        return Subtraction(self, other).simplify()

    @symbolicate
    def __rsub__(self, other):
        from .subtraction import Subtraction
        return Subtraction(other, self).simplify()

    @symbolicate
    def __mul__(self, other):
        from .multiplication import Multiplication
        return Multiplication(self, other).simplify()

    @symbolicate
    def __rmul__(self, other):
        from .multiplication import Multiplication
        return Multiplication(other, self).simplify()

    @symbolicate
    def __mod__(self, other):
        from .modulo import Modulo
        return Modulo(self, other).simplify()

    @symbolicate
    def __rmod__(self, other):
        from .modulo import Modulo
        return Modulo(other, self).simplify()

    @symbolicate
    def __truediv__(self, other):
        from .division import Division
        return Division(self, other).simplify()

    @symbolicate
    def __rtruediv__(self, other):
        from .division import Division
        return Division(other, self).simplify()

    @symbolicate
    def __floordiv__(self, other):
        from .intdiv import IntDiv
        return IntDiv(self, other).simplify()

    @symbolicate
    def __rfloordiv__(self, other):
        from .intdiv import IntDiv
        return IntDiv(other, self).simplify()

    @symbolicate
    def __pow__(self, other):
        from .power import Power
        return Power(self, other).simplify()

    @symbolicate
    def __rpow__(self, other):
        from .power import Power
        return Power(other, self).simplify()

    # TODO: Have a negation class
    def __neg__(self):
        from .subtraction import Subtraction
        from .integer import Int
        return Subtraction(Int(0), self).simplify()

    def diff(self, var):
        raise NotImplementedError("diff() is not implemented for this class")

    def simplify(self):
        return self

    def is_constant(self):
        return False

    def is_negative(self):
        return False

    def sqrt(self):
        from .rational import Rational
        return self ** Rational(1, 2)

    def log(self):
        from .log import Logarithm
        return Logarithm(self)

    # Should be called by the user
    def subs(self, env=None, **kwargs):
        from .symbol import Symbol
        from .integer import Int

        if env is None and not kwargs:
            raise ValueError("No substitutions provided")
        if env is None:
            env = {}
        for k, v in kwargs.items():
            if k not in env:
                env[k] = v

        # Convert all symbols to names
        env = {str(k): v for k, v in env.items()}
        for k, v in env.items():
            if isinstance(v, Expression) and v.is_constant():
                continue
            if isinstance(v, int):
                env[k] = Int(v)
                continue
            raise ValueError("Invalid substitution value: {}".format(v))

        return self.eval(env)
        
    # Internal use only.
    def eval(self, env):
        raise NotImplementedError("eval() is not implemented for this class")
