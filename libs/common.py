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

def readPuzzleInputAsString(filepath):
    puzzleInput = ""
    try:
        with open(filepath, "r") as file:
            puzzleInput = file.read()
    except FileNotFoundError:
        print("Error: File not found")
        puzzleInput = None

    return(puzzleInput)

def replaceCharAtIndex(orgStr, index, replacement):
    ''' Replace character at index in string org_str with the
    given replacement character.'''
    newStr = orgStr
    if index < len(orgStr):
        newStr = orgStr[0:index] + replacement + orgStr[index + 1:]
    return newStr