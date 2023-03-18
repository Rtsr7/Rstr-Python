def add(a,b):
    return a+b
if __name__=='__main__': #this line means that the code within it will only be executed if this file is run 
#if this file is imported somewhere then the code below will not run because of the if condition
#main means the current file is run when we are in the file
    print("This line will only be executed when file is opened in main")
    print("If the file is imported these two lines will not be executed")