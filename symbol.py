class Symbol(object):
    def __init__(self, symbolName):
        self.symbolName = symbolName;

    def __repr__(self):
        return ':' + self.symbolName

    def __cmp__(self, other):
        if self.symbolName == other.symbolName:
            return 0
        
        return 1
