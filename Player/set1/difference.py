x,y=input().split()
c=0
for i in range(0,len(x)):
    if x[i]!=y[i]:
        c+=1
if c>1:
    print("no")
else:
    print("yes")