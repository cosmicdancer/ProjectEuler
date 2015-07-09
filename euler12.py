# What is the value of the first triangle number to have over five hundred divisors?
import time
t0 = time.time()

trinum = [1]
nfactors = 0

while nfactors < 500:
    trinum.append((len(trinum) + 1) + trinum[-1])
    nfactors = 0
    for y in range(1, int(trinum[-1] ** 0.5)):
        if trinum[-1] % y == 0:
            nfactors += 2

print trinum[-1]
t1 = time.time()
total = t1-t0
print ("%.8f seconds" % total)
