#!/usr/bin/env python

import os, sys, commands

def combinations(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = range(r)
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)

def binary(n):
    '''convert denary integer n to binary string bStr'''
    bStr = ''
    if n < 0:  raise ValueError, "must be a positive integer"
    if n == 0: return '0'
    while n > 0:
        bStr = str(n % 2) + bStr
        n = n >> 1
    return bStr


def patrick_math(binary1,binary2):

    len1 = len(binary1)
    len2 = len(binary2)

    if len1 > len2:
        tmp = ''
        for i in range(len1-len2): tmp += '0'
        binary2 = tmp + binary2
    if len2 > len1:
        tmp = ''
        for i in range(len2-len1): tmp += '0'
        binary1 = tmp + binary1
    
    b1 = list(binary1)
    b2 = list(binary2)

    psum = ''
    for i in range(len(b1)):
        if int(b1[i])+int(b2[i]) == 0:
            psum += '0'
        if int(b1[i])+int(b2[i]) == 1:
            psum += '1'
        if int(b1[i])+int(b2[i]) == 2:
            psum += '0'

    return psum #return binary   # int(psum,2)  # return binary back to int


def solve(candies):

    N = len(candies)

    # create all possible two pile combos
    same = []
    for i in range(int(N/2.)):
        print "current=",i, int(N/2.)
        sys.stdout.flush()
        x = combinations(range(N),i+1)
#        print 'got it'
        for k in x:
            k = list(k)
#            print k
            pile1, pile2 = [], []
            for j in range(N):
                if j in k:
                    pile1.append(int(candies[j]))
                elif j not in k:
                    pile2.append(int(candies[j]))
            psum1 = '0'
            for j in range(len(pile1)):
                binary_tmp = binary(pile1[j])
                g = patrick_math(psum1,binary_tmp)
                psum1 = g
            psum2 = '0'
            for j in range(len(pile2)):
                binary_tmp = binary(pile2[j])
                g = patrick_math(psum2,binary_tmp)
                psum2 = g
            if int(psum1,2) == int(psum2,2):
                same.append( max( [sum(pile1), sum(pile2)] ) )
                
    if same == []:
        return 'NO'

    else:
        return max(same)
        

def main():

    try:
        f = open(sys.argv[1],'r')
    except:
        sys.exit(1)

    T = int(f.readline())

    for i in range(T):

        N = int(f.readline())
        candies = f.readline().split()

        x = solve(candies)

        print "Case #"+str(i+1)+": "+str(x)
        sys.stdout.flush()


if __name__ == '__main__':
    main()

