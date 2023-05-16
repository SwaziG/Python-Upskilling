# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 14:55:58 2022

@author: Mikey_I_G
"""

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    Guess = ''
    for L in secretWord:
        
        if L in lettersGuessed:
            Guess += L
        else:
            Guess += '_'
            
    return Guess
    
  
    
secretWord = 'apple' 
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getGuessedWord(secretWord, lettersGuessed))
#'_ pp_ e'