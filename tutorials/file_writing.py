# https://pythonspot.com/write-file/

# filename = "newfile.txt"

# myfile = open(filename, "w")

# myfile.write("Written with python\n")

# myfile.close()

# myfile = open(filename, "a")

# myfile.write("Appended with python\n")

# myfile.close()

# socratica
oceans = ["Pacific", "Atlantic", "Indian", "Southern", "Arctic"]

with open("oceans.txt", "w") as f:
    for ocean in oceans:
        f.write(ocean)
        f.write("\n")
        # same can be done with print:
        # print(ocean, file=f)

# append mode
with open("oceans.txt", "a") as f:
    print(23*"=", file=f)
    print("These are the 5 oceans.", file=f)

