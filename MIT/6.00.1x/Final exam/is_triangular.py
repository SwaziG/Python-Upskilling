# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 10:24:04 2022

@author: Mikey_I_G
"""

def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not
    """
    tri = 1
    i= 2
    while tri <= k:
        if tri == k:
            return True
        else:
            tri += i
            i += 1
    return False

print(is_triangular(17))