#L = ['LLL','GGG','LLG','LGL','LGG','GLL','GLG','GGL']
L = []
fkc = input()
C = input()
n,u = map(int,raw_input().split())
L = ['L','G']
for k in range(fkc-1):

	#L = ['L','G']
	X = ['L'+x for x in L]
	Y = ['G'+x for x in L]
	L = X+Y
	#C = input()
	#n = input()
O = []
for S in L:
	#S = raw_input()
	T = S
	l = len(S)
	
	opt = ""
	for c in range(C-1):
		opt = ""
		for s in T:
			if s == 'L':
				opt += S
			elif s == 'G':
				opt += 'G'*len(S)
		T = opt
		
#print opt

	i = 1
	j = 0 	
	pt = ""
	ans = ""
	pichi = ""
	for s in opt:
		pt += s +" "+ str(i)+" j: "+str(j)+" ,"
		ans += s
		pichi += s
		i = i+1
		j = j+1
		if j == l**(C-1):
			j=0
			ans += " , "
				
			#print pt	
	print S,ans.split(",")
	O.append(pichi)
	print pichi[n-1],pichi[u-1]

l = len(O[0])
n = len(O)
LS = []
for i in range(l):
	c = 0	
	for j in range(n):
		if O[j][i] == 'G':
			c += 1
	LS.append(c)

print LS	

m =  max(LS)
print "max",m
#print fkc

c =0
f = -1
for j in range(len(LS)):
	if LS[j] == m:
		c += 1
		if f == -1:
			f = j+1
		print j+1


print "count",c,"max",m,"first",f
'''
while True:
	l = input()
	print opt[l-1]
'''
