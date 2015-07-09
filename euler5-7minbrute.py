__author__ = 'Neiloy'

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

divisors = range(11, 21)
quotient = 21
sumremainders = 1

import time

t0 = time.time()
while sumremainders != 0:
    sumremainders = 0
    for x in divisors:
        sumremainders += quotient % x
    if sumremainders == 0:
        print ('The smallest positive number that is evenly divisible by all of the numbers from 1 to 20 is '), quotient
    else:
        quotient += 1
t1 = time.time()
total = t1-t0
print(str.format('{0:.3f}', total))