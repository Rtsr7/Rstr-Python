set1= {1,2,3,4,5}
set2= {1,2,3,5,6,"last element"}

newset= set1.copy() #copies the current set to the new set
print("\n",set1,"\n",set2,"\n",newset)

#setmethods
set1.add("new element") #adds new element to the last 
#sets dont have indexing
print("\n",set1)

# set1.clear() #clears the whole set
# print("\n",set1)

print("\n",set1.difference(set2)) #shows the uncommon elements between set1 and set2 it can show the uncommon elements between more than one set
# set1.difference_update(set2) #updates the uncommon elements between set1 and set2 into set1
# print("\n",set1)
print("\n",set1.intersection(set2)) #shows the common elements between set1 and set2
# set1.intersection_update(set2) #updates the common elements between set1 and set2 into set1

# print("\n",set1)

print("\n",set1.isdisjoint(set2))  #returns true if two sets have no common elements in them else returns false
print("\n",set1.union(set2))   #makes a new set with the elements of both the sets and removes any duplicates
# there are symbols which gives intersection and union for two or more sets
# the symbol & gives intersection of two sets and the symbol | gives union of two sets

print("\n", set1|set2)
print("\n", set1&set2)
set3= {1,2}
print("\n",set1.issubset(set2)) #returns true if set2 has all the elements of set1 else returns false
print("\n",set1.issuperset(set2)) #returns true if set1 has all the elements of set2 else returns false
print("\n",set3.issubset(set1))
print("\n",set1.issuperset(set3))