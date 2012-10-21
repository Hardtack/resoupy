from typedefs import BuiltinFunction

add = BuiltinFunction()
add.__call__ = lambda *args:sum(args)

sub = BuiltinFunction()
sub.__call__ = (lambda *args:reduce(lambda x,y:x-y, args)
    if len(args) > 1 else -args[0])

mul = BuiltinFunction()
mul.__call__ = lambda *args:reduce(lambda x,y:x*y, args)

div = BuiltinFunction()
div.__call__ = (lambda *args:reduce(lambda x,y:x/y,args)
    if len(args) > 1 else 1 / args[0])
