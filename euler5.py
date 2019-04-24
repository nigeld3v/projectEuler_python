#!/usr/bin/env python

""" This doc to accompany Project Euler Problem 5, Completed 190422__
    - https://projecteuler.net/problem=5

2520 is the smallest number that can be divided by each of the numbers from
1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
"""
# multiply terms 11 - 20
# divide product by

m = 1
bool2 = False
bool = None

while bool2 == False:
  if(m % 11 == 0):
    bool = True
  else:
    m += 1

  if (bool == True):
    if(m % 12 == 0):
      bool = True
    else:
      bool = False
      m += 1

    if (bool == True):
      if(m % 13 == 0):
        bool = True
      else:
        bool = False
        m += 1

      if (bool == True):
        if(m % 14 == 0):
          bool = True
        else:
          bool = False
          m += 1

        if (bool == True):
          if(m % 15 == 0):
            bool = True
          else:
            bool = False
            m += 1

          if (bool == True):
            if(m % 16 == 0):
              bool = True
            else:
              bool = False
              m += 1

            if (bool == True):
              if(m % 17 == 0):
                bool = True
              else:
                bool = False
                m += 1

              if (bool == True):
                if(m % 18 == 0):
                  bool = True
                else:
                  bool = False
                  m += 1

                if (bool == True):
                  if(m % 19 == 0):
                    bool = True
                  else:
                    bool = False
                    m += 1

                  if (bool == True):
                    if(m % 20 == 0):
                      bool = True
                      bool2 = True
                    else:
                      bool = False
                      m += 1

                    if bool2 == True:
                      print(m)
# answer: 232792560
# you must find a more efficient way to do this!

"""
BETTER:
Python. Started off counting by num+=1, but took WAY too long.
However, the final product must at least be a multiple of the primes so I
counted by that instead. There's a faster mathematical way to go about it
without code, but this worked fine and was quick.

def divisble(bound):
    num = 0
    primes = primeProduct(bound)
    while (True):
        num += primes
        for x in range(2,bound+1):
         if num%x != 0:
            break
         if x == bound:
             return num

def primeProduct(bound):
    primeProduct = 1
    for x in range(2, bound+1):
       for y in range(2, x+1):
           if (y == x):
               primeProduct *= x
           if (x%y == 0):
               break
    return primeProduct
print(divisble(20))

"""

"""
ANOTHER GOOD EXAMPLE

def gcd(x, y):
   '''This function implements the Euclidian algorithm
   to find G.C.D. of two numbers'''

   while(y):
       x, y = y, x % y

   return x

def lcm(x,y):
   lcm = (x*y)//gcd(x,y)
   return lcm

lcm_val = 1

for i in range(1,21):
   lcm_val = lcm(lcm_val,i)

print(lcm_val)
"""
