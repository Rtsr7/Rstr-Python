# Creating a llst 

# syntax  
# variable = [element, element, element, element] #items can be of any datatypes
# list index always starts from 1
# variable= [] #empty list
a=[1,2,3,4,5]
print(a)

#list Methods
copy_a= a.copy() #copies the list into new list
copy_a1= a[:] #copies the list into new list
print(copy_a)
print(copy_a1)

a.append(6) #adds the given element to the last
print(a)


print(a.count(1)) #counts the number of occurences of an element in the list
a.append(-1)
a.append(456)
a.append(-2)

a.sort() #sorts the given llst
print(a)
# a.append('string')
# a.sort() #sort wont work in the list containing a string


print(a.index(5)) #shows the index of the given element in the list


a.insert(4,10) #inserts 10 at index 4 in the list syntax-- insert(at which index, value)
print(a)

a.pop(5) #removes the element at the given index
print(a)

a.reverse() #reverses the list
print(a)

sorted_a= sorted(a) #sorts the list and copies it into the new variable This doesnt change the original list
print(sorted_a)
print(a)



#List slicing

b=[-1,0,1,2,3,4,5,6,7,8,9,10]

#Accessing list elements from index 0 to index 6

print(b[:7]) # nothing before : means start from 0
# the 7 after : means stop at index 6
#this is because of a null zero at the end of every list the counter stops just one index before what was specified

#Accessing list elements from index 1 to the last
print(b[1:])

#Accessing list elements from index 2 to index 7
print(b[2:8])

#Accessing the whole list
print(b[:])

# Accessing the whole list skipping two elements at a time
print(b[::2])

#Another method to reverse the list 
print(b[::-1])



#List Operations

#Creating a new list with the same elements repeated 5 times
newlist= [1]*5 
print(newlist)


#Adding two lists
newlist2=[5,35,2,5,7]
print(newlist+newlist2)

# Looping through the elements in a list
listc= [1,2,"this",3,45,5456,6,7,75,678,657,785,8,9,10,5.55]
for element in listc:
    print(element)
#Making a new list with the elements which are even
# for item in listc:
#     if item%2==0: #doesnot work since a string is there in the list
#         listeven=[]
#         listeven.append(item)
# print(listeven)
listc1= [1,2,3,45,5456,6,7,75,678,657,785,8,9,10,5.55]
for item in listc1:
    if item%2==0: #doesnot work since a string is there in the list
        listeven=[]
        listeven.append(item)
print(listeven)

#Short way of looping through list


# syntax
#  
# list=[element,element,element,element]
# newlist=[expression for variable in list]


d= ["fruits","cars","morecars","expensive cars","more expensive cars"]

d1=[item for item in d] #loops through each item in list d and puts them in a new list d1
print(d1)


#Squares the elements and returns a new list with the mulitplied elements
new=[1,2,3,4,-5]
new_1= [this*this for this in new]
print(new_1)    

#Changing the elements in a list
list_5=[1,2,24,43,5,2,532,5]
list_5[2] = "newitem" #changes the element at the given index 2 with the passed value "newitem"
print(list_5)