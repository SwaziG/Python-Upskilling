# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 08:47:00 2023

@author: Mikey_I_G
"""
def greedySum(L, s):
    """ input: s, positive integer, what the sum should add up to
               L, list of unique positive integers sorted in descending order
        Use the greedy approach where you find the largest multiplier for 
        the largest value in L then for the second largest, and so on to 
        solve the equation s = L[0]*m_0 + L[1]*m_1 + ... + L[n-1]*m_(n-1)
        return: the sum of the multipliers or "no solution" if greedy approach does 
                not yield a set of multipliers such that the equation sums to 's'
    """
   # NewL = L.copy()
        
    summ = 0
    summ_m = 0
    for i in range(len(L)):
       
        for j in range (s):
            if (summ + (L[i]*(s-j))) <= s:
                summ += L[i]*(s-j)
                summ_m += (s-j)
                break
    if summ != s: 
       return "no solution"
    return summ_m

# -----> testing
print(greedySum([6,3,2], 26))


