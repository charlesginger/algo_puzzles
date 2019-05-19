#!/usr/bin/python

n = 1
m = 3
count = 0
nn = 20

def cut(m,nn):
	n = 1
	count = 0
	while(1):
		if n<m:
			n = 2*n
		else:
			n = n+m
		count = count+1
		
		print(count,n)
		if n>nn:
			break		
	print('done')
	
#cut(3, 20)
#cut(5,100)

def cutbar(m,n,current):
	if current>n:
		return 0
	elif current < m:
		x = 1 + cutbar(m, n, current*2)
		return x
	else:
		x = 1 + cutbar(m, n, current+m)
		return x
		
	
print cutbar(3, 20, 1)
	

