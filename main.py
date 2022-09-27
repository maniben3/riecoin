import pyximport; pyximport.install()
import time
import c
start=time.time()
print(c.eratosthenes(10 ** 9))
stop=time.time()-start
print(stop)
