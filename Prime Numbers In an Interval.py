a=int(input("Enter 1st number"))
b=int(input("Enter 2nd Number"))
for i in range (a,b):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)
            

