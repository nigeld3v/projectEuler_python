#!/usr/bin/env python

"""
Euler Problem 9 solved: 190424

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a**2 + b**2 = c**2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

# a in range (1, 995)
# b in range (2, 996)
# c in range (3, 997)
# a ** 2 + b ** 2 == c**2
# a + b + c == 1000
# a < b < class

total = 1000
at = total - 5
bt = total - 4
ct = total - 3

for a in range (1, at+1):
  for b in range (2, bt+1):
    for c in range (3, ct+1):
      if(a < b < c and a**2 + b**2 == c**2 and a + b + c == total):
        print(">>>  "+str(a) + ", " + str(b) + ", "+ str(c))
        print (a * b * c)

#answer: 31875000
