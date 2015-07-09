#
import time
import math
t0 = time.time()

n = 2

numroutes = math.factorial(4)/math.factorial(4-2)


print numroutes

t1 = time.time()
runtime = t1-t0
print ("%.8f seconds" % runtime)
