# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 10:07:34 2023

@author: Mikey_I_G
"""

def max_contig_sum(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L 
    """
    maxi = 0
    L_copy = L.copy()
    
    while len(L_copy) > 0:
        summ = 0
        
        for i in range(len(L_copy)): 
            
            summ += L_copy[i]
            if summ > maxi:
                maxi = summ

        del L_copy [0]
    return maxi

list1 = [3, 4, -8, 15, -1, 2]
print (max_contig_sum(list1))