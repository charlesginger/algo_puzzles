#!/usr/bin/python
def collatz(n):
	m = n
	n = 3*n+1
	while(1):
		if n==m or n==1:
			break
		elif n%2==0:
			n = n/2
		else:
			n = 3*n+1
	return(n)
			


count=0		
for i in range(2,10001):
#	print(i)
	if collatz(i)==i:
		print i
		count=count+1
	
print(count)