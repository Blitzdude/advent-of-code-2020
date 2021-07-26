# https://pythonspot.com/python-class/

class Animal:
    def __init__(self,name) -> None:
        self.name = name

    def walk(self):
        print(self.name + " Walks.")

duck = Animal("Duck")
duck.walk()

rhino = Animal("African Rhino")
rhino.walk()