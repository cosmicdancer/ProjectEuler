__author__ = 'Neiloy'

fib = [1, 1]

while max(fib) <= 4000000:
    fib.append(fib[len(fib)-1]+(fib[len(fib)-2]))

sum = 0

for x in fib:
    if x <= 4000000:
        if x % 2 == 0:
            sum = sum + x

print(sum)
