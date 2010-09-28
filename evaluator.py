from symbol import *
from environment import *
from resoupExceptions import *
from nil import *
from quote import *

def evaluate(form, env):
    if type(form) is Symbol:
        value = env.find(form)
        if value == None:
            raise SymbolNotFound
        else:
            return value
            
    elif type(form) is list:
        if len(form) is 0:
            return Nil()
        first = evaluate(form[0],env)
        return first(env,form[1:])

    elif type(form) is Quote:
        return form.val

    else:
        return form

