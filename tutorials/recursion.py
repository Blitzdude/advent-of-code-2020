# https://pythonspot.com/recursion/
import sys

sys.setrecursionlimit(5000)


def sum(list):
    sum = 0

    # add every number in the list.
    for i in range(0, len(list)):
        sum = sum + list[i]

    # Return the sum
    return sum

def sum_recursive(list):
    if len(list) == 1:
        return list[0]
    else:
        return list[0] + sum(list[1:])

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(sum([5,7,3,4,10]))
print(sum_recursive([5,9,3,2,10]))
print(factorial(300))