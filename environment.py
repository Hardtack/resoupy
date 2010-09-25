from symbol import *
from functions import *

class Environment(object):
    def __init__(self, parent):
        self.parent = parent
        self.dic={}

    def __repr__(self):
        string = 'parent: '+self.parent.__repr__()+'\n'
        for key in self.dic.keys():
            string = string+key+'\t:'+self.dic[key].__repr__()+'\n'

        string = string+'\n'
        return string
    
    def find(self, symbol):
        name = symbol.symbolName
        if self.dic.has_key(name):
            return self.dic[name]

        elif self.parent is 0:
            return None

        else:
            return self.parent.find(symbol)

    def add(self, symbol, value):
        self.dic[symbol.symbolName]=value

    def has_symbol(self, symbol):
        return self.dic.has_key(symbol.symbolName)

