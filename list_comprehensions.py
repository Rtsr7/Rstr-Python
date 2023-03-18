
#print all even numbers from the list
list1=[5.6,100,2,3,4,5,6,7,8,9,10]
b=[]
for item in list1:
    if item%2==0:
        b.append(item)
print(b)

#new method
c=[item for item in list1 if item%2==0] #this line means return item after looping through all the items in list if the item is divisible by 2 which means its even
print(c)