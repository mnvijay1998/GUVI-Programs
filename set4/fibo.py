n=int(input())
l=[1,1]
for i in range(n-2):
	sum=l[i]+l[i+1]
	l.append(sum)
if n>=2:
	print(*l)
if n==1:
	print(l[0])