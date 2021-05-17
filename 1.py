num=int(input())
temp=num
rev=0
while(num>0):
    remainder=int(num)%10
    rev=rev*10+remainder
    num=num//10
if temp==rev:
    print("the number is a palindrome")

else:
    print("the number is not a palindrome")

n=int(input())
n1,n2=0,1
print(n1,n2)
for i in range(2,n):
    n3=n1+n2
    n1=n2
    n2=n3
    print(n3,end=" ")

print()


n=int(input())
base=int(input())
temp=1
for i in range(0,base):
    temp=temp*n
print(temp)

n=int(input())
for i in range(1,n+1):
    if n%i==0:
        print(i)


n=int(input("enter the number:"))
temp=n
sum=0
while(n):
    digits=temp%10
    temp=temp//10
    fac=1
    for i in range(1,digits+1):
        fact=fac*i
    sum+=fac
    
if sum==n:
    print("the number is a strong number")
else:
    print("the number is not a strong number")



n=int(input())
#save the number in another variable 
temp=n 
sum=0
#Implementation
while(temp):
    r=temp%10 # r will have the value of the unit place digit
    temp=temp//10
    fac=1
    for i in range(1,r+1): #finding factorial
        fac=fac*i 
        
    sum+=fac #adding all the factorial
    
if(sum==n):
    print("it is a stroong number")
    
else:
    print("it is not a strong number")
    