
def symbolicate(func):
    def wrapper(*args, **kwargs):
        from .integer import Int
        args = [ (Int(a) if isinstance(a, (int, bool)) else a) for a in args ]
        return func(*args, **kwargs)
    return wrapper

def handle_only(*types):
    def decorator(method):
        @symbolicate
        def wrapper(self, other):
            if not any(isinstance(other, t) for t in types) and not isinstance(other, type(self)):
                return getattr(super(type(self), self), method.__name__)(other)
            return method(self, other)
        return wrapper
    return decorator