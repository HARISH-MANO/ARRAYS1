n1=int(input())
n2=int(input())
arr=[]
if n1>n2:
    smaller=n2
else:
    smaller=n1
for i in range(1,smaller+1):
    if n1%i==0 and n2%i==0:
        arr.append(i)

print(max(arr))