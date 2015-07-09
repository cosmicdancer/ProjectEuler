# What is the 10 001st prime number?
import time
t0 = time.time()

primes = [2, 3, 5, 7, 11, 13]
test = 17

def is_prime(n):
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

while len(primes) < 10002:
    if is_prime(test) == True:
        primes.append(test)
        test += 2
    else:
        test += 2

print primes[10000]

t1 = time.time()
total = t1-t0
print ("%.8f seconds" % total)
