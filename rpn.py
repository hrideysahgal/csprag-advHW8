#!/usr/bin/env python3


import operator
import math

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
    '%': operator.mod,
    '//': operator.floordiv,
    '&': operator.and_,
    '|': operator.or_, 
    '~': operator.invert,
    '!': math.factorial,
}

def calculate(myarg):
    stack = list()
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
            if (token == 'c'): 
                stack.append(stack[-1])
            elif(token == '~' or token == '!'):
                function = operators[token]
                arg1 = stack.pop()
                result = function(arg1)
                stack.append(result)
            elif((token == '/' or token == '//') and stack[-1] == 0):
                stack.pop()
                stack.pop()
                print("You're dividing by zero, fool")
                continue
            else: 
                function = operators[token]
                arg2 = stack.pop()
                arg1 = stack.pop()
                result = function(arg1, arg2)
                stack.append(result)
        print(stack)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()

def main():
    while True:
        result = calculate(input("rpn calc> "))
        print("Result: ", result)

if __name__ == '__main__':
    main()
