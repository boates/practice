#!/usr/bin/env python

import os, sys, numpy, commands, glob, math

f = open(sys.argv[1],'r')
out = open('store_credit.out','w')

Ncases = int(f.readline())

for i in range(Ncases):
    
    credit = float(f.readline())
    Nitems = int(f.readline())
    items = f.readline().split()
    item_prices = [float(p) for p in items]

    for j in range(len(item_prices)):
        for k in range(len(item_prices)):
            if j < k:
                if item_prices[j] + item_prices[k] == credit:
                    out.write("Case #"+str(i+1)+": "+str(min(j,k)+1)+" "+str(max(j,k)+1)+"\n")
