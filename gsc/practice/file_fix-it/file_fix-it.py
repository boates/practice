#!/usr/bin/env python

import sys

def Nmkdirs(old,new):

    all_old = ['/']
    for i in range(len(old)):
        d = old[i]
        all_old.append(d)
        x = d.split('/')[1:]
        tmp = ''
        for n in x:
            tmp += '/'
            tmp += n
            if tmp not in all_old:
                all_old.append(tmp)

    tmp2 = [n for n in new if n not in all_old]
    new = tmp2


    all_new = []
    for i in range(len(new)):
        x = new[i].split('/')[1:]
        tmp = ''
        for n in x:
            tmp += '/'
            tmp += n
            if tmp not in all_new:
                all_new.append(tmp)

    mkdirs = len( [d for d in all_new if d not in all_old] )

    return mkdirs
    

try:
   f = open(sys.argv[1],'r')
except: sys.exit(1)

T = int(f.readline())

for i in range(T):
    old, new = [], []
    N, M = f.readline().split()
    N, M = int(N), int(M)
    for j in range(N):
        old.append(f.readline().strip())
    for j in range(M):
        new.append(f.readline().strip())

    mkdirs = Nmkdirs(old, new)

    print "Case #"+str(i+1)+": "+str(mkdirs)

