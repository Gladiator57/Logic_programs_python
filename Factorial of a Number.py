#Factorial of a Number
n=int(input("Enter a Number : "))
fact=1
if n==0|n==1: 
    print("1")
else:
    for i in range (1,n+1):
        fact=fact*i
    else:
        print(fact)
