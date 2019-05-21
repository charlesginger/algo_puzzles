countries_list = ["Brazil","Croatia","Mexico","Cameroon","Spain","Netherlands","Chile","Colombia","Greece","Cote d'Ivoire","Japan","Uruguay","Costa Rica","England","Italy","Switzerland","Ecuador","France","Honduras","Bosnia and Herzegovina","Iran","Nigeria","Germany","Portugal","Ghana","USA","Belgium","Algeria","Russia","Korea Republic"] #,"Argentina","Australia"

for i in range(len(countries_list)):
	countries_list[i]=countries_list[i].lower()
	
def next_country_list(a):
	n = a[-1]
	country_next_list = []
	for l in countries_list:
		if l[0]==n:
			country_next_list.append(l)
	return country_next_list


def seq_count(sequence,cnt):

	country_last = sequence[-1]
	next_country =next_country_list(country_last)
	
	for c in next_country:
		if c not in sequence:
			print(sequence+[c])
			print(len(sequence+[c]))
			
			seq_count(sequence+[c],cnt+1)

	

	
if __name__ == "__main__":
	#print(next_country('netherlands'))
#	print(country_sequence(['netherlands']))
#	print(seq_count(['netherlands'],1))
	for c in countries_list:
		print(seq_count([c],1))
	