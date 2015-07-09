# Which starting number, under one million, produces the longest chain?
import time
t0 = time.time()

# colseq function
def colseq(n=1):
    """I create a Collatz sequence starting with the input "n" and ending with 1 and return its length"""
    if n == 1:
        return 1
    elif n % 2 == 0:  # if last # is even
        return [n, colseq(n / 2)]
    else:  # if last # is odd:
        return [n, colseq(3 * n + 1)]

def flatten(*args):
    for x in args:
        if hasattr(x, '__iter__'):
            for y in flatten(*x):
                yield y
        else:
            yield x

print "the length for 6171 is", len(list(flatten(colseq(6171))))
print "the length for 77031 is", len(list(flatten(colseq(77031))))
print "the length for 156159 is", len(list(flatten(colseq(156159))))
print "the length for 230631 is", len(list(flatten(colseq(230631))))
print "the length for 345947 is", len(list(flatten(colseq(345947))))
print "the length for 410011 is", len(list(flatten(colseq(410011))))
print "the length for 511935 is", len(list(flatten(colseq(511935))))
print "the length for 626331 is", len(list(flatten(colseq(626331))))
print "the length for 704623 is", len(list(flatten(colseq(704623))))
print "the length for 837799 is", len(list(flatten(colseq(837799))))
print "the length for 939497 is", len(list(flatten(colseq(939497))))
'''
lengths = []
for x in range(1, 10000):
    lengths.append(len(list(flatten(colseq(x)))))

print lengths.index(max(lengths))+1
'''
t1 = time.time()
runtime = t1-t0
print ("%.8f seconds" % runtime)
