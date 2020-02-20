a=0
b=1
total=0
#to get the first 100 fobonacci numbers
for i in range(1,101):
    c=a+b
    a=b
    b=c
    #to get the even fibonacci numbers less than 4 million
    if c%2==0 and c<4000000:
        #to get their total
        total+=c
print total
