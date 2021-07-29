# https://pythonspot.com/threading/

from threading import *
import time

def handleClient1():
    while(True):
        print("Waiting for client 1...")
        time.sleep(5)

def handleClient2():
    while(True):
        print("Waiting for client 2...")
        time.sleep(5)

# create threads
t1 = Timer(5.0, handleClient1)
t2 = Timer(3.0, handleClient2)

# start threads
t1.start()
t2.start()