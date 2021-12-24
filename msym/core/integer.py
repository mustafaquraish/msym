from .decorators import handle_only
from .expression import Expression

class Int(Expression):

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f'{self.value}'

    def __neg__(self):
        return Int(-self.value)

    @handle_only()
    def __add__(self, other):
        return Int(self.value + other.value)

    @handle_only()
    def __radd__(self, other):
        return Int(self.value + other.value)

    @handle_only()
    def __mul__(self, other):
        return Int(self.value * other.value)

    @handle_only()
    def __mod__(self, other):
        return Int(self.value % other.value)

    @handle_only()
    def __rmod__(self, other):
        return Int(other.value % self.value)

    @handle_only()
    def __rmul__(self, other):
        return Int(self.value * other.value)

    @handle_only()
    def __sub__(self, other):
        return Int(self.value - other.value)

    @handle_only()
    def __rsub__(self, other):
        return Int(other.value - self.value)

    @handle_only()
    def __truediv__(self, other):
        from .rational import Rational
        return Rational(self.value, other.value)

    @handle_only()
    def __rtruediv__(self, other):
        from .rational import Rational
        return Rational(other.value, self.value)

    @handle_only()
    def __floordiv__(self, other):
        from .intdiv import IntDiv
        return IntDiv(self.value, other.value)

    @handle_only()
    def __rfloordiv__(self, other):
        from .intdiv import IntDiv
        return IntDiv(other.value, self.value)

    # Just for completeness
    def floor(self):
        return self

    # Just for completeness
    def ceil(self):
        return self
    
    def __eq__(self, other):
        # For convenience, we want to allow comparison against a regular int
        if isinstance(other, int):
            return self.value == other
        if (isinstance(other, Int)):
            return self.value == other.value
        return False

    def __le__(self, other):
        if isinstance(other, int):
            return self.value <= other
        if (isinstance(other, Int)):
            return self.value <= other.value
        return False

    def __ge__(self, other):
        if isinstance(other, int):
            return self.value >= other
        if (isinstance(other, Int)):
            return self.value >= other.value
        return False

    def diff(self, var):
        return Int(0)
    
    def is_constant(self):
        return True
    
    def is_negative(self):
        return self.value < 0
    
    def eval(self, env):
        return self