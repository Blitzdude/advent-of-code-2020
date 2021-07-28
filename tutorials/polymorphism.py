# https://pythonspot.com/polymorphism/
from abc import ABC, abstractmethod

# Polymorphism with functions
class Bear(object):
    def sound(self):
        print("Groarrr")

class Dog(object):
    def sound(self):
        print("Woof woof!")

# function takes an animal object
def makeSound(animalType):
    animalType.sound()

bearObj = Bear()
dogObj = Dog()

makeSound(bearObj)
makeSound(dogObj)

# Polymorphism with abstract class
# Python 3.9 does not provide abstract base classes by default. 
# We need to import a module to do that

class Document(ABC):
    name = ""
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def show(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Pdf(Document):

    def show(self):
        return "Show pdf contents!"

class Word(Document):

    def show(self):
        return "Show word contents!"


documents = [Pdf("Document1"), Pdf("Document2"), Word("Document3")]

for doc in documents:
    print(doc.name + ": " + doc.show())