# https://adventofcode.com/2020/day/4

from os import replace
from libs.common import readPuzzleInputAsString

def day4(puzzleInput):
    expectedFields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"}
    passports = list(puzzleInput.split("\n\n"))
    passports = list(map(lambda x: x.replace("\n", " "), passports))

    for passport in passports:
        fields = passport.split()
        id_fields = []
        val_fields = []
        
        for field in fields:
            id, val = field.split(":")
            id_fields.append(id)
            val_fields.append(val)
        passport_dict = dict(zip(id_fields, val_fields))

        print(passport_dict)

if __name__ == "__main__":
    day4(readPuzzleInputAsString("puzzleInput/day4_test.txt"))
    pass