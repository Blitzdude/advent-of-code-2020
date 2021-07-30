# https://pythonspot.com/python-set/

exampleSet = set(["Postcard", "Radio", "Telegram"])
print(exampleSet)

# Sets cannot contains multiples. Any doubles are removed
exampleSet = set(["Postcard", "Radio", "Telegram", "Postcard"])
print(exampleSet)

# Above is old notation, Use simple notation in python 3

simpleSet = {"Postcard", "Radio", "Telegram"}
print(simpleSet)

# set.clear() removes all elements from set
emptySet = {"Postcard", "Radio", "Telegram"}
emptySet.clear()
print(emptySet)

# set.remove(var) removes specified elements
removedSet = {"Postcard", "Radio", "Telegram"}
removedSet.remove("Postcard")
print(removedSet)

# set.difference(other) compares set with another and returns set with differing values
xSet = {"Postcard", "Radio", "Telegram" }
ySet = {"Radio"}
print("xset " + str(xSet.difference(ySet)))
print("ySet " + str(ySet.difference(xSet)))

# Subset - set.issubset(other) tests if values in "set" are contained in "other"
xSuperSet = {"a","b","c","d"}
ySubSet = {"c","d"}
print("Subsets")
print(xSuperSet.issubset(ySubSet))
print(ySubSet.issubset(xSuperSet))

# Superset - set.issuperset(other) tests if values in "other" are contained in "set"
print("Superset")
xSuperSet = {"a","b","c","d"}
ySubSet = {"c","d"}
print(xSuperSet.issuperset(ySubSet))
print(ySubSet.issuperset(xSuperSet))

# Intersection - set.intersection(other) returns all variables in both sets
xIntersect = {"a","b","c","d","e"}
yIntersect = {"c","d"}
print( xIntersect.intersection(yIntersect))

