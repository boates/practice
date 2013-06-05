#!/usr/bin/env python

import os, sys, numpy, commands, glob, math

f = open(sys.argv[1],'r')
out = open('output.out','w')

Ncases = int(f.readline())

for k in range(Ncases):
    
    line = f.readline().split()
    N, K = int(line[0]), int(line[1])
    board = []
    for i in range(N):
        board.append(list(f.readline().replace('\n','')))
#        print board[i]

#    print 

    for i in range(N):
        if board[i].count('.') != len(board[i]):
            dots = board[i].count('.')
            top = []
            for j in range(dots):
                top.append('.')
                board[i].remove('.')
            board[i] = top + board[i]
#        print board[i]

#    print 
    new = []
    for i in range(N):
        new.append([row[i] for row in board][::-1])
#        print new[i]

    # rows
    rows = []
    for i in range(N):
        s = ''
        for j in range(N):
            s += new[i][j]
        rows.append(s)

    columns = []
    for i in range(N):
        s = ''
        for j in range(N):
            s += new[j][i]
        columns.append(s)

    diagonals1 = []
    for i in range(N):
        s = ''
        m = i
        j = 0
        while m >= 0:
            s += new[m][j]
            m -= 1
            j += 1
        diagonals1.append(s)

    for i in range(1,N):
        m = N-1
        j = i
        s = ''
        while m >= 0 and j < N:
            s += new[m][j]
            m -= 1
            j += 1
        diagonals1.append(s)

    diagonals2 = []
    for i in range(N):
        s = ''
        m = i
        j = 0
        while m < N:
            s += new[m][j]
            m += 1
            j += 1
        diagonals2.append(s)

    for i in range(1,N):
        m = 0
        j = i
        s = ''
        while m < N and j < N:
            s += new[m][j]
            m += 1
            j += 1
        diagonals2.append(s)

    all = rows + columns + diagonals1 + diagonals2

    Rstr, Bstr = '', ''
    for i in range(K):
        Rstr += 'R'
        Bstr += 'B'

    Rwin, Bwin = False, False
    for i in range(len(all)):
        if Rstr in all[i]:
            Rwin = True
            answer = 'Red'
        if Bstr in all[i]:
            Bwin = True
            answer = 'Blue'
    if Rwin == True and Bwin == True:
        answer = 'Both'
    if Rwin == False and Bwin == False:
        answer = 'Neither'

    out.write("Case #"+str(k+1)+": "+answer+"\n")

out.close()
