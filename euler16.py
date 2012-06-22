#top is my try, bottom is a copy/paste.  Mine has a problem because in line 15, python does not do arithmetic precisly enough with these large ints.  have to implement arbitrary precision arithmetic functionality.  The top part works on smaller numbers though.
"""from __future__ import division
from operator import *
import math
from numpy import *
power = input("2 to what power?")
big_int = math.pow(2, power)
print "%d" % big_int
i = 0
x = 0
array = array([])
while i < 303:
    x = big_int % 10
    array = insert(array,0,x)
    big_int = floordiv(big_int, 10)
    print "big_int now: %d" % big_int
    i += 1
print array
j = 0
sum = 0
while j < len(array):
    sum = sum + array[j]
    j += 1
print sum
"""
print sum([int(i) for i in str(2**1000)]) """
#must make a string out of 2^1000, then make an int out of each char in the string, then sum all the ints.  pretty good
