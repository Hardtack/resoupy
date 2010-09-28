from symbol import *
from resoupExceptions import *
from evaluator import *

class Macro(object):
    def __init__(self, body):
        self.body = body

    def __call__(self, env, args):
        return self.body(env, *args)

