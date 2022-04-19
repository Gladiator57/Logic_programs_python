#Fibonacci Number using Functions

def fibo(n):
    a=0
    b=1
    if n==1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c=a+b
            a=b
            b=c
            print(c)

n=int(input("Enter the number to find fibonacci series"))
fibo(n)



#Fibonacci using Recursion
def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-2)+fibo(n-1)
    
number= int(input("Enter the Number : "))
for n in range(0,number):
    print(fibo(n))
