RESOUP
======

Author
------

Hardtack

Description
-----------

Resoup is interpreter of Lisp dialect

Installation
------------

cd /path/for/resoup

python setup.py install


Run
---

   cd /path/for/resoup

   python resoup

   Welcome to resoup!
   >>>

Syntax
------

Syntax of resoup is based on lisp family language

*   The first element of list is Function and others are arguments of Function
    
    For example:

    ([Function] [Arg1] [Arg2] ...)
    
        >>> (+ 1 2)
        3
    
    In this example '+' is procedure, '1', '2' are arguments of '+'
    
*   To define variable `(define [variable name] [value])`
    
    For example:
    
        >>> (define a (+ 1 2))
        >>> a
        3
    
*   To make function `(lambda [arg list] [function body])`
    
    For example:
    
        >>> (define add (lambda (x y) (+ x y)))
        >>> (add 3 5)
        8
        
*   To quit resoup call 'exit' function

    For example:

        >>> (exit)
        
    
Options
-------
