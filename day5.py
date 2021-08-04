# https://adventofcode.com/2020/day/5

from libs.common import readPuzzleInput

def day4(puzzleInput):
    print(puzzleInput)

def decodeSeatCode(code):
    if (type(code) != str):
        print("Error, code needs to be a string")
        return None
    if (len(code) != 10):
        print("Error, code needs to 10 characters long")
        return None

    # plane has rows 0 - 127 and columns 0 - 7
    

    

if __name__ == "__main__":
    day4(readPuzzleInput("puzzleInput/day5_test.txt"))