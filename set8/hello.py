n=input()
l=list(n)
lc=len(l)//2
if len(l)%2!=0:
	l[lc]="*"
else:
	l[lc]="*"
	l[lc-1]="*"
for i in l:
    print(i,end='')