# https://adventofcode.com/2020/day/2

from libs.common import readPuzzleInput

def day2(puzzleInput):
    number_of_valid_passwords = 0
    for line in puzzleInput:
        limits, letter, password = line.split()
        min, max = limits.split("-")
        letter = letter.replace(":", "")

        count = password.count(letter)
        if (int(min) <= count and int(max) >= count):
            number_of_valid_passwords += 1

    return number_of_valid_passwords

def day2_part2(puzzleInput):
    number_of_valid_passwords = 0
    for line in puzzleInput:
        positions, letter, password = line.split()
        first, second = positions.split("-")
        idx1, idx2 = int(first)-1, int(second)-1
        letter = letter.replace(":", "")

        if (letter == password[idx1]):
            if (letter != password[idx2]):
                number_of_valid_passwords += 1
        elif (letter == password[idx2]):
            if (letter != password[idx1]):
                number_of_valid_passwords += 1

    return number_of_valid_passwords

if __name__ == "__main__":
    input = readPuzzleInput("puzzleInput/day2.txt")
    print(day2(input))
    print(day2_part2(input))