list1=[1,2,3,4,5]
def square(n):
    return n*n
    


#syntax-- map(function,inputlist)  #applies the function to all the items in the inputlist
print(list(map(square,list1))) #squares the list then the map function is typecasted into a list and then its printed


#Filter syntax-- filter(function,inputlist)
#filter returns a list containing all the elements which meets the condition True

list2=[1,2,3,4,5,6,7,8,9,10]
lambdafunction= lambda item: item>5

# lambda syntax-- lambda variable: condition #the elements meeting the condition are returned 

print(list(filter(lambdafunction,list2))) #returns numbers greater than 5
print(list(map(lambdafunction,list2))) #difference between map and filter

#Reduce syntax

# reduce(function,inputlist) #reduce iterates the condition in the function through all the elements in the input list and returns a total 

#reduce is not built in so we need to import reduce from functools

from functools import reduce

list3=[1,2,3,4,5,6,7,8,9,10]

sum1= lambda a,b:a+b

create= reduce(sum1,list3)
print(create)