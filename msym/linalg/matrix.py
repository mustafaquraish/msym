from msym.core import *
from msym.core.decorators import handle_only

class Matrix(Symbol):
    def __init__(self, rows, cols, name="M", fstr='{}_{}{}'):
        self.rows = rows
        self.cols = cols
        self.name = name
        self.fstr = fstr
        self.data = [[Symbol(fstr.format(name, i, j)) for j in range(cols)] for i in range(rows)]

    def trace(self):
        s = Int(0)
        for i in range(min(self.rows, self.cols)):
            s += self.data[i][i]
        return s

    def __eq__(self, other):
        return type(self) == type(other) and self.rows == other.rows and self.cols == other.cols and self.name == other.name and self.data == other.data

    def determinant(self):
        if self.rows != self.cols:
            raise ValueError("Matrix must be square")
        if self.rows == 1:
            return self.data[0][0]
        if self.rows == 2:
            return self.data[0][0] * self.data[1][1] - self.data[0][1] * self.data[1][0]
        s = Int(0)
        for i in range(self.rows):
            s += (-1)**i * self.data[0][i] * self.submatrix(0, i).determinant()
        return s

    # For compatibility with sympy
    def det(self):
        return self.determinant()
    
    def __repr__(self):
        txt = "[\n"
        for i in range(self.rows):
            txt += "  "
            for j in range(self.cols):
                txt += str(self.data[i][j]) + ",  "
            txt += "\n"
        txt += "]"
        return txt

    def submatrix(self, row, col):
        m = Matrix(self.rows - 1, self.cols - 1, self.name)
        for i in range(self.rows):
            for j in range(self.cols):
                if i != row and j != col:
                    m.data[i - (i > row)][j - (j > col)] = self.data[i][j]
        return m

    def transpose(self):
        m = Matrix(self.cols, self.rows, self.name)
        for i in range(self.rows):
            for j in range(self.cols):
                m.data[j][i] = self.data[i][j]
        return m

    def __mul__(self, other):
        if not isinstance(other, Matrix):
            assert False, "Can only multiply matrix with another matrix currently"
        if self.cols != other.rows:
            raise ValueError("Incompatible dimensions")

        m = Matrix(self.rows, other.cols, self.name)
        for i in range(self.rows):
            for j in range(other.cols):
                s = Int(0)
                for k in range(self.cols):
                    s += self.data[i][k] * other.data[k][j]
                m.data[i][j] = s
        return m

    
    def __iter__(self):
        for i in range(self.rows):
            for j in range(self.cols):
                yield self.data[i][j]