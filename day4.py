# https://adventofcode.com/2020/day/4

from os import replace
from libs.common import readPuzzleInputAsString

def day4(puzzleInput):
    valid_passports = 0
    expectedFields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"}

    # split passports from eachother
    passports = list(puzzleInput.split("\n\n"))
    # remove newlines from passport strings
    passports = list(map(lambda x: x.replace("\n", " "), passports))

    for passport in passports:
        fields = passport.split()
        id_fields = set()
        val_fields = list()
        
        for field in fields:
            id, val = field.split(":")
            id_fields.add(id)
            val_fields.append(val)

        passport_dict = dict(zip(id_fields, val_fields))

        # find differing values in sets
        print(passport_dict)
        missingFields = expectedFields.difference(id_fields)
        if (len(missingFields) == 0):
            valid_passports += 1
        elif (len(missingFields) == 1 and missingFields.pop() == "cid"):
            valid_passports += 1
    
    return valid_passports

if __name__ == "__main__":
    part1 = day4(readPuzzleInputAsString("puzzleInput/day4.txt"))
    print(part1)
    pass