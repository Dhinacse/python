import random
account_number=random.randint(1000,2000)
l=[]
print("WELCOME TO OUR BANK")
select=input("Create New Account(CA)/Login Account(LA)/Customer service(CS) :")
if(select=="CA"):
  a=account_number
  print("Your Account number is :",a)
  name=input("Enter Your Name :")
  password=input("Enter Password :")
  address=input("Enter Address :")
  l.append(a)
  l.append(name)
  l.append(password)
  l.append(address)
  
elif(select=="LA"):
  b=input("enter account number :")
  print("Welcome",name)
user_name=input("enter user name :")
password=input("enter password :")
balance=5000
choice=int(input("1.Deposit/2.Withdraw/3.Balance/4.profile/5.Log Out"))
if(choice=="1"):
  l=int(input("enter the amount to debit :"))
  balance=balance+l
  print(l+"is debited and the available balance is",balance)
elif(choice=="2"):
  m=int(input("enter the amount to Withdraw :"))
  balance=balance-m
  print(l+"is debited and the available balance is",balance)
elif(choice=="3"):
  balance=balance
  print("available balance is :",balance)
elif(choice=="4"):
  print("user profile")
  print(name,address)
else:
  exit()
