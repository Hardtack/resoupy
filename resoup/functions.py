import itertools
from typedefs import Function, Null

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
        return (reduce(lambda x,y:x-y, itertools.chain([first], args))
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

class DisplayFunction(BuiltinFunction):
    def __init__(self, env):
        super(DisplayFunction, self).__init__('display', env)

    def __call__(self, item):
        import resoup.globals as g
        g.stdout.write(str(item))
        return Null()

class NewlineFunction(BuiltinFunction):
    def __init__(self, env):
        super(NewlineFunction, self).__init__('newline', env)

    def __call__(self):
        import resoup.globals as g
        g.stdout.write('\n')
        return Null()

class ExitFunction(BuiltinFunction):
    def __init__(self, env):
        super(ExitFunction, self).__init__('exit', env)

    def __call__(self, code=0):
        exit(code)
