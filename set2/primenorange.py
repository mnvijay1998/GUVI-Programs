sn,ln=map(int,input().split())
sn+=1
l=[]
for i in range(sn,ln):
	fl=0
	for j in range(2,i):
		if i%j==0:
			fl=-1
			break
	if fl==0 and i >1:
		l.append(i)
print(*l)