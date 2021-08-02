# https://adventofcode.com/2020/day/3

from libs.common import readPuzzleInput

def day3(puzzleInput):
    trees = checkSlope(puzzleInput, 3, 1)
    return trees

def day3_part2(puzzleInput):
    t1 = checkSlope(puzzleInput, 1, 1)
    t2 = checkSlope(puzzleInput, 3, 1)
    t3 = checkSlope(puzzleInput, 5, 1)
    t4 = checkSlope(puzzleInput, 7, 1)
    t5 = checkSlope(puzzleInput, 1, 2)
    print(t1, t2, t3, t4, t5)
    return t1 * t2 * t3 * t4 * t5

def checkSlope(input, stepX, stepY):
    x = 0
    trees = 0
    lineWidth = len(input[0])

    for i, line in enumerate(input):
        if (i != 0 and i % stepY == 0): 
            x = (x + stepX) % lineWidth 
            if (line[x] == "#"):
                trees += 1

    return trees

if __name__ == "__main__":
    input = readPuzzleInput("puzzleInput/day3.txt")
    print(day3(input))
    input = readPuzzleInput("puzzleInput/day3.txt")
    print(day3_part2(input))
