__author__ = 'Neiloy'


num = 600851475143
factors = []

for x in range(2, int(num ** 0.5)):
    if num % x == 0:
        factors.append(x)

for i in factors:
        if factors[-1] % i == 0:
            del factors[-1]

print factors
print max(factors)