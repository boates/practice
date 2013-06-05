#!/usr/bin/env python

import sys
import numpy

try:
    N = int(sys.argv[1])
except: sys.exit(1)

x = [ [1, 2, 3, 4],
      [5, 6, 7, 8],
      [1, 6, 9, 11],
      [10, -4, 4, 4]]
x = numpy.array(x)

print '2D array:'
for i in x: print ' ', i
print

if numpy.min((x - N)**2) == 0:
    print N, 'is in 2D array'
else:
    print N, 'is not in 2D array'
