# https://adventofcode.com/2020/day/4

from libs.common import readPuzzleInputAsString, is_in_range

def day4(puzzleInput):
    validator = Validator()
    valid_passports = 0

    # split passports from eachother
    passports = list(puzzleInput.split("\n\n"))
    # remove newlines from passport strings
    passports = list(map(lambda x: x.replace("\n", " "), passports))

    for passport in passports:
        passport = passport.split()
        if (validator.hasAllFields(passport)):
            valid_passports += 1

    return valid_passports

def day4_part2(puzzleInput):
    validator = Validator()

    num_valid_passports = 0

    # split passports from eachother
    passports = list(puzzleInput.split("\n\n"))
    # remove newlines from passport strings
    passports = list(map(lambda x: x.replace("\n", " "), passports))

    for passport in passports:
        passport = passport.split()
        pp_is_valid = validator.validatePassport(passport)
        if (pp_is_valid):
            num_valid_passports += 1

    return num_valid_passports

class Validator:
    expectedFields = set()
    validation_rules = dict()

    def __init__(self):
        self.expectedFields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"}
        
        self.validation_rules = {
            "byr": {"min": 1920, "max": 2002},
            "iyr": {"min": 2010, "max": 2020},
            "eyr": {"min": 2020, "max": 2030},
            "hgt": {"cm": {"min": 150, "max": 193}, "in": {"min":59, "max":76}},
            "hcl": {"length": 7},
            "ecl": {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"},
            "pid": {"length": 9}
            }

    def hasAllFields(self, passport):
        '''
        Validates that fields object has all the needed values

        passport (list): passport contains checkable fields

        Returns True, if passport has all fields
        '''

        id_fields = set()
        
        for field in passport:
            id = field.split(":")[0]
            id_fields.add(id)

        # find differing values in sets
        missingFields = self.expectedFields.difference(id_fields)
        if (len(missingFields) == 0):
            return True
        elif (len(missingFields) == 1 and missingFields.pop() == "cid"):
            return True
        else:
            return False

    def validatePassport(self, passport):
        if (self.hasAllFields(passport) == False):
            return False
        for field in passport:
            field_type, value = field.split(":")
            field_is_valid = self.validateField(field_type, value)
            if (field_is_valid == False):
                return False
        return True

    def validateField(self, field, value):
        if field == "byr":
            return self.__validateBirthYear(value)
        elif field == "iyr":
            return self.__validateIssueYear(value)
        elif field == "eyr":
            return self.__validateExpirationYear(value)
        elif field == "hgt":
            return self.__validateHeight(value)
        elif field == "hcl":
            return self.__validateHairColor(value)
        elif field == "ecl":
            return self.__validateEyeColor(value)
        elif field == "pid":
            return self.__validatePersonalId(value)
        elif field == "cid":
            return True
        else:
            return False

    def __validateBirthYear(self, value):
        if (is_in_range(int(value), self.validation_rules["byr"]["min"], self.validation_rules["byr"]["max"])):
            return True
        return False

    def __validateIssueYear(self, value):
        if (is_in_range(int(value), self.validation_rules["iyr"]["min"], self.validation_rules["iyr"]["max"])):
            return True
        return False

    def __validateExpirationYear(self, value):
        if (is_in_range(int(value), self.validation_rules["eyr"]["min"], self.validation_rules["eyr"]["max"])):
            return True
        return False

    def __validateHeight(self, value):
        return self.__check_height(value, self.validation_rules["hgt"])

    def __validateHairColor(self, value):
        if (len(value) != self.validation_rules["hcl"]["length"]):
            return False
        if (value[0] != "#"):
            return False
        return True
        
    def __validateEyeColor(self, value):
        if (value in self.validation_rules["ecl"]):
            return True
        return False

    def __validatePersonalId(self, value):
        if (value.isnumeric() and len(value) == self.validation_rules["pid"]["length"]):
            return True
        return False
    
    def __check_height(self, value, rule_dict):
        if (value.count("in") > 0):
            hgt_value = int(value.split("in")[0])
            if (is_in_range(hgt_value, rule_dict["in"]["min"], rule_dict["in"]["max"])):
                return True
        elif (value.count("cm") > 0):
            hgt_value = int(value.split("cm")[0])
            if (is_in_range(hgt_value, rule_dict["cm"]["min"], rule_dict["cm"]["max"])):
                return True
        else:
            return False

        return False

if __name__ == "__main__":
    part1 = day4(readPuzzleInputAsString("puzzleInput/day4_test.txt"))
    print(part1)
    part2 = day4_part2(readPuzzleInputAsString("puzzleInput/day4_test.txt"))
    print(part2)
    # validator = Validator()
    # print(validator.hasAllFields(["pid:860033327", "eyr:2020", "hcl:#fffffd", "byr:1937", "iyr:2017", "hgt:183cm"]))

    # # valid
    # print(validator.validateField("byr", 2002))
    # print(validator.validateField("hgt", "60in"))
    # print(validator.validateField("iyr", 2020))
    # print(validator.validateField("eyr", 2030))
    # print(validator.validateField("hcl", "#123abc"))
    # print(validator.validateField("ecl", "brn"))
    # print(validator.validateField("pid", "000000001"))

    # # invalid
    # print(validator.validateField("byr", 2003))
    # print(validator.validateField("hgt", "194in"))
    # print(validator.validateField("iyr", 2021))
    # print(validator.validateField("eyr", 2031))
    # print(validator.validateField("hcl", "123abc"))
    # print(validator.validateField("ecl", "asd"))
    # print(validator.validateField("pid", "0123456789"))