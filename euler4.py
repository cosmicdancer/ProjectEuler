__author__ = 'Neiloy'

# Find the largest palindrome made from the product of two 3-digit numbers

palindromes = []

# create list of three digit numbers
for x in reversed(range(100, 999)):
    # create second list of three digit numbers
    for y in reversed(range(100, 999)):
        # multiply numbers
        product = x * y
        # check if palindrome
        if str(product) == str(product)[::-1]:
            # store as palindromes
            palindromes.append(product)

print max(palindromes)