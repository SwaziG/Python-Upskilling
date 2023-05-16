# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 12:17:01 2022

@author: Mikey_I_G
"""

s = str(input('input a string of letters: '))
alphabetical = ('')
alphabet = ('')
alph = ('')
for char in s:
   
    if char >= alph:
        alph = char
        alphabet += char
     
        if len(alphabet) > len(alphabetical):
            alphabetical = alphabet
     
    else:
        alph = char
        alphabet = char
        

print('Longest substring in alphabetical order is: ' + alphabetical)