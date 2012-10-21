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
    pass

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

class String(Type, unicode):
    """Unicode string type.  
    """
    pass

class Int(Type, int):
    """Integer type.  
    """
    pass

class Real(Type, float):
    """Real number type.   
    """
    pass

class Bool(Type):
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

    def apply(self, *args, **kwargs):
        """Apply function
        """
        import evaluator
        # Create new environment for function
        new_env = Environment(self.env)

        # Add given variables to new environment
        for s, v in zip(self.args, args):
            new_env[s] = v

        # Evaluate body with new environment
        return evaluator.eval(self.body, new_env)

    def __repr__(self):
        return '<Function(%s)>' % self.name

    def __unicode__(self):
        return str(self.body)

    def __str__(self):
        return unicode(self).encode('utf-8')

    def __call__(self, *args, **kwargs):
        return self.apply(args, kwargs)

class Macro(Type):
    __metaclass__ = ABCMeta

    @abstractmethod
    def excute(self, *args, **kwargs):
        pass

    def __call__(self, *args, **kwargs):
        return self.excute(*args, **kwargs)

def convert(obj):
    if isinstance(obj, (int, long)):
        return Int(obj)
    elif isinstance(obj, float):
        return Real(obj)
    elif isinstance(obj, (str, unicode)):
        for quote in ['"',"'"]:
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
