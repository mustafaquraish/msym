from msym.core import *

# importing enum for enumerations
from enum import Enum, auto
 
_LOWEST = 0
_ADD = 1
_MULT = 2
_DIV = 3
_NEG = 4
_CALL = 5
_HIGHEST = 6


def _ccode(E, prec):
    def wrap(s, p):
        if p < prec:
            return '(' + s + ')'
        return s

    if isinstance(E, Symbol):
        return wrap(E.name, _HIGHEST)
    if isinstance(E, Int):
        return wrap(str(E), _HIGHEST)
    if isinstance(E, Rational):
        return wrap(f'{E.numerator}.0/{E.denominator}.0', _MULT)
    if isinstance(E, Addition):
        return wrap(f'{_ccode(E.left, _ADD)} + {_ccode(E.right, _ADD)}', _ADD)
    if isinstance(E, Subtraction):
        if E.left == 0:
            return wrap(f'-{_ccode(E.right, _NEG)}', _NEG)
        return wrap(f'{_ccode(E.left, _ADD)} - {_ccode(E.right, _ADD)}', _ADD)
    if isinstance(E, Multiplication):
        return wrap(f'{_ccode(E.left, _MULT)}*{_ccode(E.right, _MULT)}', _MULT)
    if isinstance(E, Division):
        return wrap(f'{_ccode(E.left, _MULT)}/{_ccode(E.right, _DIV)}', _MULT)
        
    if isinstance(E, Power):
        # Don't use pow() for something simple like x^2
        if E.right == Int(2) and isinstance(E.left, Symbol):
            return wrap(f'{_ccode(E.left, _MULT)}*{_ccode(E.left, _MULT)}', _MULT)

        # if E.right.is_negative():
        #     return wrap(f'1.0/{_ccode(E.left ** (-E.right), _MULT)}', _MULT)

        # We use `ccode()` here to avoid the outer parenthesis on expressions
        if E.right == Rational(1, 2):
            return wrap(f'sqrt({_ccode(E.left, _LOWEST)})', _CALL) 
        return wrap(f'pow({_ccode(E.left, _LOWEST)}, {_ccode(E.right, _LOWEST)})', _CALL)

# Essentially the same as `_ccode`, except strips out outer parenthesis
def ccode(E):
    return _ccode(E, _LOWEST)