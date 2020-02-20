import time
start = time.time()
total = 0
for m in range(2,2000000):#getting primes below 2000000
    for n in range(2,int(m**(0.5)+1)):
        if m%n==0:
            break
    else:
        total+=m #getting sum of primes
print total
print (time.time() - start),'s'
