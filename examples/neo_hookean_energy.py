from msym import *

F = Matrix(3, 3, 'F', '{}{}{}')
C = Symbol('C')
D = Symbol('D')

J = F.determinant()
Ic = (F.transpose() * F).trace()

w = C * (J ** Rational(-2, 3) * Ic - 3) + D * (J - 1) * (J - 1)
print(f"// Energy: ")
print(f"psi = {ccode(w)};")

dw = [w.diff(fi) for fi in F]
print()
print(f"// Gradient: ")
for i in range(9):
    print(f"dw({i}) = {ccode(dw[i])};")

ddw = [[w.diff(fi).diff(fj) for fi in F] for fj in F]
print()
print(f"// Hessian: ")
for i in range(9):
    for j in range(9):
        print(f"ddw({i},{j}) = {ccode(ddw[i][j])};")