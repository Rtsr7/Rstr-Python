#write a program to print the list which contains the multiplication table of a user entered number

a= int(input("Enter a number: "))

list1= [a*i for i in range(1,20)]
print(list1)

#store the multiplication tables in file named tables.txt

with open("tables.txt","a") as tables:
    tables.write(str(list1)) #changing the list to a string to write that in tables.txt because .txt files doesnt support lists
    tables.write('\n') 