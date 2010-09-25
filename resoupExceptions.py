class symbolNotFound(Exception):
    pass

class badTypeArgument(Exception):
    def __init__(self, has, expected, at):
        self.has = has
        self.expected = expected
        self.at = at
