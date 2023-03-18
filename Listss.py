my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# add all the elements in the list using for loop
counter = 0
for item in my_list:
    counter += item
print('\n', counter)

# range function

# range(initial, final, jump needed)
print(range(0, 10, 2))  # a single range function doesnt work individually
# range converted into list and skips 2 numbers upto 10 doesnt print 10 since 10 is the limit
print(list(range(0, 10, 2)))

# enumerate function


# check for duplicates in a list

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
new_list = []
for char in some_list:  # loops through the some_list to access all the char
    # checks if the number of instances of any char is more than 1 in the some_list
    if some_list.count(char) > 1:
        if char not in new_list:  # checks if duplicates are there in new list and doesnt add more than one instance of any char
            # one instance of the duplicate char are added in new_list
            new_list.append(char)
print(new_list)




# list comprehensions
#shorcut way to create lists 
#syntax
# listname= [expression for expression in newlist]
# listname= [expression for expression in range(initial,final,jump)]
# listname= [expression for expression in range(initial,final,jump) if code ]

list_new= [num for num in range(0,1000)]
print("\n",list_new)

list_newcreated = [char for char in 'thischar']
print("\n",list_newcreated)

num_list= [this for this in range(0,1000) if this%2==0]  #gives all even numbers between 1 to 1000
print("\n",num_list)

num_newlist= [num*2 for num in range(1,500)]
print("\n",num_newlist)


#for sets

set_new= {num for num in range(0,1000)}
print("\n",set_new)

set_newcreated = {char for char in 'thischar'}
print("\n",set_newcreated)

set_sets= {this for this in range(0,1000) if this%2==0}  #gives all even numbers between 1 to 1000
print("\n",set_sets)

set_newset= {num*2 for num in range(1,500)}
print("\n",set_newset)

#for dictionaries

new_dictionary={
    'key1': 1,
    'key2': 2,
    'key3': 3,
    'key4': 4
}

this_dictionary= {key:value for key, value in new_dictionary.items()}
print("\n",this_dictionary)



new_dictionary2={
    'key1': 1,
    'key2': 2,
    'key3': 3,
    'key4': 4
}

this_dictionary2= {a:b*2 for a, b in new_dictionary2.items()}
print("\n",this_dictionary2)



new_dictionary3={
    'key1': 1,
    'key2': 2,
    'key3': 3,
    'key4': 4
}

this_dictionary3= {a:b*2 for a, b in new_dictionary3.items() if b%2==0} #first variable in this case a is the key and the second variable in this case b is the value
print("\n",this_dictionary3)


print("List methods\n")
#List methods
list_1= ['item1', 'rich',"money"]
print(list_1)
#method 1: in
if 'item1' in list_1: #checks if the given element is in the list or not
    print("\nits there")
#method 2: append()
list_1.append("newitem") #adds the given item to the end of the list
print(list_1)

#method 3: len()
print(len(list_1)) #returns the length of the list

#method 4: count()
print(list_1.count("newitem")) #counts the number of times the given item is present

#method 5: index()
print(list_1.index("money")) #returns the index number of the given element in the list

#method 6:reverse()
list_1.reverse() #reverses the index number of the elements in the list
print(list_1) 

#method 7: sort()
list_1.sort() #sorts the list in ascending order
print(list_1) 

#method 8: copy()
list2= list_1.copy() #copies the list into another list
print(list2)

#method 9:
list_1.extend("5") #adds the given element to the list
print(list_1)

#method 10:
list_1.pop(2) #removes the item at the given index number
print(list_1)

#list operations
print("List Operations\n")
list_a=["2"]*5 #creates the given item the number of times multiplied to it
print(list_a)
list_a=[5]*20 #creates the given item the number of times multiplied to it
print(list_a)

list_b=[3,4,5,"item2",7]
sumlist= list_a+list_b
print(sumlist)
# subtraction multiplication and division dont work for lists with the normal symbols like * / 
# variablename= listname[startindex:stopindex] #prints one element before stop index
iterating= list_a[1:5]
print(iterating)
newiterating= list_a[:7] #takes default start index as 0
print(newiterating)

newiterating2= list_a[1::2] #index 1 to end while skipping every 2 elements
print(newiterating2)

print("\n",2**3/4)
672749994932560070000