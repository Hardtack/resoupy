import typedefs as t
import evaluator as ev

class DefineMacro(t.Macro):
    def excute(self, env, name, value):
        if isinstance(name, t.List): # Function definition
            fname = name[0]
            args = name[1:]
            func = t.Function(args, value, env, fname)
            env[fname] = func
            return t.Null()
        elif isinstance(name, t.Symbol): # Value definition
            env[name] = ev.eval(value, env)
            return t.Null()
        else:
            raise SyntaxError('define')

class IfStatement(t.Macro):
    def excute(self, env, state, true, false):
        if ev.eval(state, env):
            return ev.eval(true, env)
        else:
            return ev.eval(false, env)
