import time
import gmpy2
start=time.time()
for x in  range(10**4):
    m=(2**1000)+x
    if gmpy2.is_fermat_prp(m,2)==-1:
       print(m)
stop=time.time()-start
print(stop)
print(10**4/stop)
