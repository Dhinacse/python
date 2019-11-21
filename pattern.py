a=int(input())
o=1
for i in range(1,a+1):
  c=(a-i)*" "+i*"* "
  print(c)
for j in range(a-1,-1,-1):
  d=(o)*" "+"* "*j
  o=o+1
  print(d)
