# https://adventofcode.com/2020/day/6

from libs.common import readPuzzleInputAsString

def day6(puzzleInput):
    # each group contains x number of people with answers
    # count how many unique answers are in group and sum them up

    # split groups from each other
    groups = list(puzzleInput.split("\n\n"))
    # remove newlines from passport strings
    num_answers = 0
    for group_answers in groups:
        # remove newlines from group answers and join them together as string
        answer_str = "".join(map(str, list(group_answers.split("\n"))))
        
        # convert string to set all element in set are unique
        answer_set = set(answer_str)
        num_answers += len(answer_set)

    return num_answers

def day6_part2(puzzleInput):
    # each group contains x number of people with answers
    # for each group, count how many questions ALL people answered "yes" to.

    # split groups from each other
    groups = list(puzzleInput.split("\n\n"))

    # in each group, split persons from each other
    sorted_groups = list()
    for group in groups:
        sorted_groups.append(group.split("\n"))

    # sort each answer group by length
    for idx, ag in enumerate(sorted_groups):
        sorted_groups[idx] = sorted(ag, key=len, reverse=True)

    # each persons answers are split by char into set
    for group in sorted_groups:
        for idx, person in enumerate(group):
            group[idx] = set(answer for answer in person)
            pass

    result = 0

    for group in sorted_groups:
        # for each group, get intersections of each persons answer sets to find the amount of answers everyone answered yes to
        answer_set = group[0] # first one should be the longest, because we sorted them in reverse
        for person in group:
            answer_set = answer_set.intersection(person)

        result += len(answer_set)

    return result


if __name__ == "__main__":
    result = day6(readPuzzleInputAsString("puzzleInput/day6.txt"))
    print(result)
    result = day6_part2(readPuzzleInputAsString("puzzleInput/day6.txt"))
    print(result)