#join method

list1=['item 1','item 2', 'item 3', 'item 4', 'item 5']
list2=[1,2,3,4,5]
tuple3=('1','2','3','4','5')
sentence= " and ".join(list1)
# sentence2= " ".join(list2) #doesnt work for integers
sentence3= " ".join(tuple3) #works for tuples and arrays too
# sentence= "\n".join(list1)
# sentence= " ".join(list1)
print(sentence)
# print(sentence2)
print(sentence3)

#join method can be used anywhere which is iterable

#Format method-- another way of writing fstrings

name= 'raise return'
age= 20
a= "The name is {} and the age is {}".format(name,age) #any number of arguments can be passed in the format method
print(a)

#with indexing

b= "The age is {1} and the name is {0}".format(name,age)
print("\n",b)
#here index of the place where the name and age is placed in the format method is passed into the curly brackets as per the requirements of the user