from .expression import Expression

class Subtraction(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __repr__(self):
        if (self.left == 0):
            return f'-{self.right}'
        return '({} - {})'.format(self.left, self.right)

    def __eq__(self, other):
        return (isinstance(other, Subtraction) and
                self.left == other.left and
                self.right == other.right)

    def diff(self, var):
        return self.left.diff(var) - self.right.diff(var)

    def simplify(self):
        from .integer import Int

        left = self.left.simplify()
        right = self.right.simplify()

        if (right == Int(0)):
            return left
        if (left == right):
            return Int(0)

        # Convert to addition if we're doing x - (-y)
        if right.is_negative():
            return left + (-right)
        
        from .addition import Addition

        # Coalesce multiplications
        from .multiplication import Multiplication
        if isinstance(left, Multiplication):
            mult = left
            if left.right == right:
                return Multiplication(mult.left - 1, mult.right)
        if isinstance(right, Multiplication):
            mult = right
            if mult.right == left:
                return Multiplication(1 - mult.left, mult.right)

        if isinstance(right, Subtraction):
            return left + (right.right - right.left)

        if isinstance(left, Addition):
            if left.right == right:
                return left.left
        if isinstance(right, Addition):
            if left == right.left:
                return -right.right
        
        return Subtraction(left, right)

    def eval(self, env):
        return self.left.eval(env) - self.right.eval(env)