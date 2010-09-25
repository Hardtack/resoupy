from symbol import *
from resoupExceptions import *
from evaluator import *

class Macro(object):
    def __init__(self, body):
        self.body = body

    def __call__(self, env, args):
        return self.body(env, *args)

def setDefaults(env):
    def defineCall(env, symbol, value):
        if type(symbol) is not Symbol:
            raise badTypeArgument(type(symbol,Symbol,0))
        else:
            env.add(symbol,evaluate(value, env))
    define = Macro(defineCall)
    env.add(Symbol('define'), define)

