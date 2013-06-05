#!/usr/bin/env python

import os, sys, numpy, commands, glob, math

f = open(sys.argv[1],'r')
out = open('output.out','w')

Ncases = int(f.readline())

convert = {'a':'2','b':'22','c':'222','d':'3','e':'33','f':'333', \
           'g':'4','h':'44','i':'444','j':'5','k':'55','l':'555', \
           'm':'6','n':'66','o':'666','p':'7','q':'77','r':'777','s':'7777', \
           't':'8','u':'88','v':'888','w':'9','x':'99','y':'999','z':'9999', \
           ' ':'0'}

#on_same_key = {'a':['a','b','c'],'b':['a','b','c'],'c':['a','b','c'], \
#               'd':['d','e','f'],'e':['d','e','f'],'f':['d','e','f'], \
#               'g':,'h':'44','i':'444','j':'5','k':'55','l':'555', \
#               'm':'6','n':'66','o':'666','p':'7','q':'77','r':'777','s':'7777', \
#               't':'8','u':'88','v':'888','w':'9','x':'99','y':'999','z':'9999', \
#               ' ':'0'}


for i in range(Ncases):
    
    line = list(f.readline())[:-1]
    translated = convert[line[0]]
    for j in range(1,len(line)):
        if len(line) > 1 and convert[line[j]][0] == convert[line[j-1]][0]:
#        if line[j] == line[j-1]:
            translated += " "
        translated += convert[line[j]]
        
    out.write("Case #"+str(i+1)+": "+translated+"\n")

out.close()
