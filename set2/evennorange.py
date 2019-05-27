sn,ln=map(int,input().split())
if sn%2==0:
	sn+=2
else:
	sn+=1
for i in range(sn,ln,2):
	print(i,end=' ')