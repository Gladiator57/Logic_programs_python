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
        
        
        
        
        
        #Factorial using Recursion
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
    
n=int(input('Enter a Number : '))
fact(n)
result=fact(n)
print(result)
