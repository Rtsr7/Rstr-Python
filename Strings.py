#type conversion string to int
a= "55"
b= "this will be converted into a string"

print(type(int(a)))
#the variable a was generally an string but later in the print statement it was converted to string using the int method

#type coversion string to int
c= 55
d= "this will be converted into a string"

print(type(str(c)))
#the variable c was generally an integer but later in the print statement it was converted to string using the str method

#formatted strings
a= "this is the name of the variable"
b= 55
print(f"formatted string allows us to use {a} without using the plus operator to join the values")
#reverse a string 
str1= "formatted string"
print(str1[::-1])
#if two elements need to be skipped at once
print(str1[::-2])

