n=input()
c=0
for i in n:
	if i.isnumeric()==False and i.isalpha()==False and i!=" ":
		c+=1
print(c)