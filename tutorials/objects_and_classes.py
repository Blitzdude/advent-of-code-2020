# https://pythonspot.com/objects-and-classes/

class User:
    name = ""

    def __init__(self, name):
        self.name = name

    def sayHello(self):
        print("Hello, my name is " + self.name)

# create object
james = User("James")
david = User("David")
eric = User("Eric")

james.sayHello()
eric.sayHello()

# Coffee machine
class CoffeeMachine:
    name = ""
    beans = 0
    water = 0

    def __init__(self, name, beans, water) -> None:
        self.name = name
        self.beans = beans
        self.water = water

    def addBean(self):
        self.beans = self.beans + 1
        
    def removeBean(self):
        self.beans = self.beans - 1

    def addWater(self):
        self.water = self.water + 1
        
    def addWater(self):
        self.water = self.water - 1

    def printState(self):
        print("Name = " + self.name)
        print("Beans = " + str(self.beans))
        print("Water = " + str(self.water))

pythonBean = CoffeeMachine("Python Bean", 83, 20)
pythonBean.printState()
print("")
pythonBean.addBean()
pythonBean.printState()