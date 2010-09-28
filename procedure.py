from resoupExceptions import *
from environment import *
from evaluator import *
class Procedure(object):
    def __init__(self, argnames, body, env):
        self.argnames = argnames
        self.body = body
        self.env = env

    def __call__(self, args):
        set = zip(self.argnames, args)
        if len(set) is not len(args) and len(set) is not len(argnames):
            raise BadNumberOfArgs(len(args),len(argnames),len(argnames))
        newEnv = Environment(self.env)
        for argset in set:
            newEnv.add(argset[0],argset[1])
        return evaluate(self.body,newEnv)

class Plus(Procedure):
    def __init__(self):
        Procedure.__init__(self,None,None,None)

    def __call__(self, env, args):
        result = args[0]
        for i in args[1:]:
            result += i

        return result

class Minus(Procedure):
    def __init__(self):
        Procedure.__init__(self,None,None,None)
    def __call__(self, env, args):
        if len(args) is 1:
            return -args[0]

        result = args[0]

        for i in args[1:]:
            result -= i

        return result

class Mult(Procedure):
    def __init__(self):
        Procedure.__init__(self,None,None,None)
    def __call__(self, env, args):
        result = args[0]
        for i in args[1:]:
            result *= i

        return result

class Div(Procedure):
    def __init__(self):
        Procedure.__init__(self,None,None,None)
    def __call__(self, env, args):
        if len(args) is 1:
            return 1/args[0]

        result = args[0]
        for i in args[1:]:
            result/=i

        return result

