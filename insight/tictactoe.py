#!/usr/bin/env python
from random import random

def printBoard(board):
    """
    """
    tl, tm, tr = board[0][0], board[0][1], board[0][2]
    ml, mm, mr = board[1][0], board[1][1], board[1][2]
    bl, bm, br = board[2][0], board[2][1], board[2][2]
    
    header = '_____________'
    bottom = '-------------'
    
    print header
    print '| '+tl+' | '+tm+' | '+tr+' |'
    print bottom
    print '| '+ml+' | '+mm+' | '+mr+' |'
    print bottom
    print '| '+bl+' | '+bm+' | '+br+' |'
    print bottom
    


def winningScenario(board):
    """
    board = [[tl, tm, tr],
             [ml, mm, mr],
             [bl, bm, br]]
    """
    result = None
    
    # top row
    if board[0][0] == board[0][1] == board[0][2]: result = board[0][0]
    
    # mid row
    elif board[1][0] == board[1][1] == board[1][2]: result = board[1][0]
    
    # bot row
    elif board[2][0] == board[2][1] == board[2][2]: result = board[2][0]
    
    # left col
    elif board[0][0] == board[1][0] == board[2][0]: result = board[0][0]
    
    # mid col
    elif board[0][1] == board[1][1] == board[2][1]: result = board[0][1]
    
    # right col
    elif board[0][2] == board[1][2] == board[2][2]: result = board[0][2]
    
    # diag 1
    elif board[0][0] == board[1][1] == board[2][2]: result = board[0][0]
    
    # diag 2
    elif board[2][0] == board[1][1] == board[0][2]: result = board[2][0]
    
    # None if not winning table
    if result == ' ':
        return None
    else:
        return result


def allFull(board):
    """
    """
    tmp = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            tmp.append(board[i][j])
    if ' ' in board:
        return False
    else:
        return True


def insertMove(board, move, player):
    """
    """
    if move == 'tl': board[0][0] = player
    elif move == 'tm': board[0][1] = player
    elif move == 'tr': board[0][2] = player
    elif move == 'ml': board[1][0] = player
    elif move == 'mm': board[1][1] = player
    elif move == 'mr': board[1][2] = player
    elif move == 'bl': board[2][0] = player
    elif move == 'bm': board[2][1] = player
    elif move == 'br': board[2][2] = player
    else:
        'move not valid, please try again:'
    
    return board 


def main():
    
    board = [[' ',' ',' '],
             [' ',' ',' '],
             [' ',' ',' ']]
    
    print "Current board:"
    printBoard(board)
    
    moves = ['tl','tm','tr','ml','mm','mr','bl','bm','br']
    
    while not winningScenario(board):
        
        if moves:
            
            redo = False
        
            move = raw_input('choose your slot (tl, tm, tr, ml, mm, mr, bl, bm, br):\n')
        
            if move not in moves:
                print "Move has already been played or is invalid! Choose again!"
                redo = True
                
            else:
                moves.pop(moves.index(move))
                board = insertMove(board, move, player='X')
                printBoard(board)
            
            print moves
            if moves and not redo:
                # random computer player's turn
                r = int(random()*len(moves))
                cmove = moves.pop(r)
                board = insertMove(board, cmove, player='O')
                printBoard(board)
                
            
    if winningScenario(board) == 'X':
        print 'Dude! You won!'
    elif winningScenario(board) == 'O':
        print 'You lost, bro'
    else:
        print 'Nobody wins :\\'

    
    
if __name__ == '__main__':
    main()