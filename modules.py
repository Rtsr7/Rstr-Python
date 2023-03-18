import testmodule1 as ts #importing the testmodule1
#import testmodule1 #we can also import like this but we gave it a small name for ease in calling later
#import testmodule1 as anything
a= int(input("Enter num1: "))
b= int(input("Enter num2: "))
print("Sum: ",ts.add(a,b)) #ts means calling the testmodule1 file and .add means the function name after the dot. If there are more functions to be created in testmodule1 and used in this file or any other file we can just simply call it as ts or any name which was given by us and the dot function name 