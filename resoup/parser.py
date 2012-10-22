from . import typedefs as t
from utils import is_int, is_float
class Parser(object):
    buff = []

    def read_list(self, close):

        li = t.List()
        if len(self.buff) == 0:
            raise ParseError('Bracket not closed')
        while len(self.buff) > 0 and self.buff[0] != close:
            li.append(self.read_item())
        if len(self.buff) == 0:
            raise ParseError('Bracket not closed')
        self.buff.pop(0)
        return li

    def read_str(self, quote):
        if len(self.buff) < 2:
            raise ParseError('String not closed')
        body = self.buff.pop(0)
        self.buff.pop(0)
        return t.String(body.decode('string_escape'))

    def read_item(self):
        if len(self.buff) == 0:
            return t.Null()
        token = self.buff.pop(0)
        if token == '(':
            return self.read_list(')')
        elif token in ['"', "'"]:
            return self.read_str(token)
        elif token == '`':
            return t.Quote(self.read_item())
        elif is_int(token):
            return t.Int(token)
        elif is_float(token):
            return t.Real(token)
        else:
            return t.Symbol(token)

    def parse(self, tokens):
        self.buff = list(tokens)
        return self.read_item()

class ParseError(Exception):
    pass
