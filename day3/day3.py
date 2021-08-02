# https://adventofcode.com/2020/day/3

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

def replace_char_at_index(org_str, index, replacement):
    ''' Replace character at index in string org_str with the
    given replacement character.'''
    new_str = org_str
    if index < len(org_str):
        new_str = org_str[0:index] + replacement + org_str[index + 1:]
    return new_str

def readPuzzleInput(filepath):
    puzzleInput = []
    try:
        with open(filepath, "r") as file:
            lines = file.readlines()
            puzzleInput = list(map(lambda x : x.replace("\n", ""), lines))
    except FileNotFoundError:
        print("Error: File not found")
        puzzleInput = None

    return(puzzleInput)


if __name__ == "__main__":
    input = readPuzzleInput("day3/puzzleInput.txt")
    print(day3(input))
    input = readPuzzleInput("day3/puzzleInput.txt")
    print(day3_part2(input))
