#!/usr/bin/python

disk_eu = [0, 32, 15, 19, 4, 21, 2, 25, 17, 34, 6, 27, 13, 36, 11, 30, 8, 23, 10,
		5, 24, 16, 33, 1, 20, 14, 31, 9, 22, 18, 29, 7, 28, 12, 35, 3, 26]
disk_us = [0, 28, 9, 26, 30, 11, 7, 20, 32, 17, 5, 22, 34, 15, 3, 24, 36, 13, 1,
		00, 27, 10, 25, 29, 12, 8, 19, 31, 18, 6, 21, 33, 16, 4, 23, 35, 14, 2]
disk = {'eu':disk_eu,'us':disk_us}		


len_disk = len(disk_eu)


def sum_n(n,m,region):
	sum_n = 0
	for i in range(n):
		sum_n = sum_n + disk[region][m+i]
	return sum_n

def sum_disk(n,region):
	sum_max = 0
	n_max = -37
#	print disk[region]
	for i in range(-len_disk,0):	
#		print(sum_n(n,i, region),disk[region][i])
		if sum_n(n,i, region)>sum_max:
			sum_max = sum_n(n,i, region)
			n_max = disk[region][i]
	return [sum_max,n_max,n]
		
		

	
if __name__ == "__main__":
	cnt = 0
	for i in range(2,36):
		print(sum_disk(i,'eu'))
		print(sum_disk(i,'us'))
		
		if sum_disk(i,'eu')[0]<sum_disk(i,'us')[0]:
			cnt += 1
	print(cnt)