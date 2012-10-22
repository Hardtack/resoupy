from typedefs import Function

class BuiltinFunction(Function):
    def __init__(self, name, env):
        super(BuiltinFunction, self).__init__(None, None, env, name)

class AddFunction(BuiltinFunction):
    def __init__(self, env):
        super(AddFunction, self).__init__('+', env)

    __call__ = lambda self, *args:reduce(lambda x,y:x+y,(args))

class SubstractFunction(BuiltinFunction):
    def __init__(self, env):
        super(SubstractFunction, self).__init__('-', env)
    __call__ = (lambda self, *args:reduce(lambda x,y:x-y, args)
        if len(args) > 1 else -args[0])

class MultiplyFunction(BuiltinFunction):
    def __init__(self, env):
        super(MultiplyFunction, self).__init__('+', env)

    __call__ = lambda self, *args:reduce(lambda x,y:x*y, args)

class DivideFunction(BuiltinFunction):
    def __init__(self, env):
        super(DivideFunction, self).__init__('/', env)

    __call__ = (lambda self, *args:reduce(lambda x,y:x/y,args)
        if len(args) > 1 else 1 / args[0])
