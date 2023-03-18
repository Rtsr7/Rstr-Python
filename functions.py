# def function1(argument1,argument2): #syntax
#     execute code
#    return something
# function1() #calling the function

# def function1():
#     print('this is function 1')


# function1()

# Check age


# def checkAge():
#     while True:
#         age = input("Enter your age: ")
#         if age == '':
#             pass  # creating loop until something is entered
#         else:
#             break
#     age = int(age)  # typecasting string age into int
#     if age > 18 and age < 150:
#         print('Powering on...\nEnjoy your ride')
#     elif age < 18:
#         print('Sorry, you are too young to drive this\nPowering off...')
#     elif age == 18:
#         print('Congratulations on your first year of driving\nEnjoy your ride...')
#     elif age > 150:
#         print('Sorry but you should be resting right now...\nPowering off')
#     else:
#         print('Enter your age properly')


# checkAge()




# def docstrings(a):
#     '''
#     this function prints argument a
#     ''' #this ''' is a docstring can be used to identify functions later in the code

#     print(a)


# help(docstrings) #displays everything within the docstring in the function



# *args and **kwargs


# def argsfunc (args):
#     print(args)
#     return sum(args)
# print(argsfunc(1,2,3,4,5)) #doesnt work since only one positional argument was given in function

# def argsfunc(*args):
#     print(args)
#     return sum(args)
# print(argsfunc(1,2,3,4,5)) #the *args takes infinite positional arguments

# def kwargsfunc(*args,**kwargs):
#     print(kwargs) #returns a dictionary of the kwargs means keyword arguments given
#     return sum(args)
# print(kwargsfunc(12,3,3,4,4,5, kwargs1= 5, kwargs2 =6))

# fing the max even number from a list

# def highest_even(list1):
#     even=[]
#     for item in list1:
#       if item%2==0:
#          even.append(item)  
#     return max(even)



# # ([1,2,3,4,5,6,7,8])

          
# print(highest_even([1,2,3,4,5,6,7,8]))

 

