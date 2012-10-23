# -*- encoding: utf-8 -*-
""":mod:`resoup.types` --- Type definition for resoup.  
========================================================

Contains definition of resoup's types.  
"""
from abc import ABCMeta, abstractmethod
from types import NoneType
from env import Environment

class Type(object):
    """Base class for resoup's type.  
    """
    def __ne__(self, other):
        return not self == other

class List(Type, list):
    """List type.  
    """
    pass

class Symbol(Type):
    """Symbol type.  
    """
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, Symbol):
            return self.name == other.name
        return False
    
    def __hash__(self):
        return hash(self.name)

class String(Type, unicode):
    """Unicode string type.  
    """
    pass

class Number(Type):
    """Base number type.  
    """
    pass

class Int(Number, int):
    """Integer type.  
    """
    def __add__(self, other):
        return Int(super(Int, self).__add__(other))
    def __sub__(self, other):
        return Int(super(Int, self).__sub__(other))
    def __mul__(self, other):
        return Int(super(Int, self).__mul__(other))
    def __floordiv__(self, other):
        return Int(super(Int, self).__floordiv__(other))
    def __mod__(self, other):
        return Int(super(Int, self).__mod__(other))
    def __divmod__(self, other):
        return Int(super(Int, self).__divmod__(other))
    def __pow__(self, other, *args):
        return Int(super(Int, self).__pow__(other, *args))
    def __lshift__(self, other):
        return Int(super(Int, self).__lshift__(other))
    def __rshift__(self, other):
        return Int(super(Int, self).__rshift__(other))
    def __and__(self, other):
        return Int(super(Int, self).__and__(other))
    def __xor__(self, other):
        return Int(super(Int, self).__xor__(other))
    def __or__(self, other):
        return Int(super(Int, self).__or__(other))
    def __div__(self, other):
        return Int(super(Int, self).__div__(other))
    def __truediv__(self, other):
        return Int(super(Int, self).__truediv__(other))

class Real(Number, float):
    """Real number type.   
    """
    def __add__(self, other):
        return Real(super(Real, self).__add__(other))
    def __sub__(self, other):
        return Real(super(Real, self).__sub__(other))
    def __mul__(self, other):
        return Real(super(Real, self).__mul__(other))
    def __floordiv__(self, other):
        return Real(super(Real, self).__floordiv__(other))
    def __mod__(self, other):
        return Real(super(Real, self).__mod__(other))
    def __divmod__(self, other):
        return Real(super(Real, self).__divmod__(other))
    def __pow__(self, other, *args):
        return Real(super(Real, self).__pow__(other, *args))
    def __lshift__(self, other):
        return Real(super(Real, self).__lshift__(other))
    def __rshift__(self, other):
        return Real(super(Real, self).__rshift__(other))
    def __and__(self, other):
        return Real(super(Real, self).__and__(other))
    def __xor__(self, other):
        return Real(super(Real, self).__xor__(other))
    def __or__(self, other):
        return Real(super(Real, self).__or__(other))
    def __div__(self, other):
        return Real(super(Real, self).__div__(other))
    def __truediv__(self, other):
        return Real(super(Real, self).__truediv__(other))

class Bool(Number):
    """Boolean type.  
    """
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        if self.value:
            return '#T'
        else:
            return '#F'

    def __eq__(self, other):
        if isinstance(other, Bool):
            return self.value == other.value
        return False

    def __nonzero__(self):
        return self.value

    def __add__(self, other):
        return Bool(super(Bool, self).__add__(other))
    def __sub__(self, other):
        return Bool(super(Bool, self).__sub__(other))
    def __mul__(self, other):
        return Bool(super(Bool, self).__mul__(other))
    def __floordiv__(self, other):
        return Bool(super(Bool, self).__floordiv__(other))
    def __mod__(self, other):
        return Bool(super(Bool, self).__mod__(other))
    def __divmod__(self, other):
        return Bool(super(Bool, self).__divmod__(other))
    def __pow__(self, other, *args):
        return Bool(super(Bool, self).__pow__(other, *args))
    def __lshift__(self, other):
        return Bool(super(Bool, self).__lshift__(other))
    def __rshift__(self, other):
        return Bool(super(Bool, self).__rshift__(other))
    def __and__(self, other):
        return Bool(super(Bool, self).__and__(other))
    def __xor__(self, other):
        return Bool(super(Bool, self).__xor__(other))
    def __or__(self, other):
        return Bool(super(Bool, self).__or__(other))
    def __div__(self, other):
        return Bool(super(Bool, self).__div__(other))
    def __truediv__(self, other):
        return Bool(super(Bool, self).__truediv__(other))

class Null(Type, NoneType):
    """Null type.  
    """
    def __repr__(self):
        return '<NULL>'

    def __str__(self):
        return 'NULL'

class Quote(Type):
    """Quote type.  
    """
    def __init__(self, item):
        self.item = item
        
    def __repr__(self):
        return '`%s' % repr(self.item)

    def __eq__(self, other):
        if isinstance(other, Quote):
            return self.item == other.item
        return False

class Function(Type):
    """Base function definition.  
    """
    def __init__(self, args, body, env, name='λ'):
        self.args = args
        self.body = body
        self.env = env
        self.name = name

    def __repr__(self):
        return '<Function(%s)>' % self.name

    def __call__(self, *args, **kwargs):
        import evaluator
        new_env = Environment(self.env)
        for s, v in zip(self.args, args):
            new_env[s] = v
        return evaluator.eval(self.body, new_env)

class Macro(Type):
    __metaclass__ = ABCMeta

    @abstractmethod
    def excute(self, env, *args, **kwargs):
        pass

    def __call__(self, *args, **kwargs):
        return self.excute(*args, **kwargs)

def convert(obj):
    if isinstance(obj, (int, long)):
        return Int(obj)
    elif isinstance(obj, float):
        return Real(obj)
    elif isinstance(obj, (str, unicode)):
        for quote in ['"', "'"]:
            if obj.startswith(quote):
                if (len(obj) - len(quote) * 2) > 0 and obj.endswith(quote):
                    return String(obj[1:-1])
                else:
                    raise ValueError
            elif obj.endswith(quote):
                raise ValueError
        if obj.startswith('`'):
            return Quote(convert(obj[1:]))
        return Symbol(obj)
    elif isinstance(obj, list):
        return List([convert(x) for x in obj])
