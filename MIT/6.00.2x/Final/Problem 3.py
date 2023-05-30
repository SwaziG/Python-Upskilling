# -*- coding: utf-8 -*-
"""
Created on Sun May 21 10:46:47 2023

@author: Mikey_I_G
"""
import random 

# helper function
def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std  
  
def guessfood_sim(num_trials, probs, cost, get):
    """
    num_trials: integer, number of trials to run
    probs: list of probabilities of guessing correctly for 
           the ith food, in each trial
    cost: float, how much to pay for each food guess
    get: float, how much you get for a correct guess
    
    Runs a Monte Carlo simulation, 'num_trials' times. In each trial 
    you guess what each food is, the ith food has 'prob[i]' probability 
    to get it right. For every food you guess, you pay 'cost' dollars.
    If you guess correctly, you get 'get' dollars. 
    
    Returns: a tuple of the mean and standard deviation over 
    'num_trials' trials of the net money earned 
    when making len(probs) guesses
    """
    i=0
    tot_list = []
    while i < num_trials:
        i+=1
        tot = 0.0
        for prob in probs:
            tot -= cost
            if random.random() <= prob:
                tot += get
        tot_list.append(tot)
    x, y = getMeanAndStd(tot_list)
   
    return (x, y)

## print(guessfood_sim(100, [0.2, 0.4, 0.8, 0.9, 0.5, 0.7], 1, 5))
print(guessfood_sim(100, [1, 1, 1], 1, 0))
## print(guessfood_sim(3000, [0.1, 0.1, 0.7], 0.5, 0.8))
## print(guessfood_sim(3000, [0.5, 0.4, 0.9], 2.2, 10.3))
## print(guessfood_sim(3000, [0.11, 0.2, 0.5], 2, 2.5))
print(guessfood_sim(3000, [0.5, 0.5, 0.5], 1, 1))