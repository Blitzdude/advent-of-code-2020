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
