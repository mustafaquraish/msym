from .expression import Expression

class Symbol(Expression):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        return isinstance(other, Symbol) and self.name == other.name

    def eval(self, env):
        if self.name in env:
            return env[self.name]
        return self

    def diff(self, var):
        from .integer import Int
        return Int(int(self == var))

    def eval(self, env):
        if self.name in env:
            return env[self.name]
        return self