# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 11:16:21 2022

@author: Mikey_I_G
"""

balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

monthlyInterest = annualInterestRate/12
paid = 0
for month in range (0,12):
    paid += monthlyPaymentRate * balance
    balance = balance - monthlyPaymentRate * balance
    balance += balance * monthlyInterest
    
    #print('Month ' + str(month+1) + ' Total paid: ' + str(paid))
    #print('Month ' + str(month+1) + ' Remaining balance: ' + str(balance))

balance = round(balance,2)
print('Remaining balance: ' + str(balance))
    
