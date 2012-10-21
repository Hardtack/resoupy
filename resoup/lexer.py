import itertools
import StringIO
import string

class Lexer(object):
    c = None
    specials = ['(', ')', "'", '"', '`']

    def skip_whitespaces(self, io):
        while True:
            self.c = io.read(1)
            if self.c == '':
                break
            if not self.c in string.whitespace:
                io.seek(io.tell() - 1)
                self.c = io.read(1)
                break

    def read_symbol(self, io):
        li = []
        while self.c != '':
            if self.c in itertools.chain(self.specials, string.whitespace):
                io.seek(io.tell() - 1)
                break
            li.append(self.c)
            self.c = io.read(1)
        return ''.join(li)

    def lexio(self, io):
        li = []
        self.skip_whitespaces(io)
        while self.c != '':
            if self.c in self.specials:
                li.append(self.c)
            else:
                s = self.read_symbol(io)
                li.append(s)
            self.skip_whitespaces(io)
        return li

    def lex(self, s):
        return self.lexio(StringIO.StringIO(s))
