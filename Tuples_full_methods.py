a= (1,2,3,4,"this",4,3,45,325,23,5,2345,245,3245,324)
print(len(a)) #prints the length of tuple

# a[0]=5 #doesnot work since tuples are immutable
print(a[0])

print(a.count(4)) #counts the number of occurences of the given element in the tuple


# converting tuple to a list
print(list(a))

list1=[1,2,2,4,5]


#converting list to tuple
print(tuple(list1))


# Unpacking a tuple
c= (1,2,3)
this1, this2, this3 = c
print(this1)
print(this2)
print(this3)
#This assigns the index 0 to this1, index 1 to this 2 and index2 to this3

# for accessing multiple elements at once we can use
c1=(1,2,3,4,5,6,7,8,9,10)
item, *item2 =c1
print(item) #value at index 0 is assigned to item
print(item2) #all the values are assigned to item2 and returned in the form of a list





# Tuple slicing
b=(-1,0,1,2,3,4,5,6,7,8,9,10)

#Accessing tuple elements from index 0 to index 6

print(b[:7]) # nothing before : means start from 0
# the 7 after : means stop at index 6
#this is because of a null zero at the end of every tuple the counter stops just one index before what was specified

#Accessing tuple elements from index 1 to the last
print(b[1:])

#Accessing tuple elements from index 2 to index 7
print(b[2:8])

#Accessing the whole tuple
print(b[:])

# Accessing the whole tuple skipping two elements at a time
print(b[::2])

#Another method to reverse the tuple 
print(b[::-1])



#Printing the size of list or tuple
list2=[1,2,343,42,5]
tuple1=(1,2,343,42,5)
import sys #we need to import the builtin function sys to use the sys.getsizeof method

print(sys.getsizeof(list2)) #the sys.getsizeof() method returns the size in bytes
print(sys.getsizeof(tuple1))


#We can find the time taken to execute one statement using the timeit method
import timeit
print(timeit.timeit(stmt="[1,2,3,4,5]",number=5000)) #repeats the statement 5000 times and prints the time taken to do so
print(timeit.timeit(stmt="(1,2,3,4,5)",number=10000)) #repeats the statement 5000 times and prints the time taken to do so


#It takes less time to create a tuple than a list