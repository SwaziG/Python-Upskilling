# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 14:11:34 2022

@author: Mikey_I_G
"""

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    
    TrueOrFalse = True
    for L in secretWord:
        
        if L not in lettersGuessed:
            TrueOrFalse = False
            break
            
    return TrueOrFalse
    
secretWord = 'apple' 
lettersGuessed = ['e', 'a', 'l', 'p', 'r', 's']
print(isWordGuessed(secretWord, lettersGuessed))
#False