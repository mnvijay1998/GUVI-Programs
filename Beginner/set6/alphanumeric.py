n=input()
num,alp=0,0
for i in n:
    if i.isnumeric() and num==0:
        num=1
    if i.isalpha() and alp==0:
        alp=1
if num==1 and alp==1:
    print("Yes")
else:
    print("No")