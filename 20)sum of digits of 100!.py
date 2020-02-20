import time
start = time.time()
total = 1
for num in range(1,100):
    total*=num #getting 100!
total2 = 0
for digit in str(total):
    total2+=int(digit) #getting sum of digits in 100!
print total2
print (time.time() - start),'s'
