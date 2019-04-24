#!/usr/bin/env python


""" This doc to accompany Project Euler Problem 1, Completed 190416
    - https://projecteuler.net/problem=1
    - example code for first part
    - my solve for the second part (objective)
    - other ways to solve with code
"""

"""
>>> If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
"""
part 1
"""
# define variables
count = 1
threes = 0
fives = 0

#create loop counting up
while count < 10:
    print(count)

    # isolate multiples of three and add to threes
    if count%3 == 0:
      threes = threes + count
      print("threes: "+str(threes))
    # isolate multiples of five and add to fives
    if count%5 == 0:
      fives = fives + count
      print("fives: "+str(fives))
    count += 1
# print out the totals of each
print("sum of multiples of 3: "+ str(threes))
print("sum of multiples of 5: "+ str(fives))

print("sum of multiples of 3 and 5 together: " + str(threes + fives))

"""
part 2
"""
# define variables
count = 1
threes = 0
fives = 0

#create loop counting up
while count < 1000:
    print(count)

    # isolate multiples of three and add to threes
    if count%3 == 0:
      threes = threes + count
      print("threes: "+str(threes))
    # isolate multiples of five and add to fives
    if count%5 == 0:
      fives = fives + count
      print("fives: "+str(fives))
    # do not count multiples of both more than once!!!
    if count%15 == 0:
      fives = fives - count
      print("fives: "+str(fives))
    count += 1
# print out the totals of each
print("sum of multiples of 3: "+ str(threes))
print("sum of multiples of 5: "+ str(fives))

print("sum of multiples of 3 and 5 together: " + str(threes + fives))

"""
SOLUTION: 233168
"""

"""
# MUCH SIMPLER ANSWER FROM SOMEBODY ELSE
# create a function
def Divisible(n):
    if n%3==0 or n%5==0 :
        return True
# define the variable that will hold the increasing sum
sum_number=0
# create the loop
for n in range(1,1000):
    if Divisible(n):
        sum_number+=n
print (sum_number)
"""


"""
python using numpy

x = np.array(range(3,1000))
s = np.array([t % 3 == 0 for t in x])
t = np.array([t % 5 == 0 for t in x])
r = np.multiply(s,t) + s + t

a = sum(x[r])
"""

"""
j =0
for i in range(1000):
    if(i%3 == 0 or i%5 == 0):
        j = j + i

print(j)
"""
