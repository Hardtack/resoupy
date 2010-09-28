from symbol import *
from resoupExceptions import *
from procedure import *
from macro import *

def isNumber(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def setDefaults(env):
    def defineCall(env, symbol, value):
        if type(symbol) is not Symbol:
            raise BadTypeArgument(type(symbo),Symbol,0)
        else:
            env.add(symbol,evaluate(value, env))
    define = Macro(defineCall)
    env.add(Symbol('define'), define)

    def lambdaCall(env, argnames, body):
        for symbol in argnames:
            if type(symbol) is not Symbol:
                raise BadTypeArgument(type(symbol),Symbol,argnames.index(symbol))

        return Procedure(argnames, body, env)

    lambdamacro = Macro(lambdaCall)
    env.add(Symbol('lambda'),lambdamacro)




    env.add(Symbol('+'),Plus())
    env.add(Symbol('-'),Minus())
    env.add(Symbol('*'),Mult())
    env.add(Symbol('/'),Div())
