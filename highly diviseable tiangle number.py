for n in range(1,10000000):
    d = []
    t=n*(n+1)/2
    for i in range(1,int(t**0.5+1)):
        if t%i==0:
            d.append(i)
            x=len(d)
            if x == 500:
                print t
                break
            else:
                 continue
