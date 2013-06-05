#!/usr/bin/env python

import os, sys, numpy, commands, glob, math

f = open(sys.argv[1],'r')
out = open('output.out','w')

Ncases = int(f.readline())

def is_smooth(pixels,M):
    for i in range(1,len(pixels)):
        if abs(pixels[i] - pixels[i-1]) > M:
            return False
        else: return True

for i in range(Ncases):
    
    line = f.readline()
    D, I, M, N = line.split()
    pixels = f.readline().split()

    



#    out.write("Case #"+str(k+1)+": "+answer+"\n")

out.close()
