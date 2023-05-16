# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 15:03:35 2022

@author: Mikey_I_G
"""
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    Available = ''
    for L in string.ascii_lowercase:
        if L not in lettersGuessed:
            Available += L
    
    return Available


#import string
#print(string.ascii_lowercase)
#abcdefghijklmnopqrstuvwxyz

lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's', 'w', 'x', 'n', 'o', 'a', 'z']
print(getAvailableLetters(lettersGuessed))
#abcdfghjlmnoqtuvwxyz