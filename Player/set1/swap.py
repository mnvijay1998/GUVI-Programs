ip=input()
l=list(ip)
if len(l)%2==0:
    for i in range(0,len(l),2):
        l[i],l[i+1]=l[i+1],l[i]
else:
    for i in range(0,len(l)-1,2):
        l[i],l[i+1]=l[i+1],l[i]
for i in l:
    print(i,end="")