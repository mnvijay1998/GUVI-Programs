n=int(input())
l=[1,1]
for i in range(n-2):
	sum=l[i]+l[i+1]
	l.append(sum)
print(*l)