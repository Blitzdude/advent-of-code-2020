# https://pythonspot.com/python-lambda/

from functools import reduce

f_double = lambda x : 2 * x
print(f_double(3))

check_true = lambda x : x > 10
print(check_true(4))
print(check_true(69))

# Map function
mylist = [1,2,3,4,5]
squaredList = list(map(lambda x: x*x, mylist))
print(squaredList)

# Filter function
unfilteredList = [1,2,3,4,5,6,7,8,9,10]
filteredList = list(filter(lambda x: x % 2 == 0, unfilteredList))
print(filteredList)

# Reduce function
firstList = [1,2,3,4,5]
s = reduce(lambda x,y: x+y, firstList)
print(s)

anotherList = [10,6,7,5,2,1,8,5]
reducedList = reduce(lambda x,y: x if (x > y) else y, anotherList)
print(reducedList)
