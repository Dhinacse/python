a=[3,5,8,2,1,4,6]
b=len(a)
for i in range(b):
  for j in range(i+1,b):
    if(a[i]>a[j]):
      a[i],a[j]=a[j],a[i]
print(a)
