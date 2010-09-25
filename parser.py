from symbol import *
from functions import *
def parse(tokenQueue):
    while len(tokenQueue):
        token = tokenQueue.pop(0)
        listStack = []
        if token is '(':
            listStack.push(list)

        elif token is ')':
            list = listStack.pop()
            if len(listStack) is 0:
                return list

            listStack[-1].append(list)

        elif token[0] is '"':
            string = token[1:-1]
            if len(listStack) is 0:
                return string

            listStack[-1].append(string)

        else:
            if len(listStack) is 0:
                return Symbol(token)

            listStack[-1].append(Symbol(token))


    """Exception"""
