list = []
for n in range(2,110000): #to get the range of prime numbers
    for m in range(2,int(n**(0.5)+1)):#chosing wether prime or not
        if n%m==0:
            break           
    else:
        list.append(n)#getting primes in a list
print list[10000]#choosing 10001th element of the list
