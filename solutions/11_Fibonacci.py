#!/usr/bin/python
from functools import lru_cache

@lru_cache()
def fibonacci(n):
	if n ==1 or n==2:
		return 1
	else:
		return (fibonacci(n-1)+fibonacci(n-2))
		
def clear_devide(n):
	dgt = list(str(n))
	sum_dgt = 0
	for i in range(len(dgt)):
		sum_dgt += int(dgt[i])
	return n%sum_dgt
		
if __name__ == "__main__":
#	print(fibonacci(6))
#	print(clear_devide(144))
	
	cnt = 0
	i =3
	while(1):
		if cnt == 11:
			break
		else:
			if clear_devide(fibonacci(i))==0:
				print(fibonacci(i))
				cnt+=1
			i+=1
	
	
#!/usr/bin/python

# coding=utf-8

#
#from functools import lru_cache
#
#
#def get_all_numbers_sum(n):
#	tmp = n
#	value = 0
#	while n > 0:
#		value += n % 10
#		n //= 10
#	return tmp % value == 0
#
#
#@lru_cache()
#def fibonacci(n):
#	if n < 2:
#		return 1
#	return fibonacci(n - 1) + fibonacci(n - 2)
#
#
#def is_validated():
#	count = 0
#	for i in range(100):
#		tmp = fibonacci(i)
#		if get_all_numbers_sum(tmp):
#			count += 1
#			print(tmp)
#
#
#if __name__ == '__main__':
#	is_validated()