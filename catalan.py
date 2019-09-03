def catalan(N): 
	if N <=1 : 
		return 1
	res = 0
	for i in range(N): 
		res += catalan(i)*catalan(N-i-1) 
	return res
a=int(input())
for i in range(a+1): 
	print (catalan(i),end=" ")
