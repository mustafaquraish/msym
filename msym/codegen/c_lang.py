from .generator import *

class CCodeGenerator(CodeGenerator):
    def power(self, E):
        # Don't use pow() for something simple like x^2
        if E.right == Int(2) and isinstance(E.left, Symbol):
            A = self.gen(E.left, Prec.MULT)
            return f'{A} * {A}', Prec.MULT
        
        # Do sqaure roots explicitly
        if E.right == Rational(1, 2):
            A = self.gen(E.left, Prec.LOWEST)
            return f'sqrt({A})', Prec.CALL

        A = self.gen(E.left, Prec.LOWEST)
        B = self.gen(E.right, Prec.LOWEST)
        return f'pow({A}, {B})', Prec.CALL

def ccode(E):
    return CCodeGenerator().generate(E)