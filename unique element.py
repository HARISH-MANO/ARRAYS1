def unique(arr):
    s=set(arr)
    for i in s:
        if arr.count(i)==1:
            return i

arr=[1,2,3,4,3,2,12,1,4]
result=unique(arr)
print(result)
