a=input("NAME :")
b=int(input("MOB NO :"))
sou =int(input("SOURCE :"))
des =int(input("DESTINATION :"))
if a is None and b is None and sou is None and des is None:
  print("enter the details ")
tot=des-sou
print("total diatance",tot)

choice = input("Enter choice(bike/auto/car/bus): ")
if choice =='bike':
  f=tot*5
  print("travel cost in bike",tot*5)
elif choice =='auto':
  f=tot*10
  print("travel cost in auto",tot*10)
elif choice =='car':
  f=tot*20
  print("travel cost in car",tot*20)
elif choice =='bus':
  f=tot*25
  print("travel cost in bus",tot*25)
else:
  print("Invalid input")
