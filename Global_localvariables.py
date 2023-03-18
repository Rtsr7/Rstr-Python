a= 5 #global variable can we used anywhere in the program

def newfunction(a):

    a= 10 #local variable can be used only within the function or area in which it is defined
    print(a)
newfunction(a)
print(a)
def function2(b):
    b=6
    global a #taking the global variable
    a=2 #changing the global variable
    print(a) 
function2(a)
