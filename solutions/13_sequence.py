countries_list = ["Brazil","Croatia","Mexico","Cameroon","Spain","Netherlands","Chile","Australia","Colombia","Greece","Cote d'Ivoire","Japan","Uruguay","Costa Rica","England","Italy","Switzerland","Ecuador","France","Honduras","Argentina","Bosnia and Herzegovina","Iran","Nigeria","Germany","Portugal","Ghana","USA","Belgium","Algeria","Russia","Korea Republic"]

for i in range(len(countries_list)):
	countries_list[i]=countries_list[i].lower()
	
def next_string(a):
	n = a[-1]
	print(n)
	
	for l in countries_list:
		if l[0]==n:
			return l


def 
	
	

if __name__ == "__main__":
	print(next_string('netherlands'))