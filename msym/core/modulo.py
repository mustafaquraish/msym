from .expression import Expression

class Modulo(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __repr__(self):
        return '({} % {})'.format(self.left, self.right)

    # TODO: Handle commutativity where applicable
    def __eq__(self, other):
        return (isinstance(other, Modulo) and
                self.left == other.left and
                self.right == other.right)

    def diff(self, var):
        raise NotImplementedError()
    
    def simplify(self):
        from .integer import Int
        if self.right == 1:
            return Int(0)
        return self

    def eval(self, env):
        return self.left.eval(env) % self.right.eval(env)