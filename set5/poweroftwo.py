n=int(input())
c="yes"
if n==0:
    c="no"
else:
    while(n!=1):
        if n%2!=0:
            c="no"
            break
        n=n/2
print(c)

