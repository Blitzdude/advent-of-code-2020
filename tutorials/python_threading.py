# https://pythonspot.com/threading/

from threading import *

# our thread class
class MyThread(Thread):

    def __init__(self,x):
        self.__x = x
        Thread.__init__(self)

    def run(self):
        print(str(self.__x))

def hello():
    print("Hello World after 5 seconds")

# Start 10 threads.
for x in range(10):
    MyThread(x).start()

# Timed threads

t = Timer(5.0, hello)

t.start()


