# https://pythonspot.com/read-file/
import os.path

filename = "bestand.txt"

if not os.path.isfile(filename):
    print("File does not exist")
else:
    with open(filename) as file:
        contents = file.read().splitlines()
        # contents = file.readlines()

for line in contents:
    print(line)

# socratica
try:
    with open(filename) as fileobj:
        text = fileobj.read()
except FileNotFoundError:
    text = None

print(contents)