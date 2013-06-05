#!/usr/bin/env python
import sys

def FizzBuzz(n=100):

    for i in range(1, n):
        s = ''
        if i % 3 == 0: s += 'Fizz'
        if i % 5 == 0: s += 'Buzz'

        if i % 3 == 0 or i % 5 == 0: print s
        else: print i


def main():

    try: n = int(sys.argv[1])
    except IndexError: n = 100

    FizzBuzz(n)


if __name__ == '__main__':
    main()
