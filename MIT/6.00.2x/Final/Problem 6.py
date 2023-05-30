# -*- coding: utf-8 -*-
"""
Created on Sun May 21 14:00:23 2023

@author: Mikey_I_G
"""
import numpy as np
import random

def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int
 
    Returns result, a numpy.array of length len(choices) 
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total, 
    pick the one that gives sum(result*choices) closest 
    to total without going over.
    """
    summ = 0
    run = 0
    min_val = 100000
    min_result =[]
    while summ != total:
        run += 1
        result = []
        for i in range(len(choices)):
            result.append(random.choice([1,0]))
        summ = 0   
        for i in range(len(choices)):
            new = result[i]*choices[i]
            summ += new
        if summ != total:
            val = abs(total - summ)
            if val < min_val:
                min_val = val
                min_result = result
        if run == 1000:
            result = min_result
            break
            
    
    return np.array(result)


print(find_combination([1,2,2,3], 4))
