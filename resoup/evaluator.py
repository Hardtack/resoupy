from . import typedefs as t

def eval(obj, env):
    if isinstance(obj, t.Quote):
        return obj.item
    elif isinstance(obj, t.Symbol):
        return env.find(obj)
    elif isinstance(obj, t.List):
        if len(obj) == 0:
            return t.Null()
        first = eval(obj[0], env)
        if isinstance(first, t.Function):
            return first(*map(lambda x:eval(x, env), obj[1:]))
        elif isinstance(first, t.Macro):
            return first(env, *obj[1:])
        else:
            raise TypeError('%s is not callable' % obj[0])
    else:
        return obj
