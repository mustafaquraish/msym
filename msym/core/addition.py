from .expression import Expression

class Addition(Expression):
    def __init__(self, left, right):
        # keep constants on the left
        if right.is_constant():
            left, right = right, left

        self.left = left
        self.right = right

    def __repr__(self):
        return '({} + {})'.format(self.left, self.right)

    # TODO: Handle commutativity where applicable
    def __eq__(self, other):
        return (isinstance(other, Addition) and
                self.left == other.left and
                self.right == other.right)

    def diff(self, var):
        return self.left.diff(var) + self.right.diff(var)
    
    def simplify(self):
        from .integer import Int
        left = self.left.simplify()
        right = self.right.simplify()

        if (left == Int(0)):
            return right
        if (right == Int(0)):
            return left

        if left == right:
            return Int(2) * left

        if left == -right:
            return Int(0)

        # If any of the constants are negative, convert to a subtraction
        if left.is_negative():
            return right - (-left)
        if right.is_negative():
            return left - (-right)
        
        # Coalesce multiplications
        from .multiplication import Multiplication
        if isinstance(left, Multiplication):
            mult = left
            if left.right == right:
                return Multiplication(mult.left + Int(1), mult.right)
        if isinstance(right, Multiplication):
            mult = right
            if mult.right == left:
                return Multiplication(mult.left + Int(1), mult.right)

        # Pyll out constants to the left
        if isinstance(left, Addition):
            if left.left.is_constant():
                return Addition(left.left, left.right + right)
        if isinstance(right, Addition):
            if right.left.is_constant():
                return Addition(right.left, left + right.right)

        from .subtraction import Subtraction

        # Remove cancellations between addition and subtraction
        if isinstance(left, Subtraction):
            if left.right == right:
                return left.left

            # Separate the constant
            if left.right.is_constant():
                return (left.left + right) - left.right

        if isinstance(right, Subtraction):
            if right.right == left:
                return right.left
            # Separate the constant
            if right.right.is_constant():
                return (left + right.left) - right.right

        return Addition(left, right)

    def eval(self, env):
        return self.left.eval(env) + self.right.eval(env)