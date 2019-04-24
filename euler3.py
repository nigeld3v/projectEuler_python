#!/usr/bin/env python

""" This doc to accompany Project Euler Problem 3, Completed 190418
    - https://projecteuler.net/problem=3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

"""
n = 1
create while loop within a while loop, second
  n += 1 until 600851475143
  if n%y == 0 (means divisible), print the number

to verify primes are being pulled, just find a list of primes and make sure the
first 15 terms are primes
"""

"""
PRIME FINDER:

for n in range(2, 100):
  for x in range(2, n):
    if n % x == 0:
      break
  else:
    print("prime: "+str(n))
"""
"""
From working with Shana @ ThoughtWorks

primeList = []

def PrimeFinder(n, c):
  for n in range(2, c):
    for c in range(2, n):
      if n % c == 0:
        break
    else:
      primeList.append(n)

factorList = []

def factors(c):
   print("factors of",c,":")
   for n in range(1, c + 1):
       if c % n == 0:
           factorList.append(n)

winList = []

PrimeFinder(2, 600851475143)
# print(primeList)
factors(600851475143)
# print(factorList)
for x in primeList:
  for y in factorList:
    if x == y:
      winList.append(x)
print(winList)

# NOTE: The above code, while technically correct, is a super inefficient way to
# get this done. It takes forever. Think about the target.
"""

def factors(c):
  factorList = []
  i = 2
  while i <= c:
    while c % i == 0:
      c /= i
      """
      /= is shorthand for / and =.
      Example:
      x = 12
      x /= 3
      # equivalent to
      x = x / 3
      """
      factorList += [i]
    i += 1
  return factorList

def largeFactor(c):
  return factors(c)[-1]

print(largeFactor(600851475143))

### Answer is 6857
