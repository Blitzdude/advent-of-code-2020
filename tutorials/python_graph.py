# https://pythonspot.com/python-graph/

# Python does not have its own graph module. we can implement one ourselves
# definition
graph = {"A": ["B", "C"],
         "B": ["C", "A"],
         "C": ["D"],
         "D": ["A"]}

print(graph)

# NetworkX is not available in python 3