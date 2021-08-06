# https://adventofcode.com/2020/day/7
from libs.common import readPuzzleInput

def day7(puzzleInput):
    rules = list()
    for line in puzzleInput:
        new_rule = Rule(line)
        rules.append(new_rule)
    
    for rule in rules:
        print(rule.get_name(), rule.get_bags())

    # format of line is: 
    # color bags contain X color bag <repeat N> , Y color bags

class Rule:

    def __init__(self, rule_string) -> None:
        self.name = ""
        self.bags_contained = []
        self.__splitRuleString(rule_string)

    def __splitRuleString(self, rule_string):
        rule_name, contains_strings = str(rule_string).split("contain ", maxsplit=1)
        self.set_name(rule_name)
        
        bag_rules = contains_strings.split(", ")
        for bag_rule in bag_rules:
            if (bag_rule.count("no other bags.") == 0):
                self.add_bag(list(bag_rule.split(" ", maxsplit=1)))

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_bags(self):
        return self.bags_contained

    def add_bag(self, bag):
        self.bags_contained.append(bag)


class Bag(object):
    # works like binary tree https://pythonspot.com/python-tree/
    def __init__(self):
        self.left = None
        self.right = None

if __name__ == "__main__":
    day7(readPuzzleInput("puzzleInput/day7_test.txt"))
    pass