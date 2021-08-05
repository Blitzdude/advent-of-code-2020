# https://adventofcode.com/2020/day/5

from libs.common import readPuzzleInput

def day4(puzzleInput):
    seat_codes = list()
    for line in puzzleInput:
        seat_codes.append(decodeSeatBinary(line))

    sorted_seats = sorted(seat_codes)
    highest_seat_code = sorted_seats.pop()
    return highest_seat_code

def day4_part2(puzzleInput):
    # to find our seat we need to go through all possible seat position codes and
    # find one, that cannot be found in the puzzle input.
    # When we find a seat not in the puzzle input, we check seat codes +1 and -1 also exist.

    # starting x = 1, because we ignore first row
    # terminating condition x < 127, because we ignore the last row
    x, y = 1, 0
    while (x < 127):
        seat_bin_to_check = coordToSeatBiniary(x, y)
        if (seat_bin_to_check not in puzzleInput):
            # found seat not in puzzleinput
            seat_code_to_check = decodeSeatBinary(seat_bin_to_check)

            # check that seat codes +1 and -1 are on the list
            nxt_seat_code = seat_code_to_check + 1
            prv_seat_code = seat_code_to_check - 1
            nxt_seat_bin = encodeSeatCodeToSeatBinary(nxt_seat_code)
            prv_seat_bin = encodeSeatCodeToSeatBinary(prv_seat_code)

            if (nxt_seat_bin in puzzleInput and prv_seat_bin in puzzleInput):
                # next and previous are on the list, so we have found our seat
                return seat_code_to_check
        
        # Update the loop
        y += 1
        if (y >= 8):
            y = 0
            x += 1
        
    return None


def decodeSeatBinary(code):
    '''
    Takes a seat binary code and returns the corresponding seat_cod

    code: string with length 10. Example "FBFBBFBRLL"

    return: seat code as an int
    '''
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

def encodeSeatCodeToSeatBinary(seat):
    '''
    takes a integer seat code and returns the corresponding seat binary

    seat: int number value of the seat code

    return: string; seat binary string of length 10. Example "FBFBBFBRLL
    '''
    row, col = int(seat / 8), seat % 8
    return coordToSeatBiniary(row, col)
    

def coordToSeatBiniary(row, col):
    '''
    turns row and column coordinates between 0-127 and 0-7 to seat binary code

    row : int - row number between 0 - 127
    col : int - col number between 0 - 7

    return : string - seat binary as string length 10
    '''
     # use F-string to represent coordinates as binary
    row_string = f'{row:07b}'
    col_string = f'{col:03b}'

    # format each string as characters
    row_string = row_string.replace("0", "F")
    row_string = row_string.replace("1", "B")
    col_string = col_string.replace("0", "L")
    col_string = col_string.replace("1", "R")
    
    seat_code = row_string + col_string
    return seat_code

if __name__ == "__main__":
    print(day4(readPuzzleInput("puzzleInput/day5.txt")))
    print(day4_part2(readPuzzleInput("puzzleInput/day5.txt")))