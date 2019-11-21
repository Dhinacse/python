n=list(input())
for i in range(len(n)-1):
  for j in range(i+1,len(n)):
    if(n[i]>n[j]):
      n[i],n[j]=n[j],n[i]
print(*n)
