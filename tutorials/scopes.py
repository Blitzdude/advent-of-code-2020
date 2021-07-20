# https://pythonspot.com/global-local-variables/

z = 10 # global variable

def sum(x,y):
    sum = x + y # x and y are local
    return sum

print(sum(8,9))

# this will not work
# print(x)

def aFunction():
    global z
    print(z)
    z = 9 # changes the global variable

aFunction()
print(z)

z = 10

def func1():
    global z
    z = 3

def func2(x,y):
    global z
    return x+y+z

func1()
total = func2(4,5)
print(total)