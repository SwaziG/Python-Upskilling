# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 11:32:05 2022

@author: SwaziG
"""

def cipher(map_from, map_to, code):
    """ map_from, map_to: strings where each contain 
                          N unique lowercase letters. 
        code: string (assume it only contains letters also in map_from)
        Returns a tuple of (key_code, decoded).
        key_code is a dictionary with N keys mapping str to str where 
        each key is a letter in map_from at index i and the corresponding 
        value is the letter in map_to at index i. 
        decoded is a string that contains the decoded version 
        of code using the key_code mapping. """
    
    Cipher_Dict = {}
    for i in range(len(map_from)):
        Cipher_Dict[map_from[i]] = map_to[i]
        
        
    DeCiphered = ''
    for i in range(len(code)):
        DeCiphered += Cipher_Dict[code[i]]
    
    return (Cipher_Dict, DeCiphered)
    

print(cipher("abcd", "dcba", "dab"))