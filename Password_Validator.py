password = input("enter the password: ")
length = len(password)
print(length)
if length >=8 and password.isalnum():
  print("password is valid!")
else:
  print("password is invalid")
