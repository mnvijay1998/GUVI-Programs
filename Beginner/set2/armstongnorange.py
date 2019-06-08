sn,ln=map(int,input().split())
sn+=1
for i in range(sn,ln):
    j=str(i)
    le=len(j)
    k,n=i,i
    s=0
    while(n!=0):
        r=n%10
        s=s+(r**le)
        n=n//10
    if s==k:
        print(i,end=' ')