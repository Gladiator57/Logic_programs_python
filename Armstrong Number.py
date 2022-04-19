#Armstrong Number
n=int(input("Enter a Number"))
b=0
t=n
while(n>0):
    a=n%10
    b=b+a*a*a
    n=n//10
if b==t:
    print("Armstrong")
else:
    print("Not Armstrong")
    
    
    #Armstrong in an Interval
    
    #Armstrong Number
# Armstrong Number
p = 1
q = 500
for i in range(p,q+1):
    b = 0
    t = i
    while t > 0:
        a = t % 10
        b = b + a * a * a
        t = t // 10
        if b == i:
            print(b)
