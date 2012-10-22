import sys
import functions as f
import typedefs as t
from env import Environment

stdout = sys.stdout
builtin_env = Environment()

builtin_env[t.Symbol('+')] = f.AddFunction(builtin_env)
builtin_env[t.Symbol('-')] = f.SubstractFunction(builtin_env)
builtin_env[t.Symbol('*')] = f.MultiplyFunction(builtin_env)
builtin_env[t.Symbol('/')] = f.DivideFunction(builtin_env)
