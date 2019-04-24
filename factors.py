#!/usr/bin/env python

# define function
def print_factors(x):
   # This function takes a number and prints the factors
   print("factors of",x,":")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)
