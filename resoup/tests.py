""":mod:`resoup.tests`
======================

Testcases for resoup
"""
import unittest
import StringIO
import resoup
import resoup.globals
from resoup.globals import builtin_env
from . import typedefs
from lexer import Lexer
from parser import Parser
from evaluator import eval as evaluate
from env import Environment

class ResoupTest(unittest.TestCase):
    def test_lex(self):
        expr = '(+ 1 2 ( 3 "this \\"is\\"\\nstring" `quote ? symbol) 1)'
        lexed = Lexer().lex(expr)
        self.assertEquals(['(', '+', '1', '2', '(', '3', '"',
            'this \\"is\\"\\nstring', '"', '`', 'quote', '?', 'symbol', ')',
            '1', ')'], lexed)

    def test_parse(self):
        lexed = [
            '(', 'begin', '(', '+', '1', '2', '(', '-', '4', '3.5', ')', ')',
            '(', 'display', "'", "Message is\\n\\'Here\\'", "'", ')', '(',
            'eval', '`', '1', ')', ')' ]
        li = typedefs.List()
        li.append(typedefs.Symbol('begin'))

        add = typedefs.List()
        add.append(typedefs.Symbol('+'))
        add.append(typedefs.Int(1))
        add.append(typedefs.Int(2))

        sub = typedefs.List()
        sub.append(typedefs.Symbol('-'))
        sub.append(typedefs.Int(4))
        sub.append(typedefs.Real(3.5))

        add.append(sub)

        li.append(add)

        display = typedefs.List()
        display.append(typedefs.Symbol('display'))
        display.append(typedefs.String("Message is\n'Here'"))

        li.append(display)

        ev = typedefs.List()
        ev.append(typedefs.Symbol('eval'))
        ev.append(typedefs.Quote(typedefs.Int(1)))

        li.append(ev)

        parsed = Parser().parse(lexed)
        self.assertEquals(li, parsed)

    def test_eval(self):
        testcase = '''
        (define zero (lambda (f) (lambda (x) x)))
        (define one (lambda (f) (lambda (x) (f x))))
        (define plus (lambda (m n) (lambda (f) (lambda (x) ((n f) ((m f) x))))))
        (define mult (lambda (m n) (lambda (f) (lambda (x) ((n (m f)) x)))))
        (define xp (lambda (m n) (lambda (f) (lambda (x) (((n m) f) x)))))
        (define pr (lambda (x) (begin (display x) x)))
        (define prn (lambda (n) (begin ((n pr) ".") (newline))))
        (define two (plus one one))
        (define three (plus two one))
        (define six (mult two three))
        (define sixty-four (xp two six))
        (prn sixty-four)
        '''
        stdout = resoup.globals.stdout
        sio = StringIO.StringIO()
        resoup.globals.stdout = sio
        env = Environment(builtin_env)
        for line in testcase.split('\n'):
            if line.strip() == '':
                continue
            evaluate(Parser().parse(Lexer().lex(testcase)), env)
        output = sio.getvalue()
        resoup.globals.stdout = stdout
        self.assertEquals('.' * 64, ''.join([x.strip() for x in
            output.split('\n')]))
