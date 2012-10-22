from utils import MutableDictMixin

class Environment(MutableDictMixin):
    def __init__(self, parent=None):
        self.parent = parent
        self.dic = {}

    def find(self, symbol):
        try:
            return self[symbol]
        except KeyError:
            if self.parent is None:
                raise
            else:
                return self.parent.find(symbol)

    def exists(self, symbol):
        if self.has_key(symbol):
            return True
        elif self.parent is None:
            return False
        else:
            return self.parent.exists(symbol)

    def __repr__(self):
        return '<Environment(%s)>' % self.dic
    
    def __getitem__(self, key):
        return self.dic[key]

    def __setitem__(self, key, value):
        self.dic[key] = value

    def __delitem__(self, key):
        del self.dic[key]

    def keys(self):
        return self.dic.keys()
