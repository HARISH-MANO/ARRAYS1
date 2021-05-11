def countingvalleys(steps,path):
    count=0
    result=0
    for i in path:
        if i=='U':
            count+=1
        else:
            count-=1
        if count==0 and i=='U':
            result+=1
    return result

steps=int(input())
path=input()
r=countingvalleys(steps, path)
print(r)