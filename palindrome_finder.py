#!/usr/bin/env python
'''
Use the code below to find all the palindromes in a large block of text :)
'''

def reverse(s):
  str = ""
  for i in s:
    str = i + str
  return str

palindromes = []

paragraph = """ENTER BLOCK OF TEXT HERE TO SIEVE OUT PALINDROMES"""

for i in paragraph.split():
  if(i == reverse(i)):
    palindromes += [i]

print(palindromes)
