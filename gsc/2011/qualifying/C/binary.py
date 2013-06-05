#!/usr/bin/env python
 
def Denary2Binary(n):
    '''convert denary integer n to binary string bStr'''
    bStr = ''
    if n < 0:  raise ValueError, "must be a positive integer"
    if n == 0: return '0'
    while n > 0:
        bStr = str(n % 2) + bStr
        n = n >> 1
    return bStr
 
def int2bin(n, count=24):
    """returns the binary of integer n, using count number of digits"""
    return "".join([str((n >> y) & 1) for y in range(count-1, -1, -1)])

print Denary2Binary(5)

 
if __name__ == '__main__':
    print Denary2Binary(255)  # 11111111
 
    # convert back to test it
    print int(Denary2Binary(255), 2)  # 255
 
    print
 
    # this version formats the binary
    print int2bin(255, 12)  # 000011111111
    # test it
    print int("000011111111", 2)  # 255
 
    print
 
    # check the exceptions
    print Denary2Binary(0)
    print Denary2Binary(-5)  # should give a ValueError

