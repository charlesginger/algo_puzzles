#for i in range(10,1000):
i=11
while i>10:
#	if str(i)==str(i)[::-1]
#		print(i)
	a = bin(i).replace('0b','')
#	print(a)
	b = oct(i)[1:]
	c = str(i)
	
	if a==a[::-1] and b==b[::-1] and c==c[::-1]:
		print(c)
		print(a)
		print(b)
		break
	else:
		i=i+2
		

	
	
