#LEap Year Program
year=int(input("ENter a Year : "))
if ((year%400==0)|((year%4==0)&(year%100!=0))):
    print("Leap year")
    
else:
    print("Not a Leap year")

    
    
    
    
    
    
    
    
#printing leap years between an interval
#LEap Year Program
n=int(input("Enter the starting year"))
m=int(input("Enter the ending year"))
for i in range(n,m+1):
        
    if ((i%400==0)|((i%4==0)&(i%100!=0))):
        print(i)
    
