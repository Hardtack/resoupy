import sys
import functions as f
import typedefs as t
import macros as m
from env import Environment

stdout = sys.stdout
builtin_env = Environment()

# Functions
builtin_env[t.Symbol('+')] = f.AddFunction(builtin_env)
builtin_env[t.Symbol('-')] = f.SubstractFunction(builtin_env)
builtin_env[t.Symbol('*')] = f.MultiplyFunction(builtin_env)
builtin_env[t.Symbol('/')] = f.DivideFunction(builtin_env)
builtin_env[t.Symbol('>')] = f.GreaterFunction(builtin_env)
builtin_env[t.Symbol('>=')] = f.GreaterEqualFunction(builtin_env)
builtin_env[t.Symbol('<')] = f.LessFunction(builtin_env)
builtin_env[t.Symbol('<=')] = f.LessEqualFunction(builtin_env)

# Macros
builtin_env[t.Symbol('define')] = m.DefineMacro()
builtin_env[t.Symbol('if')] = m.IfStatement()

# Default values
builtin_env[t.Symbol('true')] = t.Bool(True)
builtin_env[t.Symbol('false')] = t.Bool(False)
