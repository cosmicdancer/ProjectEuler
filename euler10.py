# Find the sum of all the primes below two million
import time
t0 = time.time()

primes = [2]
num = 2000000

def is_prime(n):
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

for x in range(3, num, 2):
    if is_prime(x) == True:
        primes.append(x)

print (sum(primes))

t1 = time.time()
total = t1-t0
print ("%.8f seconds" % total)
