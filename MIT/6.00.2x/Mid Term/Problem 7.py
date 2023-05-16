# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 11:06:21 2023

@author: Mikey_I_G
"""

def solveit(test):
    """ test, a function that takes an int parameter and returns a Boolean
        Assumes there exists an int, x, such that test(x) is True
        Returns an int, x, with the smallest absolute value such that test(x) is True 
        In case of ties, return any one of them. 
    """
    x = 0
    while not test(x) and not test(-x):
        x += 1
    return x if test(x) else -x



# #### This test case prints 49 ####
def f(x):
    return (x+15)**0.5 + x**0.5 == 15
print(solveit(f))

# #### This test case prints 0 ####
def f(x):
    return x == -5
print(solveit(f))