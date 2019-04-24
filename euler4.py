#!/usr/bin/env python

""" This doc to accompany Project Euler Problem 4, Completed 190421
    - https://projecteuler.net/problem=4

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

winList = []
product = []

for n in range (999, 99, -1):
  for m in range (999, 99, -1):
    if (len(str(n*m)) == 6):
      product += [str(n * m)]

# mirror the chars in a string
def mirror(s):
  return s[::-1]

# sort palindromes from product, put into winList
for i in product:
  if(i == mirror(i)):
    winList += [i]

# print the largest term in the list
print(max(winList))

#answer: 906609
