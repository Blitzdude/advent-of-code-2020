# https://pythonspot.com/write-file/

filename = "newfile.txt"

myfile = open(filename, "w")

myfile.write("Written with python\n")

myfile.close()

myfile = open(filename, "a")

myfile.write("Appended with python\n")

myfile.close()