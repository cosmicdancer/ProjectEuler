# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum

import time
t0 = time.time()
numbers = range(1, 101)

sumsquares = []

for x in numbers:
    sumsquares.append(x ** 2)

sumsquares = sum(sumsquares)
print sumsquares
squaresums = sum(numbers) ** 2
print squaresums

print(squaresums - sumsquares)

t1 = time.time()
total = t1-t0
print ("%.8f seconds" % total)