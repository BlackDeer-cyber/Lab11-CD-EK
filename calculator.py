"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# https://github.com/BlackDeer-cyber/Lab11-CD-EK
# Partner 1: Christopher Deer
# Partner 2: Elijah Kelford

import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def sub(a,b):
    return a-b

def multiply(a, b):
    return a * b

def mul(a, b):
    return a * b

def div(a,b):
    if a == 0:
        raise ZeroDivisionError #raise(
    return b / a   # raise ZeroDivisionError if a == 0


def divide(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a   # raise ZeroDivisionError if a == 0

def log(a,b):
    if b <= 0 or a <= 0:
        raise ValueError
    return math.log(b, a) #log b base a

def logarithm(a, b):
    if b <= 0 or a <= 0:
        raise ValueError
    return math.log(b, a) #log b base a

def exponent(a, b):
    return a**b

def exp(a,b):
    return a**b

def square_root(a):
    # if a < 0:
    #     raise
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

#gnfhiofdonkfj