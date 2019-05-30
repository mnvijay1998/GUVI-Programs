l=[int(x) for x in input().split()]
for i in range(0,len(l),2):
	print(abs(l[i]-l[i+1]))