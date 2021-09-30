import pytest
from msym import *

class Test_Simple:
    def test_create_symbol(self):
        s = Symbol('test')
        assert isinstance(s, Symbol) and s.name == 'test'