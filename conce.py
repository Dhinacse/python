def getMaxLength(arr, n): 
	count = 0
	result = 0
	for i in range(0, n): 
		if (arr[i] == 0): 
			count = 0
		else: 
			count+= 1
			result = max(result, count) 		
	return result 
arr =[101011111]
n = len(arr) 
print(getMaxLength(arr, n))
