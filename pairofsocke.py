def matchingpairs(arr,n):
    s=set(arr)
    c=0
    for i in s:
        c+=arr.count(i)//2
    return c

n=9
arr=[10,20,10,20,30,20,30,30,10]
r=matchingpairs(arr, n)
print(r)