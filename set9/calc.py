l=input().split()
for i in range(0,len(l),3):
	a=int(l[i])
	b=int(l[i+2])
	if l[i+1]=="%":
		print(a%b)
	if l[i+1]=="/":
		print(a/b)
	