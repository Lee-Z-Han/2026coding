# week14-1.py CPE 2026-05-26 26D2 UVA10189
t = 1
while True:
	M, N = list(map(int, input().split())) # Step01
	if M==0 and N==0: break # Step01: Input
	a = []
	for i in range(M):
		a.append(list(input())) # Step03: list()
		
	for i in range(M):
		for j in range(N):
			if a[i][j]=='*': continue # Step06
			a[i][j] = 0 # Step06
			for ii in range(i-1,i+2): # Step04
				for jj in range(j-1,j+2):
					if ii<0 or jj<0 or ii>=M or jj>=N:
						continue # Step05
					if a[ii][jj]=='*': # Step06
						a[i][j] += 1 # Step06
						
	if t>1: print() # Step02: Output
	print( f'Field #{t}:' ) # Step02: Output
	for i in range(M): # Step02: Output
		#print(a[i])
		for j in range(N):
			print(a[i][j], end='')
		print()
	t += 1