# msym: A basic symbolic math library

This is the a minimal library for symbolic math, which I wrote out partly out of interest, and partly out of necessity for taking some complex derivatives while doing Physics Based animation. The code generators for existing libraries did not work the way I wanted them to, and I needed to process the generated code to work with the libraries I was using, so I wrote this library to fix that issue.

Below is a demonstration of some of the basic features:

- Creating symbols, and performing basic arithmetic with them
```py
>>> x = Symbol('x')
>>> y = Symbol('y')
>>> z = x + 5 * y
>>> z.subs(x=5, y=3)
20
>>> 3 * z
(3 * (x + (5 * y)))
```

- Basic simplification of arithmetic expressions
```py
>>> 0 + x
x
>>> x + x
(2 * x)
>>> x - x
0
>>> x - x + x
x
>>> x * x * x * x
(x ^ 4)
>>> x**2 * x**3
(x ^ 5)
```

- Rational number arithmetic
```py
>>> x = Rational(1,2)
>>> y = Rational(1,3)
>>> 2 * y
2/3
>>> 3 * y
1
>>> x + y
5/6
>>> (x + y) * 6
5
```

- Basic differentiation with chain rule
```py
>>> x = Symbol('x')
>>> y = Symbol('y')
>>> x.diff(x)
1
>>> (x ** 2).diff(x)
(2 * x)
>>> (x ** 2).diff(y)
0
>>> log(x + 1).diff(x)
(1 / (1 + x))
>>> (x ** 25 / x).diff(x)
(24 * (x ^ 23))
```

- Support for instantiating multiple symbols for a matrix
```py
>>> x = Matrix(2,2,'X')
>>> x
[
  X_00,  X_01,  
  X_10,  X_11,  
]
>>> x.trace()
(X_00 + X_11)
>>> x.determinant()
((X_00 * X_11) - (X_01 * X_10))
>>> y = Matrix(1,2,'Y')
>>> y
[
  Y_00,  Y_01,  
]
>>> y * x
[
  ((Y_00 * X_00) + (Y_01 * X_10)),  ((Y_00 * X_01) + (Y_01 * X_11)),  
]
```

- Modular code generation (currently: Matlab, C)
```py
# Can customize variable name format for matrices!
# Allows generated code to plug into any library
>>> x = Matrix(2,2,'X','{}[({},{})]') # Tuple-indices
>>> ccode(x.trace())
'X[(0,0)] + X[(1,1)]'

>>> x = Matrix(2,2,'X','{}[{},{}]')   # Numpy-like indices
>>> ccode(x.trace())
'X[0,0] + X[1,1]'

>>> x = Matrix(2,2,'X','{}({},{})')   # Eigen-like indices
>>> ccode(x.trace())
'X(0,0) + X(1,1)'
```

---

The `examples/` directory contains some real-world examples of how to use this, specifically to compute the gradient and hessian of a complex functions, and generate output code that can directly be plugged in to work with the `Eigen` C++ library.