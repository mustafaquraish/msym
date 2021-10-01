
from enum import Enum, auto
from functools import total_ordering

from msym.core import *

# Precedence of operators
@total_ordering
class Prec(Enum):
    LOWEST = auto()
    ADD = auto()
    SUB = auto()
    MULT = auto()
    DIV = auto()
    NEG = auto()
    POW = auto()
    CALL = auto()
    ATOM = auto()
    HIGHEST = auto()

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented

def for_type(arg_type):
    def decorator(func):
        if arg_type in CodeGenerator.type_handlers:
            raise Exception("Type handler for type '{}' already defined".format(arg_type))
        CodeGenerator.type_handlers[arg_type] = func
        return func
    return decorator

class CodeGenerator:
    type_handlers = {}

    def wrap(self, code, cur_prec, prec):
        if cur_prec < prec:
            return "(" + code + ")"
        else:
            return code

    def symbol(self, E):
        return E.name, Prec.ATOM

    def integer(self, E):
        return str(E), Prec.ATOM
    
    def rational(self, E):
        return f'{E.numerator}.0/{E.denominator}.0', Prec.MULT

    def addition(self, E):
        A = self.gen(E.left, Prec.ADD)
        B = self.gen(E.right, Prec.ADD)
        return f'{A} + {B}', Prec.ADD

    def subtraction(self, E):
        if E.left == 0:
            return f'-{self.gen(E.right, Prec.NEG)}', Prec.NEG
        B = self.gen(E.right, Prec.SUB)
        A = self.gen(E.left, Prec.ADD)
        return f'{A} - {B}', Prec.ADD

    def multiplication(self, E):
        A = self.gen(E.left, Prec.MULT)
        B = self.gen(E.right, Prec.MULT)
        return f'{A} * {B}', Prec.MULT

    def division(self, E):
        A = self.gen(E.left, Prec.MULT)
        B = self.gen(E.right, Prec.DIV)
        return f'{A} / {B}', Prec.MULT

    def power(self, E):
        A = self.gen(E.left, Prec.MULT)
        B = self.gen(E.right, Prec.POW)
        return f'{A}^{B}', Prec.MULT

    def log(self, E):
        A = self.gen(E.value, Prec.LOWEST)
        return f'log({A})', Prec.CALL

    def gen(self, E, prec=Prec.LOWEST):
        if isinstance(E, Symbol):
            return self.wrap(*self.symbol(E), prec)
        if isinstance(E, Int):
            return self.wrap(*self.integer(E), prec)
        if isinstance(E, Rational):
            return self.wrap(*self.rational(E), prec)
        if isinstance(E, Addition):
            return self.wrap(*self.addition(E), prec)
        if isinstance(E, Subtraction):
            return self.wrap(*self.subtraction(E), prec)
        if isinstance(E, Multiplication):
            return self.wrap(*self.multiplication(E), prec)
        if isinstance(E, Division):
            return self.wrap(*self.division(E), prec)
        if isinstance(E, Power):
            return self.wrap(*self.power(E), prec)
        if isinstance(E, Logarithm):
            return self.wrap(*self.log(E), prec)
        raise Exception("Unsupported expression type: {}".format(type(E)))
    
    generate = gen