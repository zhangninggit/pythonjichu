i=0
for a in range(1,101):
    if a % 2 == 0:
        print("%d"%a,end=" ")
        i+=1
        if(i % 5 == 0):
             print("")
