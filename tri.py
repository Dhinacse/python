def checkValidity(a, b, c): 
	if (a + b <= c) or (a + c <= b) or (b + c <= a) : 
		return False
	else: 
		return True		
a = 3
b = 4
c = 5
if checkValidity(a, b, c): 
	print("yes") 
else: 
	print("input error") 
