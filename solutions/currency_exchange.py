#!/usr/bin/python

#500 100 50 10

def exchange(n):
	currency = [500,100,50,10]
	count = range(4)
	times = 0

		
	for count[0] in range(0,min(int(n/currency[0]),15)+1):
		for count[1] in range(0,min(int(n/currency[1]),15)+1):
			for count[2] in range(0,min(int(n/currency[2]),15)+1):
				for count[3] in range(0,min(int(n/currency[0]),15)+1):
					if currency[0]*count[0]+currency[1]*count[1]+currency[2]*count[2]+currency[3]*count[3]==1000:
						print(count)
						times = times+1
	
	print(times)
					
		
	

	
exchange(1000)
	