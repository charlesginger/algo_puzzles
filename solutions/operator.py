#!/usr/bin/python
def operator():
	for i in range(1000,10000):
		a = int(str(i)[0])
		b = int(str(i)[1])
		c = int(str(i)[2:])
		reverse = int(str(i)[::-1])

		if a*b*c ==reverse:
			print i
		

			
			
operator()

