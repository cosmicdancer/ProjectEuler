# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a**2 + b**2 = c**2
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
import time
t0 = time.time()

def prod_triplet_w_sum(n):
    for a in range(1,n,1):
        for b in range(1,n-a,1):
            c = n-a-b
            if a**2+b**2==c**2:
                print a, b, c
                print 'abc = ', a * b * c
    return 0

prod_triplet_w_sum(1000)

t1 = time.time()
total = t1-t0
print ("%.8f seconds" % total)
