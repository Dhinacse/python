a=float(input())
b=float(input())
choice=input("choose add/sub/mul/div :")
if choice=="add":
  ans=a+b
  print(ans)
elif choice=="sub":
  ans=a-b
  print(ans)
elif choice=="mul":
  ans=a*b
  print(ans)
elif choice=="div":
  if a==0:
    print("0")
  elif b==0:
    print("infinity")
  else:
    ans=a/b
    print(ans)
else:
  print("Please enter the choice given")
