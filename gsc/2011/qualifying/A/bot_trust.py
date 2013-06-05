#!/usr/bin/env python

import os, sys, commands


def solve(colors,buttons):

    # orange and blue both start at POSition 1
    Opos = 1
    Bpos = 1

    Obuts, Bbuts = [], []
    for i in range(len(buttons)):
        if colors[i] == 'O':
            Obuts.append(int(buttons[i]))
        if colors[i] == 'B':
            Bbuts.append(int(buttons[i]))
    Obuts.append(1000)
    Bbuts.append(1000)
    colors.append('dummy')

    Bnext = Bbuts.pop(0)
    Onext = Obuts.pop(0)
    color = colors.pop(0)

    time = 0
    pushed = 0

    while pushed < len(buttons):

        # case 1:
        if Opos != Onext and Bpos != Bnext:
            # Omoves
            Opos += (Onext-Opos) / abs(Onext-Opos)
            # Bmoves
            Bpos += (Bnext-Bpos) / abs(Bnext-Bpos)

        # case 2:
        elif Opos != Onext and Bpos == Bnext and color == 'O':
            # O moves
            Opos += (Onext-Opos) / abs(Onext-Opos)
            # B waits

        # case 3:
        elif Opos == Onext and Bpos != Bnext and color == 'B':
            # Bmoves
            Bpos += (Bnext-Bpos) / abs(Bnext-Bpos)
            # O waits

        # case 4:
        elif Opos == Onext and Bpos == Bnext and color == 'O':
            # O pushes
            pushed += 1
            Onext = Obuts.pop(0)
            color = colors.pop(0)
            # B waits

        # case 5:
        elif Opos == Onext and Bpos == Bnext and color == 'B':
            # B pushes
            pushed += 1
            Bnext = Bbuts.pop(0)
            color = colors.pop(0)
            # O waits

        # case 6:
        elif Opos == Onext and Bpos != Bnext and color == 'O':
            # O pushes
            pushed += 1
            Onext = Obuts.pop(0)
            color = colors.pop(0)
            # B moves
            Bpos += (Bnext-Bpos) / abs(Bnext-Bpos)

        # case 7:
        elif Opos != Onext and Bpos == Bnext and color == 'B':
            # B pushes
            pushed += 1
            Bnext = Bbuts.pop(0)
            color = colors.pop(0)
            # O moves
            Opos += (Onext-Opos) / abs(Onext-Opos)

        else:
            print '------\nBUG FOUND'
            print "Onext, Opos =",Onext, Opos
            print "Bnext, Bpos =",Bnext, Bpos
            print "next color =",color
            print '----------\n'

        time += 1

    return time


try:
    f = open(sys.argv[1],'r')
except:
    sys.exit(1)

T = int(f.readline())

for i in range(T):

    line = f.readline().split()
    N = line.pop(0)
    colors = line[::2]
    buttons = line[1::2]

    time = solve(colors,buttons)

    print "Case #"+str(i+1)+": "+str(time)

    
