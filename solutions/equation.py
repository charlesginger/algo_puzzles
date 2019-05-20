#READ ＋ WRITE ＋ TALK ＝ SKILL

cnt =0 
for d in range(10):
	for e in range(10):
		for k in range(10):
			for l in range(10):
				for a in range(10):
					for t in range(1,10):
						for i in range(10):
							for r in range(10):
								for k in range(10):
									for w in range(1,10):
										for s in range(1,10):
											 if 10000*(w-s)+1000*(r+r+t-k)+100*(e+r+a-i)+10*(a+t)+d+e+k-l == 0:
											 	cnt= cnt+1
#											print(r,e,a,d,w,r,i,t,e,t,a,l,k,s,k,i,l,l)
											
print(cnt)									