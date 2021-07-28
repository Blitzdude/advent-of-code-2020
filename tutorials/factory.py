# https://pythonspot.com/factory-method/

class Car(object):

    def factory(type):
        if type == "Racecar":
            return Racecar()
        if type == "Van":
            return Van()

    factory = staticmethod(factory)

class Racecar(Car):
    def drive(self):
        print("Racecar driving. Much speed...")

class Van(Car):
    def drive(self):
        print("Van driving. Horn goes 'Meep Meep!'")

# Create object using factory
obj = Car.factory("Racecar")
obj.drive()

vanObj = Car.factory("Van")
vanObj.drive()