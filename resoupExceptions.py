class SymbolNotFound(Exception):
    pass

class BadTypeArgument(Exception):
    def __init__(self, has, expected, at):
        self.has = has
        self.expected = expected
        self.at = at

class BadNumberOfArgs(Exception):
    def __init__(self, has, min, max):
        self.has = has
        self.min = min
        self.max = max
