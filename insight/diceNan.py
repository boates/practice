#!/usr/bin/env python
"""
diceNan.py
Author: Brian Boates

Solve Nan's unfair dice rolling problem
Complexity: O(6^N)

Also solve for the probability of obtaining 
a nondecreasing series of rolls
"""
from random import shuffle

def getallP(prob, d=6):
    """
    return: dictionary of all possible dice combinations
            and their probabilities
    params:
         prob: list[list[float]] | dice probability matrix
            d: int | dimensionality of dice
    """
    # number of dice
    N = len(prob)
    
    # check for bad N
    if N == 0: return allRolls
    
    # initialize dictionary to be returned
    allRolls = {}
    allRolls['1'] = prob[0][0]
    allRolls['2'] = prob[0][1]
    allRolls['3'] = prob[0][2]
    allRolls['4'] = prob[0][3]
    allRolls['5'] = prob[0][4]
    allRolls['6'] = prob[0][5]
    
    # loop over all possible remaining dice
    for i in range(1,N):
        
        # initialize new dictionary to hold updated prob's
        newAll = {}
        
        # loop over the current rolls/probs
        for k, v in allRolls.items():
            
            # loop over possible rolls for each die
            for j in range(d):
                
                # for every existing key/value in all
                # create a new key/value for all 6 possible 
                # "next rolls"
                newAll[k+str(j+1)] = v*prob[i][j]
                
            # update allRolls dictionary to new one for 
            # next pass through loop
            allRolls = newAll
    
    return allRolls


def nondecreasingP(prob, d=6):
    """
    return: float | total probability of obtaining a
                    nondecreasing set of rolls
    params:
         prob: list[list[float]] | dice probability matrix
            d: int | dimensionality of dice
    """
    # number of dice
    N = len(prob)
    
    # check for bad N
    if N == 0: return totalP
    
    # initialize dictionary to be returned
    allRolls = {}
    allRolls['1'] = prob[0][0]
    allRolls['2'] = prob[0][1]
    allRolls['3'] = prob[0][2]
    allRolls['4'] = prob[0][3]
    allRolls['5'] = prob[0][4]
    allRolls['6'] = prob[0][5]
    
    # loop over all possible remaining dice
    for i in range(1,N):
        
        # initialize new dictionary to hold updated prob's
        newAll = {}
        
        # loop over the current rolls/probs
        for k, v in allRolls.items():
            
            # loop over possible nondecreasing rolls
            for j in range(int(k[-1])-1, d):
                
                # for every existing key/value in all
                # create a new key/value for all possible 
                # nondecreasing "next rolls"
                newAll[k+str(j+1)] = v*prob[i][j]
                
            # update allRolls dictionary to new one for 
            # next pass through loop
            allRolls = newAll
            
    # sum the nondecreasing roll probabilities
    totalP = 0.0
    for k, v in allRolls.items():
        totalP += v
    
    return totalP


def main():
    
    # create dice probability matrix (3 dice)
    prob = [[0.1, 0.2, 0.3, 0.2, 0.15, 0.05],
            [0.05, 0.15, 0.2, 0.2, 0.3, 0.1]]#,
#            [0.2, 0.3, 0.15, 0.1, 0.2, 0.05]]
    
    # print the biased dice matrix
    print "dice probability matrix:\n["
    for die in prob: print die
    print "]\n"
    
    # get all probabilities for dice rolls
    allP = getallP(prob, d=6)
    
    # print the results
    print "roll, probabilities:"
    for k, v in allP.items():
        print k, v
        
    # compute and print the total nondecreasing probability
    nondecP = nondecreasingP(prob, d=6)
    print "\nprobability of nondecreasing"
    print "series of rolls = "+str(nondecP*100.0)+"%"

    
if __name__ == '__main__':
    main()