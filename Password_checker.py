name= input("Enter your name here: ")
password= input("Enter your password here: ")
length= len(password)
hiddenpassword= len(password)*"*"
print(f"\nGreetings {name}\nYour password {hiddenpassword} is {length} characters long")



#Advanced version
# name= input("Enter your name here: ")
# password= input("Enter your password here: ")
# print("\nGreetings",name,"\nYour password",len(password)*"*","is",len(password),"characters long")