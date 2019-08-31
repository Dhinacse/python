def checkValidity(a, b, c): 
	if (a + b <= c) or (a + c <= b) or (b + c <= a) : 
		return False
	else: 
		return True		
a,b,c=[int (x) for x in input().split() ]
if checkValidity(a, b, c): 
	print("yes") 
else: 
	print("no") 
