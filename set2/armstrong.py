n=input()
le=len(n)
n=int(n)
k=n
s=0
while(n!=0):
    r=n%10
    s=s+(r**le)
    n=n//10
if s==k:
    print("yes")
else:
    print("no")