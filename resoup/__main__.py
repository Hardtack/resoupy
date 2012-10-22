import sys
import traceback
import resoup.evaluator as ev
import resoup.globals as g
import resoup.typedefs as t
from resoup.parser import Parser
from resoup.lexer import Lexer
from resoup.env import Environment


l = Lexer()
p = Parser()
env = Environment(g.builtin_env)

print 'Welcome to resoup!'
def stdprint(s):
    print >> g.stdout, s

while True:
    try:
        sys.stdout.write('>>> ')
        expr = sys.stdin.readline()
        item = p.parse(l.lex(expr))
        obj = ev.eval(item, env)
        if not isinstance(obj, t.Null):
            stdprint(obj)
    except KeyboardInterrupt:
        print
        exit(0)
    except Exception, e:
        stdprint(traceback.format_exc())
