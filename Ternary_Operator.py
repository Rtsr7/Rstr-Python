# Syntax
# variable= value if condition_is_true else value 
boolflag= True

ternary_operator_used= print("printing this is true") if boolflag else print("printing this is not true since conditions is false")



# is and ==

# == checks for equality in value while  is  checks for equality in memory location

print(1=='1') #string cannot be equal to integer
print(True=='') #anything empty is 0 means false which cannot be equal to true
print([]==[]) #empty arrays are false
print(5.5==5)
print(5.0==5) #the value of 5.0 is equal to 5 while 5.5 is greater than 5 so its evaluated as true and 5.5 == 5 as false

# == converts all data types into each others types except for strings and integers
print('\n\n')
print(1 is '1') 
print(True is '') 
print([] is []) 
print(5.5 is 5)
print(5.0 is 5) 

# is checks the memory location of each of the variables so everything is returned as false
# for the is to be true the value and data type should be same
# for the empty lists since every list be it empty or not is created in a new location in the memory so the is returns false

print('1' is '1')
print(5.0 is 5.0)
print(5.0 is 5.00000)
















