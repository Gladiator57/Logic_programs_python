# function which return reverse of a string
 
def isPalindrome(s):
    return s == s[::-1]
 
 
# Driver code
s = "malayalam"
ans = isPalindrome(s)
 
if ans:
    print("Yes")
else:
    print("No")
    
    
    
    #NUmber Palindrome Checking
p=int(input("Enter Number of digits of palindrome"))
n=12321
temp=n
rev=0
for i in range(1,p+1):
    a=n%10
    rev=rev*10+a
    n=n//10
if rev=temp:
    print("Palindrome")
else:
    print("Not palindrome")
    
    
