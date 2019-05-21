countries_list = ["Brazil","Croatia","Mexico","Cameroon","Spain","Netherlands","Chile","Australia","Colombia","Greece","Cote d'Ivoire","Japan","Uruguay","Costa Rica","England","Italy","Switzerland","Ecuador","France","Honduras","Argentina","Bosnia and Herzegovina","Iran","Nigeria","Germany","Portugal","Ghana","USA","Belgium","Algeria","Russia","Korea Republic"]

for i in range(len(countries_list)):
	countries_list[i]=countries_list[i].lower()
	
def next_country(a):
	n = a[-1]
	country_next = []
	for l in countries_list:
		if l[0]==n:
			country_next.append(l)
	return country_next
#
#
#def country_sequence(a):
#	country_last = a[-1]
#	country_next_list = next_country(country_last)
#	for l in country_next_list:
#		print(a+l)

def next_one(sequence):
	country_last = sequence[-1]

	
	
	
	#return country_sequence([a,n])
	
	

if __name__ == "__main__":
	#print(next_country('netherlands'))
#	print(country_sequence(['netherlands']))