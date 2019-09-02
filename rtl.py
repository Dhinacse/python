import math 
def getFirstSetBitPos(n): 
	return math.log2(n&-n)+1
n =int(input())
print(int(getFirstSetBitPos(n))) 
