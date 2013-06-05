#!/usr/bin/env python

def permutations(ele,tail =''):
	if len(ele) == 0: 
		print tail
	else:
		for i in range(len(ele)):
			permutations(ele[0:i] + ele[i+1:], tail+ele[i])


def main():
    # run a test
    import sys
    s = sys.argv[1]
    permutations(s)
    
    
if __name__ == '__main__':
    main()

