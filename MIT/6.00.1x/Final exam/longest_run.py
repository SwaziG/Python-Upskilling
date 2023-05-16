# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 10:38:41 2022

@author: Mikey_I_G
"""

def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing. 
    In case of a tie for the longest run, choose the longest run 
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run. 
    """
    longest = []
    temp_inc = []
    temp_dec = []
    
    for i in range(len(L)):
        if i == 0:
            temp_inc.append(L[i])
            
        else:    
            if L[i] >= L[i-1]:
                temp_inc.append(L[i])
                
                if L[i] != L[i-1]:
                    temp_dec = [L[i]]
                    
                if len(temp_inc)>len(longest):
                    longest = temp_inc
            
        if i == 0:
            temp_dec.append(L[i])
        else:
            if L[i] <= L[i-1]:
                temp_dec.append(L[i])
                
                if L[i] != L[i-1]:
                    temp_inc = [L[i]]
                    
                if len(temp_dec)>len(longest):
                    longest = temp_dec
   
    longest_sum = 0
    for i in longest:
        longest_sum += i
        
    return longest_sum

