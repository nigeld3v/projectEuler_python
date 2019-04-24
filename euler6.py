#!/usr/bin/env python

""" Euler problem 6, completed 190421

The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
"""

sum100 = 0
sq100 = 0

# creating a list
list1 = []
list2 = []

#list out and add the first hundred numbers#
for i in range (1, 101):
  list1 += [i]

# Add all the numbers in list1
for k in range(0, len(list1)):
  sum100 = sum100 + list1[k]

# square the total of sum100
sqsum100 = sum100**2

# individually square each term from 1 to 100
for j in range (1, 101):
  j = j ** 2
  list2 += [j]

#add all these squared terms
for k in range(0, len(list2)):
    sq100 = sq100 + list2[k]

print(sqsum100-sq100)

# answer: 25164150
