#!/usr/bin/python
def search(searched,N):
	cnt =0
	if len(searched) == N+1:
		return 1

	dir = [[0,1],[0,-1],[1,0],[-1,0]]
	for i in range(len(dir)):
		next_pos = [searched[-1][0]+dir[i][0],searched[-1][1]+dir[i][1]]
		if next_pos not in searched:
			print(searched+[next_pos])
			cnt = cnt + search(searched+[next_pos],N)
	
	return cnt
	
	
		

if __name__ == '__main__':
	print(search([[0, 0]], 2))