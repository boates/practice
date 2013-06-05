#!/usr/bin/env python

import os, sys, commands


def solve(combos, opposed, elements):

    N = len(elements)
    Es = list(elements)

    combo = {}
    for i in range(len(combos)):
        combo[combos[i][:2]] = [combos[i][-1]]

    invoked = []
    for i in range(N):
        invoked.append( Es.pop(0) )

        if len(invoked) >= 2:
            pair = invoked[-2] + invoked[-1]
            if pair in combo.keys():
                invoked = invoked[:-2]+combo[pair]
            elif pair[::-1] in combo.keys():
                invoked = invoked[:-2]+combo[pair[::-1]]

            for j in range(len(opposed)):
                a, b = list( opposed[j] )
                if a in invoked and b in invoked:
                    invoked = []

    return invoked


try:
    f = open(sys.argv[1],'r')
except:
    sys.exit(1)

T = int(f.readline())

for i in range(T):

    line = f.readline().split()
    C = int(line[0])
    combos = line[1:C+1]
    D = int(line[C+1])
    opposed = line[C+2:C+2+D]
    N = int(line[-2])
    elements = line[-1]

    invoked = solve(combos, opposed, elements)

    print "Case #"+str(i+1)+": "+str(invoked).replace("'","").replace('"','')
