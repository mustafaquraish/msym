from .generator import CodeGenerator

# Default generator already creates what looks like matlab :^)
def mlcode(E):
    return CodeGenerator().generate(E)