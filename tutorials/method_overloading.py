# https://pythonspot.com/method-overloading/

class Human:

    def sayHello(self, name=None):

        if name is not None:
            print("Hello " + name)
        else:
            print("Hello ")

# Create instance
ted = Human()

# Call the method
ted.sayHello()

# Call the method with a parameter
ted.sayHello("Guido")