# msym: A toy symbolic math library

This is a toy library for symbolic math, which I have been experimenting around with. It is not (and will likely never) be fit to use in any serious project, but it is a good starting point for me to learn how to do symbolic math.

So far, it can do some basic scalar operations, and derivatives. There is an incredibly simple "Matrix" class, which is just a wrapper around a nested list
of symbols. You shouldn't be using it for any sort of complex equations that
don't involve breaking the matrix down into a scalar function.

There is some rudimentary support for simplifying equations, but there's no real algorithm behind it and it's just a add-simplification-as-you-need sort of thing.

TL;DR: Don't expect anything serious out of this other than learning how stuff like `sympy` works.
