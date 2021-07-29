# https://pythonspot.com/logging/
import logging

# write a file for logging purposes
logging.basicConfig(filename="program.log", format="%(asctime)s %(message)s", level=logging.DEBUG)

# print a log message to the console
logging.warning("This is a warning!")
logging.warning("An example message")
logging.warning("Another message")

