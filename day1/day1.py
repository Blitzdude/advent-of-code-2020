
'''
--- Day 1: Report Repair ---
After saving Christmas five years in a row, you've decided to take a vacation at a nice resort on a tropical island.
Surely, Christmas will go on without you.

The tropical island has its own currency and is entirely cash-only.
The gold coins used there have a little picture of a starfish; the locals just call them stars.
None of the currency exchanges seem to have heard of them, but somehow, you'll need to find fifty of these coins by the time
you arrive so you can pay the deposit on your room.

To save your vacation, you need to get all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; 
the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input); 
apparently, something isn't quite adding up.

Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.

For example, suppose your expense report contained the following:

1721
979
366
299
675
1456

In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, 
so the correct answer is 514579.

Of course, your expense report is much larger. Find the two entries that sum to 2020; what do you get if you multiply them together?

Your puzzle answer was 842016.
'''
import sys

def day1(puzzleInput):
    if (puzzleInput == None):
        print("Error puzzle input cannot be None")
    else: 
        
        # convert to int
        puzzleInput = list(map(int, puzzleInput))
        
        num1 = 0
        num2 = 0
        for element in puzzleInput:
            to_find = 2020 - element
            if (to_find in puzzleInput):
                num1, num2 = element, to_find

        return num1 * num2

def day2(puzzleInput):
    if (puzzleInput == None):
        print("Error puzzle input cannot be None")
    else: 
        # convert to int
        puzzleInput = list(map(int, puzzleInput))
        
        # same as above, but need to find 3 elements that add to 2020
        num1 = 0
        num2 = 0
        num3 = 0
        for ix, x in enumerate(puzzleInput):
            for  y in (puzzleInput[ix:]):
                for z in (puzzleInput[ix+1:]):
                    if (x + y + z == 2020):
                        num1, num2, num3 = x, y, z
                        break

        return num1 * num2 * num3

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
    puzzleInput = readPuzzleInput(sys.argv[1])
    day1_result = day1(puzzleInput)
    print("day1: " + str(day1_result))
    day2_result = day2(puzzleInput)
    print("day2: " + str(day2_result))