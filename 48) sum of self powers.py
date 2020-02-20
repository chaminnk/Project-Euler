import time
start = time.time()
print sum(i**i for i in range(1,1001))
print (time.time()-start),'seconds'
