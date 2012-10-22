import collections
from abc import ABCMeta, abstractmethod

def is_float(s):
    """Check whether `s` is float number string or not.  
    """
    if all(ord('0') <= ord(c) <= ord('9') or c == '.' for c in s):
        if s.count('.') == 1:
            return True
    return False

def is_int(s):
    """Check whether `s` is integer string or not.  
    """
    return all(ord('0') <= ord(c) <= ord('9') for c in s)


class DictMixin(collections.Mapping):
    __metaclass__ = ABCMeta

    @abstractmethod
    def __getitem__(self, key):
        pass

    @abstractmethod
    def keys(self, key, value):
        pass

    def __contains__(self, item):
        return self.has_key(item)

    def __iter__(self):
        return self.iterkeys()

    def __len__(self):
        return len(self.keys())

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def has_key(self, key):
        return  key in self.keys()

    def items(self):
        return list(self.iteritems())

    def iteritems(self):
        return ([k, self[k]] for k in self.keys())

    def iterkeys(self):
        return iter(self.keys())

    def itervalues(self):
        return iter(self[k] for k in self.iterkeys())

    def values(self):
        return list(self.itervalues)

class MutableDictMixin(collections.MutableMapping):
    __metaclass__ = ABCMeta

    @abstractmethod
    def __getitem__(self, key):
        pass

    @abstractmethod
    def __setitem__(self, key, value):
        pass

    @abstractmethod
    def __delitem__(self, key):
        pass

    @abstractmethod
    def keys(self, key, value):
        pass

    def __contains__(self, item):
        return self.has_key(item)

    def __iter__(self):
        return self.iterkeys()

    def __len__(self):
        return len(self.keys())

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def has_key(self, key):
        return  key in self.keys()

    def items(self):
        return list(self.iteritems())

    def iteritems(self):
        return ([k, self[k]] for k in self.keys())

    def iterkeys(self):
        return iter(self.keys())

    def itervalues(self):
        return iter(self[k] for k in self.iterkeys())

    def values(self):
        return list(self.itervalues)

    def clear(self):
        for key in self:
            del self[key]

    def pop(self, key):
        value = self[key]
        del self[key]
        return value

    def popitem(self):
        if len(self) == 0:
            raise KeyError('popitem(): dictionary is empty')
        k = self.keys()[-1]
        v = self.pop(k)
        return k, v

    def setdefault(self, key, value=None):
        if not key in self.iterkeys():
            self[key] = value
            return value

    def update(self, dct):
        for k in dct:
            self[k] = dct[k]
