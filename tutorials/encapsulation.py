# https://pythonspot.com/encapsulation/

class Car:

    __maxspeed = 0
    __name = ""

    def __init__(self):
        self.__maxspeed = 200
        self.__name = "Supercar"
        self.__updateSoftware()

    def drive(self):
        print("driving. maxspeed " + str(self.__maxspeed))
    
    def setMaxSpeed(self,speed):
        self.__maxspeed = speed

    def __updateSoftware(self):
        print("updating software")

redcar = Car()
redcar.drive()
redcar.__maxspeed = 10 # will not change variable because its private
redcar.drive()
redcar.setMaxSpeed(320)
redcar.drive()
# redcar.__updateSoftware() Will not run