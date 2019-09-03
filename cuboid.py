def volumeCuboid( L,B,H): 
	return (L *B * H) 	
def surfaceAreaCuboid( L,B,H): 
	return (2 * L * H + 2 * H* B + 2 * L * B) 
L,B,H =[int (x) for x in input().split()]

print(surfaceAreaCuboid(L,B,H),volumeCuboid(L,B,H))
