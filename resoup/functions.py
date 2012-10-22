import itertools
from typedefs import Function

class BuiltinFunction(Function):
    def __init__(self, name, env):
        super(BuiltinFunction, self).__init__(None, None, env, name)

class AddFunction(BuiltinFunction):
    def __init__(self, env):
        super(AddFunction, self).__init__('+', env)

    def __call__(self, first, *args):
        return reduce(lambda x,y:x+y, itertools.chain([first], args))

class SubstractFunction(BuiltinFunction):
    def __init__(self, env):
        super(SubstractFunction, self).__init__('-', env)

    def __call__(self, first, *args):
        return (reduce(lambda x,y:x+y, itertools.chain([first], args))
            if len(args) > 0 else -first)


class MultiplyFunction(BuiltinFunction):
    def __init__(self, env):
        super(MultiplyFunction, self).__init__('+', env)

    def __call__(self, first, *args):
        return reduce(lambda x,y:x*y, itertools.chain([first], args))

class DivideFunction(BuiltinFunction):
    def __init__(self, env):
        super(DivideFunction, self).__init__('/', env)

    def __call__(self, first, *args):
        return (reduce(lambda x,y:x/y, itertools.chain([first], args))
            if len(args) > 0 else 1 / first)

class GreaterFunction(BuiltinFunction):
    def __init__(self, env):
        super(GreaterFunction, self).__init__('>', env)

    def __call__(self, first, second, *args):
        for v in itertools.chain([second], args):
            if not first > v:
                return False
        return True

class GreaterEqualFunction(BuiltinFunction):
    def __init__(self, env):
        super(GreaterEqualFunction, self).__init__('>=', env)

    def __call__(self, first, second, *args):
        for v in itertools.chain([second], args):
            if not first >= v:
                return False
        return True

class LessFunction(BuiltinFunction):
    def __init__(self, env):
        super(LessFunction, self).__init__('<', env)

    def __call__(self, first, second, *args):
        for v in itertools.chain([second], args):
            if not first < v:
                return False
        return True

class LessEqualFunction(BuiltinFunction):
    def __init__(self, env):
        super(LessEqualFunction, self).__init__('<=', env)

    def __call__(self, first, second, *args):
        for v in itertools.chain([second], args):
            if not first <= v:
                return False
        return True
        
