import time
start = time.time()
powers = []
powers2 = []
for a in range(2,101):
    for b in range(2,101):
        c = a**b #getting powers
        powers.append(c) #getting results to a list
powers.sort() #sorting list
for i in powers:
    if i in powers and i not in powers2: #eleminating similiar results
        powers2.append(i)
print len(powers2) #getting number of elements in the list
print (time.time() - start),'s'
