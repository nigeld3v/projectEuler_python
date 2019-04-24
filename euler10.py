#!/usr/bin/env python

"""
Euler Problem 10 solved: 1904
- https://projecteuler.net/problem=10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
# prime finder

def euler10():
    answer = 0
    for n in range(2, 2000000):
      for x in range(2, n):
        if n % x == 0:
          break
      else:
        answer += n
    print(answer)

euler10()
