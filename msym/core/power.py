from .expression import Expression

class Power(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __repr__(self):
        return '({} ^ {})'.format(self.left, self.right)

    # TODO: Handle commutativity where applicable
    def __eq__(self, other):
        return (isinstance(other, Power) and
                self.left == other.left and
                self.right == other.right)

    def simplify(self):
        from .integer import Int
        left = self.left.simplify()
        right = self.right.simplify()

        if right == Int(0):
            return Int(1)
        if left == Int(0):
            return Int(0)
        if right == Int(1):
            return left
        return Power(left, right)

    def diff(self, var):
        # General power rule
        from .integer import Int
        coeff = self.right * (self.left ** (self.right - Int(1)))
        return coeff * self.left.diff(var)
    
    def eval(self, env):
        return self.left.eval(env) ** self.right.eval(env)