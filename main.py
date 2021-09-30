from msym import *

a = Symbol("a")
b = Symbol("b")

c = a + b + 3

print(a)
print(b)
print(c)

print("a=1, b=3 ->", c.subs({'a': 1, 'b': 3}))