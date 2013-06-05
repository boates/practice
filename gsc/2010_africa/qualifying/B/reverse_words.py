#!/usr/bin/env python

import os, sys, numpy, commands, glob, math

f = open(sys.argv[1],'r')
out = open('reverse_words.out','w')

Ncases = int(f.readline())

for i in range(Ncases):
    
    line = f.readline().split()[::-1]
    out_string = ''
    for word in line:
        out_string += word+" "
        
    out.write("Case #"+str(i+1)+": "+out_string+"\n")

out.close()
