n=input()
l=['a','e','i','o','u','A','E','I','O','U']
if n in l:
	print("Vowel")
if n not in l:
	if n>='a' and n<='z' or n>='A' and n<='Z':
		print("Consonant")
	else:
		print("invalid")