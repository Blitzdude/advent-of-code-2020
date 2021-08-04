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


        # find differing values in sets
        missingFields = expectedFields.difference(id_fields)
        if (len(missingFields) == 0):
            valid_passports += 1
        elif (len(missingFields) == 1 and missingFields.pop() == "cid"):
            valid_passports += 1
    
    return valid_passports

def day4_part2(puzzleInput):
    validator = Validator

    valid_passports = list()
    expectedFields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"}
    num_valid_passports = 0

    # split passports from eachother
    passports = list(puzzleInput.split("\n\n"))
    # remove newlines from passport strings
    passports = list(map(lambda x: x.replace("\n", " "), passports))

    # find passports that have all fields (except cid)
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
            pass_is_valid = validator.validateField(field, valid_pass[field])
        if pass_is_valid:
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
        else:
            return False

    def hasAllFields(self, passport):
        '''
        Validates that fields object has all the needed values

        passport (list): passport contains checkable fields
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

        return False

    def __validateBirthYear(self, value):
        if (is_in_range(value, self.validation_rules["byr"]["min"], self.validation_rules["byr"]["max"])):
            return True
        return False

    def __validateIssueYear(self, value):
        if (is_in_range(value, self.validation_rules["iyr"]["min"], self.validation_rules["iyr"]["max"])):
            return True
        return False

    def __validateExpirationYear(self, value):
        if (is_in_range(value, self.validation_rules["eyr"]["min"], self.validation_rules["eyr"]["max"])):
            return True
        return False

    def __validateHeight(self, value):
        return check_height(value, self.validation_rules["hgt"])

    def __validateHairColor(self, value):
        if (len(value) != self.validation_rules["hcl"]["length"]):
            return False
        if (value[0] != "#"):
            return False
        return True
        
    def __validateEyeColor(self, value):
        if (value not in self.validation_rules["ecl"]):
            return False
        return True

    def __validatePersonalId(self, value):
        if (value.isnumeric() and len(value) == self.validation_rules["pid"]["length"]):
            return True
        return False
    

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
    # part2 = day4_part2(readPuzzleInputAsString("puzzleInput/day4.txt"))
    # print(part2)
    validator = Validator()
    print(validator.hasAllFields(["pid:860033327", "eyr:2020", "hcl:#fffffd", "byr:1937", "iyr:2017", "hgt:183cm"]))

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