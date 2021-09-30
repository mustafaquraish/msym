from .expression import Expression

class Multiplication(Expression):
    def __init__(self, left, right):
        from .integer import Int
        from .rational import Rational

        # keep constants on the left
        if right.is_constant():
            left, right = right, left

        self.left = left
        self.right = right

    def __repr__(self):
        return f'({self.left} * {self.right})'

    # TODO: Handle commutativity where applicable
    def __eq__(self, other):
        return (isinstance(other, Multiplication) and
                self.left == other.left and
                self.right == other.right)

    def diff(self, var):
        # Product rule
        u = self.left
        v = self.right

        udv = u * v.diff(var)
        vdu = v * u.diff(var)

        return udv + vdu

    def simplify(self):
        from .integer import Int
        from .rational import Rational

        left = self.left.simplify()
        right = self.right.simplify()

        if (left == 1):
            return right
        if left == -1:
            return -right

        if (right == 1):
            return left
        if right == -1:
            return -left
        
        if (left == 0 or right == 0):
            return Int(0)

        # Simplify powers to make lives easier
        from .power import Power
        if left == right:
            return Power(left, Int(2))

        # Pull out constants to the left
        if isinstance(left, Multiplication):
            if left.left.is_constant():
                # (5 * x) * 5 -> (5 * 5) * x
                if right.is_constant():
                    return Multiplication(left.left * right, left.right)
                # (5 * b) * c -> 5 * (b * c)
                else:
                    return Multiplication(left.left, left.right * right)
        if isinstance(right, Multiplication):
            if right.left.is_constant():
                # 5 * (5 * x) -> (5 * 5) * x
                if left.is_constant():
                    return Multiplication(left * right.left, right.right)
                # b * (5 * c) -> 5 * (b * c)
                else:
                    return Multiplication(right.left, left * right.right)

        # Pull out common terms and replace with power.
        # Note: This only assumes associativity, not commutivity
        # TODO: Factor out assumptions
        #  (D * x) * x -> D * (x * x)
        if isinstance(left, Multiplication):
            if left.right == right:
                return Multiplication(left.left, left.right * right)
        #  D * (D * x) -> (D * D) * x
        if isinstance(right, Multiplication):
            if right.left == left:
                return Multiplication(left * right.left, right.right)

        from .division import Division

        # When multipliying with 1/x, invert the order
        #  (1 / x) * D -> D / x
        if isinstance(left, Division):
            if left.left == 1:
                return right / left.right
        #  D * (1 / x) -> D / x
        if isinstance(right, Division):
            if right.left == 1:
                return left / right.right

        # If we have a power with an equal base, bump the exponent
        #  (x^2) * (x^2) -> x^4
        if isinstance(left, Power) and isinstance(right, Power):
            if left.left == right.left:
                return Power(left.left, left.right + right.right)
        #  (s^5) * s -> s^6
        if isinstance(left, Power):
            if left.left == right:
                return Power(left.left, left.right + Int(1))
        #  s * (s^5) -> s^6
        if isinstance(right, Power):
            if right.left == left:
                return Power(right.left, right.right + Int(1))
        
        return Multiplication(left, right)

    def eval(self, env):
        return self.left.eval(env) * self.right.eval(env)