
def sqrt_shortest_int(n):
	n_sqrt = (n**0.5)
	sqrt_str = str(n_sqrt).replace('.','')
	sqrt_set = (set(list(sqrt_str[0:10])))
	return len(sqrt_set)
	

def sqrt_shortest_noint(n):
	n_sqrt = (n**0.5)
	sqrt_str = str(n_sqrt).split('.')[1]
	sqrt_set = (set(list(sqrt_str[0:10])))
	return len(sqrt_set)		


if __name__ == "__main__":
	n=1
	while(1):
		if sqrt_shortest_int(n)==10:
			print(n,n**0.5)
			break
		else:
			n+=1

	n=1	
	while(1):
		if sqrt_shortest_noint(n)==10:
			print(n,n**0.5)
			break
		else:
			n+=1