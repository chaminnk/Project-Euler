for x in range(1,200000000):
    for n in range(1,21):
        if x%n!=0:
            break
    else:
        print x
        print raw_input("enter")
        
