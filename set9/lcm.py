a,b=map(int,input().split())
if a>b:
	t=a
else:
	t=b
while(1):
	if t%a==0 and t%b==0:
		l=t
		break
	t+=1
print(l)