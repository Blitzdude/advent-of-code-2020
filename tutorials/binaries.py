# https://pythonspot.com/binary-numbers-and-logical-operators/

# Binary numbers - second parameters tells python to use base 2
print(int("00", 2))
print(int("01", 2))
print(int("10", 2))
print(int("11", 2))

print(int("00000010", 2))
print(int("00000011", 2))
print(int("00000000", 2))
print(int("00001001", 2))
print(int("00010010", 2))
print(int("01000001", 2))
print(int("11111111", 2))

# logical operations
inputA = int('0101',2)

# shifting
print ("Before shifting " + str(inputA) + " " + bin(inputA))
print ("After shifting in binary: " + bin(inputA << 1))
print ("After shifting in decimal: " + str(inputA << 1))

# This code will execute a bitwise logical AND. Both inputA and inputB are bits.
inputA = 1
inputB = 1

print (inputA & inputB)   # Bitwise AND

# bitwise AND for secuence
inputA = int('00100011',2)   # define binary sequence inputA
inputB = int('00101101',2)   # define binary sequence inputB
print("AND")
print (bin(inputA & inputB))   # logical AND on inputA and inputB and output in binary

# bitwise OR for secuence
inputA = int('00100011',2)  # define binary number
inputB = int('00101101',2)  # define binary number

print("OR")
print (bin(inputA))            # prints inputA in binary
print (bin(inputB))            # prints inputB in binary
print (bin(inputA | inputB))   # Execute bitwise logical OR and print result in binary

# bitwise XOR for secuence
inputA = int('00100011',2)  # define binary number
inputB = int('00101101',2)  # define binary number

print("XOR")
print (bin(inputA))            # prints inputA in binary
print (bin(inputB))            # prints inputB in binary
print (bin(inputA ^ inputB))   # Execute bitwise logical OR and print result in binary