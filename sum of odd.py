n,k =input().split()
n=int(n)
k=int(k)
tot = 0
for num in range(n, k+1):
    if(number % 2 != 0):
        tot = tot + num
print(tot)
