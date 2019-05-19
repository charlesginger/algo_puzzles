def division_count(a):
	count = 0
	for i in range(2,101):
		if a%i==0 :
			count=count+1
	return count


def fold():
	for i in range(1,100):
		count = division_count(i)
		if count%2==0:
			print i
		

#print division_count(100)
fold()