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
    piles1, piles2 = [], []
    piles1_sum, piles2_sum = [], []

    for i in range(int(N/2.)):

        x = combinations(range(N),i+1)
        for k in x:
            k = list(k)
            tmp1, tmp2 = [], []
            for j in range(N):
                if j in k:
                    tmp1.append(int(candies[j]))
                elif j not in k:
                    tmp2.append(int(candies[j]))

            piles1.append(tmp1)
            piles2.append(tmp2)
#            print tmp1, tmp2

            piles1_sum.append( sum(tmp1) )
            piles2_sum.append( sum(tmp2) )

    ##########
    # now have all possible combinations of 2 piles and their sums
    ##########

    p_piles1_sum = []
    p_piles2_sum = []
    for i in range(len(piles1)):
        psum = '0'
        for j in range(len(piles1[i])):
            binary_tmp = binary(piles1[i][j])
            g = patrick_math(psum,binary_tmp)
            psum = g
        p_piles1_sum.append( int(psum,2) )  # convert binary to int
        psum = '0'
        for j in range(len(piles2[i])):
            binary_tmp = binary(piles2[i][j])
            g = patrick_math(psum,binary_tmp)
            psum = g
        p_piles2_sum.append( int(psum,2) )  # convert binary to int

#    print p_piles1_sum
#    print p_piles2_sum

    same = []
    for i in range(len(p_piles1_sum)):
        if p_piles1_sum[i] - p_piles2_sum[i] == 0:
            same.append(i)

#    print same

    if same == []:
        return 'NO'

    else:
        actual_sums = []
        for i in range(len(same)):
            actual_sums.append( max( [piles1_sum[i],piles2_sum[i]] ) )
#        print actual_sums

        x = max(actual_sums)

        return x
        

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


if __name__ == '__main__':
    main()

