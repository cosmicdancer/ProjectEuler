__author__ = 'Neiloy'

answer = 0

for x in range(1, 1000):
    if x % 3 == 0:
        answer = answer + x
    elif x % 5 == 0:
        answer = answer + x

print (answer)
