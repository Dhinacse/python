def solve(N, K) : 
	combo = [0] * (N + 1) 
	combo[0] = 1
	for i in range(1, K + 1) : 
		for j in range(0, N + 1) : 
			if j >= i : 
				combo[j] += combo[j - i] 
	return combo[N] 
if __name__ == "__main__" : 
	N, K = [int (x) for x in input().split()]
	print(solve(N, K))
