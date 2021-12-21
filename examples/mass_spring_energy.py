from msym import *

def dist_between(a, b):
    s = Int(0)
    for x, y in zip(a, b):
        s = s + (y - x)**2
    return s.sqrt()

# Input
q0 = [Symbol(f'q0({i})') for i in range(3)]
q1 = [Symbol(f'q1({i})') for i in range(3)]
k = Symbol('stiffness')
l0 = Symbol('l0')

l = dist_between(q0, q1)

V = (k * (l - l0)**2) / 2
print(f"// Energy: ")
print(f"V = {ccode(V)};")

dV = [V.diff(i) for i in q0+q1]
print()
print(f"// Gradient: ")
for i in range(6):
    print(f"f({i}) = {ccode(dV[i])};")

ddV = [[V.diff(i).diff(j) for j in q0+q1] for i in q0+q1]
print()
print(f"// Hessian: ")
for i in range(6):
    for j in range(6):
        print(f"H({i},{j}) = {ccode(ddV[i][j])};")