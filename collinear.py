def collinear(x1, y1, x2, y2, x3, y3): 
	a = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2) 
	if (a == 0): 
		print("yes")
	else: 
		print("no")
x1,y1=[int (x) for x in input().split()]
x2,y2=[int (x) for x in input().split()]
x3,y3=[int (x) for x in input().split()]
collinear(x1, y1, x2, y2, x3, y3) 
