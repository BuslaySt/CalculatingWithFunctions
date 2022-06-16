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

def zero(func=None, number=0):
    if func is None:
        return number
    return func(number)
def one(func=None, number=1):
    if func is None:
        return number
    return func(number)
def two(func=None, number=2):
    if func is None:
        return number
    return func(number)
def three(func=None, number=3):
    if func is None:
        return number
    return func(number)
def four(func=None, number=4):
    if func is None:
        return number
    return func(number)
def five(func=None, number=5):
    if func is None:
        return number
    return func(number)
def six(func=None, number=6):
    if func is None:
        return number
    return func(number)
def seven(func=None, number=7):
    if func is None:
        return number
    return func(number)
def eight(func=None, number=8):
    if func is None:
        return number
    return func(number)
def nine(func=None, number=9):
    if func is None:
        return number
    return func(number)

def plus(b):
    return lambda a: a + b
def minus(b):
    return lambda a: a - b
def times(b):
    return lambda a: a * b
def divided_by(b):
    return lambda a: a // b
