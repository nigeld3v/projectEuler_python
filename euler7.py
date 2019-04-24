#!/usr/bin/env python

"""
Solved 190422

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

steps I took were really slow and sloppy. involved watching the list and
stopping the numbers when we got to 10001... look into better ways of doing this
"""
which = 0
going = True

while going == True:
  for n in range(2, 5000000):
  #divide the current number by all integers less than it
    for x in range(2, n):
      # check for prime. if not prime, go down to else
      # if prime, break the loop and return to the first "for"
      if n % x == 0:
        break
    else:
      which += 1
      print("prime "+str(which)+": "+str(n))

# this step is supposed to stop the script
    if(which == 10001):
      print("prime "+str(which)+": "+str(n))
      break

# answer: 104743
