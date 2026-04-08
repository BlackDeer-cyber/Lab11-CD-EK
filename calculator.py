"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def sub(a,b):
    returna-b

def multiply(a, b):
    return a * b

def mul(a, b):
    return a * b

def div(a,b):
    if a == 0:
        raise(Exception("ZeroDivisionError"))
    return b / a   # raise ZeroDivisionError if a == 0


# def divide(a, b):
#     if a == 0:
#         raise(Exception("ZeroDivisionError"))
#     return b / a   # raise ZeroDivisionError if a == 0

def log(a,b):
    if b <= 0 or a <= 0:
        raise(Exception("ValueError"))
    return math.log(b, a) #log b base a

def logarithm(a, b):
    if b <= 0 or a <= 0:
        raise(Exception("ValueError"))
    return math.log(b, a) #log b base a

def exponent(a, b):
    returna**b

def exp(a,b):
    return a**b
#gnfhiofdonkfj