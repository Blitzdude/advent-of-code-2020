# https://adventofcode.com/2020/day/4

from libs.common import readPuzzleInputAsString, is_in_range

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
        missingFields = expectedFields.difference(id_fields)
        if (len(missingFields) == 0):
            valid_passports += 1
        elif (len(missingFields) == 1 and missingFields.pop() == "cid"):
            valid_passports += 1
    
    return valid_passports

def day4_part2(puzzleInput):
    valid_passports = list()
    expectedFields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"}


    # split passports from eachother
    passports = list(puzzleInput.split("\n\n"))
    # remove newlines from passport strings
    passports = list(map(lambda x: x.replace("\n", " "), passports))

    # find passports that all fields (except cid)
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
        missingFields = expectedFields.difference(id_fields)
        if (len(missingFields) == 0):
            valid_passports.append(passport_dict)
        elif (len(missingFields) == 1 and missingFields.pop() == "cid"):
            valid_passports.append(passport_dict)
    
    # check fields are valid (except cid)
    for valid_pass in valid_passports:
        pass_is_valid = True
        for field in valid_pass:
            pass_is_valid = doValidation(field, valid_pass[field])

def doValidation(field_type, value):
    validation_rules = {
        "byr": {"min": 1920, "max": 2002},
        "iyr": {"min": 2010, "max": 2020},
        "eyr": {"min": 2020, "max": 2030},
        "hgt": {"cm": {"min": 150, "max": 193}, "in": {"min":59, "max":76}},
        "hcl": {"length": 7},
        "ecl": {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"},
        "pid": {"length": 9}
        }

    field_is_valid = True
    
    if (field_type == "byr"):
        if (not is_in_range(value, validation_rules["byr"]["min"], validation_rules["byr"]["max"])):
            field_is_valid = False
    elif (field_type == "iyr"):
        if (not is_in_range(value, validation_rules["iyr"]["min"], validation_rules["iyr"]["max"])):
            field_is_valid = False
    elif (field_type == "eyr"):
        if (not is_in_range(value, validation_rules["eyr"]["min"], validation_rules["eyr"]["max"])):
            field_is_valid = False
    elif (field_type == "hgt"):
        field_is_valid = check_height(value, validation_rules["hgt"])
    elif (field_type =="hcl"):
        if (len(value) != validation_rules["hcl"]["length"]):
            field_is_valid = False
        if (value[0] != "#"):
            field_is_valid = False
    elif (field_type == "ecl"):
        if (value not in validation_rules["ecl"]):
            field_is_valid = False
    elif (field_type == "pid"):
        if (not value.isnumeric() and len(value) != validation_rules["pid"]["length"]):
            field_is_valid = False

    if (field_is_valid == False):
        print(field_type, value)
    return field_is_valid

def check_height(value, rule_dict):
        if (value.count("in") > 0):
            hgt_value = int(value.split("in")[0])
            if (not is_in_range(hgt_value, rule_dict["in"]["min"], rule_dict["in"]["max"])):
                return False
        elif (value.count("cm") > 0):
            hgt_value = int(value.split("cm")[0])
            if (not is_in_range(hgt_value, rule_dict["cm"]["min"], rule_dict["cm"]["max"])):
                return False
        else:
            return False

        return True

if __name__ == "__main__":
    # part1 = day4(readPuzzleInputAsString("puzzleInput/day4.txt"))
    # print(part1)
    day4_part2(readPuzzleInputAsString("puzzleInput/day4.txt"))