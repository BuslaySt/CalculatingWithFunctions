import time
# This time we want to write calculations using functions and get the results. Let's have a look at some examples:

# so much for this

# seven(times(five())) # must return 35
# four(plus(nine())) # must return 13
# eight(minus(three())) # must return 5
# six(divided_by(two())) # must return 3
# Requirements:

# There must be a function for each number from 0 ("zero") to 9 ("nine")
# There must be a function for each of the following mathematical operations: plus, minus, times, divided_by
# Each calculation consist of exactly one operation and two numbers
# The most outer function represents the left operand, the most inner function represents the right operand
# Division should be integer division. For example, this should return 2, not 2.666666...:

def operation(expr, number):
    if expr[0] == "+":
        return int(number)+int(expr[1])
    if expr[0] == "-":
        return int(number)-int(expr[1])
    if expr[0] == "*":
        return int(number)*int(expr[1])
    if expr[0] == "/":
        return int(int(number)/int(expr[1]))

def zero(expr=None, number="0"):
    if expr is None:
        return number
    return operation(expr, number)
def one(expr=None, number="1"):
    if expr is None:
        return number
    return operation(expr, number)
def two(expr=None, number="2"):
    if expr is None:
        return number
    return operation(expr, number)
def three(expr=None, number="3"):
    if expr is None:
        return number
    return operation(expr, number)
def four(expr=None, number="4"):
    if expr is None:
        return number
    return operation(expr, number)
def five(expr=None, number="5"):
    if expr is None:
        return number
    return operation(expr, number)
def six(expr=None, number="6"):
    if expr is None:
        return number
    return operation(expr, number)
def seven(expr=None, number="7"):
    if expr is None:
        return number
    return operation(expr, number)
def eight(expr=None, number="8"):
    if expr is None:
        return number
    return operation(expr, number)
def nine(expr=None, number="9"):
    if expr is None:
        return number
    return operation(expr, number)

def plus(expr):
    return "+"+str(expr)
def minus(expr):
    return "-"+str(expr)
def times(expr):
    return "*"+str(expr)
def divided_by(expr):
    return "/"+str(expr)
