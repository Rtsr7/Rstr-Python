# Creating a dictionary
# dictionary= {
#     'key':"value",
#     'key':"value",
#     'key':"value",
#     'key':"value"
# }

dict1={
    "word":"meaning",
    "word2":"meaning2"
}
print(dict1)

dict2={
    "num1" : 1,
    "num2" : 2,
    "num3" : 3,
    "num4" : 4,
    "num5" : 5,
}
print(dict2)

#Creating a dictionary with the dict function
dict3= dict(car1="expensive",car2="more expensive", car3="even more expensive")
print(dict3)

#Accessing values from keys
print(dict3["car1"]) 

#Accessing keys from values
# print(dict2(2))

#adding new elements to a dictionary
newdict={
    "name":"Restart",
    "age":20,
    "performance":"Excellent"
}
print(newdict)

newdict["coding"]="40 hours"
print(newdict)

#Changing elements 
newdict["age"]=25
print(newdict)

#Removing elements
del newdict["coding"]
print(newdict)

#Another way to delete
newdict.pop("age")
print(newdict)

#Removest the last element
newdict.popitem()
print(newdict)

#Every operation is done on keys and the value automatically follows the operations


#Looping through dictionaries

for item in dict2:
    print(item) #prints the keys
for item in dict2.values():
    print(item) #prints the values
for this in dict2.items():
    print(this) #prints both the keys and the values
#Another way of printing the item
for key,value in dict2.items():
    print(key,value)


#Turning a dictionary into a copy of another dictionary
dict4= {
    "key":1,
    "key2":2,
    "key3":3,
    "key4":4,
    "key5":5
}

dict5=dict(name=1,age=2)
print(dict4)
print(dict5)
dict4.update(dict5)
print(dict4)

#Dictionary methods

newdict={
    "name":"Restart",
    "age":20,
    "coding":100.5,
    "performance":"Excellent"
}

newcopy= newdict.copy() #copies the given dictionary and assigns it to another dictionary
print(newcopy)

new1=newdict.fromkeys(newdict) #Creates a newdictionary with the keys of the given dicitonary
print(new1)

print(newdict.get("coding")) #gets the value at the key

print(newdict.items()) #prints everything in new dict
print(newdict.keys() )#prints keys in new dict

print(newdict.values()) # prints the values in new dict

# newdict.clear() #clears the whole dictionary
# print(newdict)


