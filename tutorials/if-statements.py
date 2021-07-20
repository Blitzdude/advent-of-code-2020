# https://pythonspot.com/if-statements/

x = 3
if x > 10:
    print("x smaller than 10")
else:
    print("x is bigger than 10 or equal")

# a little game

age = 24

print("Guess my age, you have 1 Chance")
guess = int(input("Guess: "))

if guess != age:
    print("Wrong!")
else:
    print("Correct")

# Nesting

a = 12
b = 33
# bad
if a > 10:
    if b < 20:
        print("Good")

# better
    if a > 10 and b < 20:
        print("In Range")
    else:
        print("Out of range")
