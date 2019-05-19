#!/usr/bin/python

import datetime

def date_loop(n):
	date_dec = int(str(n).replace('-', ''))
	date_bin = bin(date_dec).replace('0b', '')
	if date_bin[::-1]==date_bin:
		return 1

#date_loop(datetime.date(1964, 10, 10))

begin = datetime.date(1964, 10, 10)
end = datetime.date(2020, 7, 24)

count = 0
for i in range((end-begin).days+1):
	new_date = begin+datetime.timedelta(days=i)
	if date_loop(new_date)==1:
		count+=1
		print(new_date)
print(count)

