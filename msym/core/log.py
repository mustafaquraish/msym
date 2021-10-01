from msym.core.decorators import symbolicate
from .expression import Expression

# Natural log only for now
class Logarithm(Expression):
    def __init__(self, value):
        self.value = value

    def simplify(self):
        value = self.value.simplify()
        return Logarithm(value)

    def __repr__(self):
        return "log({})".format(self.value)
    
    def diff(self, var):
        return (1 / self.value) * self.value.diff(var)

@symbolicate
def log(value):
    return value.log()   