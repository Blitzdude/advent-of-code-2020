# https://adventofcode.com/2020/day/3

def day3(puzzleInput):
    x = 0
    trees = 0
    lineWidth = len(puzzleInput[0])

    for line in puzzleInput[1:]: # ignore the first element
        x = (x+3) % lineWidth
        if (line[x] == "#"):
            trees += 1

    return trees


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
    trees = day3(input)
    print(trees)
