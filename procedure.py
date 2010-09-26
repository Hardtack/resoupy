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
