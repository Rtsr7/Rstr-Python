
objects = open("file.txt", "r")
# r stands for read
'''
the open method is used to open the file
if the file is not in the directory it will give error
'''
objects.read()
'''
the objects.read() and objects.readline() are just various methods after opening a file
'''
objects.readline()
objects.close()
'''
every file should be closed after opening with the .close() method
'''

# opening with 'with' statement

with open("file.txt", "r") as withmethodopening:
    print(withmethodopening.readline())  # prints first line
    print(withmethodopening.readline())  # prints second line
    print(withmethodopening.readline())  # prints third line
    print(withmethodopening.readline())  # prints fourth line
    print(withmethodopening.readline())  # prints fifth line
    print(withmethodopening.readlines())  # prints all the lines in the file

'''since all the lines has already been read by the .readline() method above the .readlines() method shows null list'''
withmethodopening.close()  # closes the file This step is very important

with open("file.txt", "r") as newmethod:
    print(newmethod.readlines())  # prints all the lines in the file


# using the for loop to read the lines in the file

with open("file.txt", "r") as newfile:
    for lines in newfile:
        print(lines)
    '''
    this for loop runs for all the lines until the end of the file

    the for lines can also be written as 
    for anything in newfile:
       print(anything)

    this will also work its just a way of iterating over all the lines 
    '''

    # returning a dictionary with the lines in file.txt


emptydict = {}
with open("file.txt", "r") as dictfile:
    for line in dictfile:
        separation = line.split(" ")
        if len(separation) == 2:
            emptydict[separation[0]] = separation[1]
print(emptydict)


newdict={}
with open("file.txt","r") as filenew:
    for chars in filenew:
         newdict.update(chars)
print(newdict)