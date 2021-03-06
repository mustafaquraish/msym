from .expression import Expression

class Division(Expression):
    def __init__(self, left, right):
        from .integer import Int
        if (right == Int(0)):
            raise ZeroDivisionError()
        self.left = left
        self.right = right

    def __repr__(self):
        return '({} / {})'.format(self.left, self.right)

    def __eq__(self, other):
        return (isinstance(other, Division) and
                self.left == other.left and
                self.right == other.right)

    def diff(self, var):
        # Quotient rule
        num = self.left.diff(var) * self.right - self.left * self.right.diff(var)
        den = self.right * self.right
        return num / den

    def simplify(self):
        from .integer import Int
        left = self.left.simplify()
        right = self.right.simplify()

        if (right == Int(0)):
            raise ZeroDivisionError()
        if (right == Int(1)):
            return left
        if (left == Int(0)):
            return Int(0)

        from .power import Power
        if isinstance(left, Power):
            if left.left == right:
                return left.left ** (left.right - 1)
        if isinstance(right, Power):
            if right.left == left:
                return Division(Int(1), right.left ** (right.right - 1))

        from .multiplication import Multiplication
        if isinstance(left, Multiplication):
            if left.left == right:
                return left.right
        if isinstance(right, Multiplication):
            if right.left == left:
                return Division(Int(1), right.right)

        return Division(left, right)
    
    def eval(self, env):
        return self.left.eval(env) / self.right.eval(env)