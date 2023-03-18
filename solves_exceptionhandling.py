#write a program to open three files. If any of these files are not present a message without exiting the program must be printed prompting the same

def fileopen(nameoffile):
    try:
        with open (nameoffile , "r") as files:
            print(files.read())
    except FileNotFoundError:
        print(f"{nameoffile} not found")
fileopen("file1.txt")
fileopen("file2.txt")
fileopen("file3.txt")
fileopen("error.txt")


#write a program to display a/b. If b=a display infinite by handling the ZeroDivisionError

a= int(input("Enter a number: "))
b= int(input("Enter a number: "))
try:
    print(a/b)
except ZeroDivisionError:
    print("Infinite")    