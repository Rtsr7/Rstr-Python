list1 = ["list item 1", 'list item 2', 3, True, "last list item"]
# accessing list items
print("\n", list1[0])  # first element
print("\n", list1[0:])  # all elements starting from first element
print("\n", list1[:])  # all elements
# all elements starting from first element skipping one at a time
print("\n", list1[0::2])
# all elements starting from first element skipping two at a time
print("\n", list1[0::3])

# changing values of particular list items
list1[0] = "changed list item"  # changing the value of first item
list1[3] = "new list item"  # changing the value of third item
print("\n", list1[0])
print("\n", list1[3])
print("\n", list1)

# making two lists equal
list2 = [10, 5, "list item 3"]
list2 = list1
print("\n", list2)

# chqnging the values of a list item in list2 to see if list1 also changes
list2[0] = "changed first item"
print("\n", list2)
# the value of the first item of list1 also changes since list2=list1
print("\n", list1)


# matrices or multidimensional lists

matrix1 = [["item 1", 2, 3, "new item", "last item"], [
    "item1 list2", "item 2 list2", 5], ["two items here", 1]]  # 2d list
print(matrix1)
# accessing elements
# shows the first list containing ["item 1",2,3,"new item","last item"]
print("\n", matrix1[0])
print("\n", matrix1[0][1])  # shows the second element of first list
print("\n", matrix1[1][1])  # shows the second element of second list

# 3d list
matrix2 = [[[1, 2, 3], [6, 7, "list 2 of list 1"]], ["list 2", "item 2"]]
# accessing elements
# shows first element of list 2 inside the first list of the outer matrix
print("\n", matrix2[0][1][0])

# more the number of dimensions more the number of [] to be used
# with every [] it starts accessing the inner list

# list methods

newlist = [1, 2, 3, 4, 5]
newlist.append(6)  # adds the given element to the end of the list
print("\n", newlist)
# counts the number of occurences of the given element in the list
print("\n", newlist.count(2))
newlist.pop()  # removes the last element from the list
print("\n", newlist)
newlist.pop(2)  # removes the third element from the list
print("\n", newlist)
newlist.reverse()  # reverses the list
print("\n", newlist)
