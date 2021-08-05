# https://adventofcode.com/2020/day/5

from libs.common import readPuzzleInput

def day4(puzzleInput):
    print(puzzleInput)
    seat_codes = list()
    for line in puzzleInput:
        seat_codes.append(decodeSeatCode(line))

    sorted_seats = sorted(seat_codes)
    highest_seat_code = sorted_seats.pop()
    print(highest_seat_code)

def decodeSeatCode(code):
    if (type(code) != str):
        print("Error, code needs to be a string")
        return None
    if (len(code) != 10):
        print("Error, code needs to 10 characters long")
        return None

    # plane has rows 0 - 127 and columns 0 - 7
    row_min, row_max = 0, 127
    col_min, col_max = 0, 7
    for c in code:
        if (c == "B"):
            row_min += int((row_max - row_min) / 2) + 1
        elif (c == "F"):
            row_max -= int((row_max - row_min) / 2) + 1
        elif (c == "R"):
            col_min += int((col_max - col_min) / 2) + 1
        elif (c == "L"):
            col_max -= int((col_max - col_min) / 2) + 1
        
    seat_code = row_min * 8 + col_min
    return seat_code


    

if __name__ == "__main__":
    day4(readPuzzleInput("puzzleInput/day5_test.txt"))