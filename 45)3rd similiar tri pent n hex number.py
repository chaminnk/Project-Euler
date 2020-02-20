tri = []
pent = []
hex = []
for n in range(1,300000):
    t = n*(n+1)/2
    tri.append(t)
    p = n*(3*n-1)/2
    pent.append(p)
    h = n*(2*n-1)
    hex.append(h)
for i in tri:
    if i in pent and i in hex:
        print i
#15 minutes approx.
