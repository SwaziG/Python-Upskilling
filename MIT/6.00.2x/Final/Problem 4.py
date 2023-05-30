# -*- coding: utf-8 -*-
"""
Created on Sun May 21 12:02:35 2023

@author: Mikey_I_G
"""

import random, pylab

# You are given this function
def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std

# You are given this class
class Die(object):
    def __init__(self, valList):
        """ valList is not empty """
        self.possibleVals = valList[:]
    def roll(self):
        return random.choice(self.possibleVals)

# Implement this -- Coding Part 1 of 2
def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a sequence of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axis
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """
    pylab.hist(values,numBins)
    if title != None:
        pylab.title(title)
    pylab.xlabel(xLabel) 
    pylab.ylabel(yLabel)
    pylab.show()
    
                    
# Implement this -- Coding Part 2 of 2
def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated
    """
    Die = die
    
    rolls = []
    for t in range(numTrials):
        
        tot = 1
        maxim = 0
        last_roll = 0
        for r in range(numRolls):
            val = Die.roll()
            # if the randomly chosen value is equal to the last rolled value, add 1 to the run total
            if val == last_roll:
                tot += 1
                # if this is the new max, store it as such
                if tot > maxim:
                    maxim = tot
            # otherwise, we need to save the current value as the last rolled, zero the total and start again
            else:
                last_roll = val
                tot = 1
        
        rolls.append(maxim)
    
    makeHistogram(rolls, 10, 'size of run', 'number of occurences')
    x, y = getMeanAndStd(rolls)
    return round(x, 3)
            
        
    
# One test case
random.seed(0)
#print (getAverage(Die([1,2,3,4,5,6,6,6,7]), 500, 10000))
# D = Die([1,2,3,4,5,6,6,6,7])
# print(D.roll())
