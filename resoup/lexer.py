import itertools
import StringIO
import string

class Lexer(object):
    c = None

    def skip_whitespaces(self, io):
        while True:
            self.c = io.read(1)
            if self.c == '':
                break
            if not self.c in string.whitespace:
                io.seek(io.tell() - 1)
                self.c = io.read(1)
                break

    def read_str(self, io, quote):
        """ Reads string body.  
        """
        li = []
        while self.c != quote and self.c != '':
            li.append(self.c)
            if self.c == '\\':
                self.c = io.read(1)
                if self.c == '':
                    break
                li.append(self.c)
            self.c = io.read(1)
        return ''.join(li)

    def read_symbol(self, io):
        li = []
        while self.c != '':
            if self.c in itertools.chain(
                    ['(', ')', "'", '"', '`'], string.whitespace):
                io.seek(io.tell() - 1)
                break
            li.append(self.c)
            self.c = io.read(1)
        return ''.join(li)

    def lexio(self, io):
        li = []
        self.skip_whitespaces(io)
        while self.c != '':
            if self.c in ['(', ')', '`']:
                li.append(self.c)
            elif self.c in ["'", '"']:
                quote = self.c

                # Append quote
                li.append(self.c)
                self.c = io.read(1)
                s = self.read_str(io, quote)

                # Append string body
                li.append(s)

                # Append quote if possible
                if self.c == quote:
                    li.append(self.c)
            else:
                s = self.read_symbol(io)
                li.append(s)
            self.skip_whitespaces(io)
        return li

    def lex(self, s):
        return self.lexio(StringIO.StringIO(s))
