list1= ['newlist',1,3,5,5.432]
for index, item in enumerate(list1): #index should be before the item 
    print(index,item)
list2= ['newlist',1,3,5,5.432]
for item, index in enumerate(list1):  #else item is being printed first then index
    print("\n",index,item) 
#enumerate function adds a counter to any iterative element in this case is item

