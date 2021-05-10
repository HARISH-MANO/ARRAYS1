a=int(input().strip())
for i in range(a):
    x,y,z=input().strip().split(" ")
    x,y,z=[int(x),int(y),int(z)]
    d1=abs(x-z)
    d2=abs(y-z)
    if d1==d2:
        print("mousec")
    elif(d1<d2):
        print("cat  A")
    else:
        print("cat b")