#!/usr/bin/env python


""" This doc to accompany Project Euler Problem 2, Completed 190416
    - https://projecteuler.net/problem=2
    - my solve for the objective
    - other ways to solve with code
"""
"""
Each new term in the Fibonacci sequence is generated by adding the previous two
terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed
four million, find the sum of the even-valued terms.
"""

n = 0
x = 1
y = 2
while x < 4000000 and y <4000000 :
    if x%2 == 0:
      n = n + x
      #print(x)
    if y%2 == 0:
      n = n + y
      #print(y)
    x = x + y
    y = x + y
print("answer to this: "+ str(n))
