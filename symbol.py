class Symbol(object):
    def __init__(self, symbolName):
        self.symbolName = symbolName;

    def __repr__(self):
        return ':' + self.symbolName

    def __cmp__(self, other):
        return self.symbolName == other.symbolName

