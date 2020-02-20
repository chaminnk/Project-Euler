import time
start = time.time()
a = 0
b = 1
fib = []
for i in range(1,10000): #getting fibonacci numbers
    c = a + b
    a = b
    b = c
    fib.append(c) #getting numbers into a list
for num in fib:
    if len(str(num)) == 1000:
        print fib.index(num) + 2 #getting the required index of the result
        break
print (time.time()-start), 's'
