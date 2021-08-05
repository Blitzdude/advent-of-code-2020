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
        print(answer_set)
        num_answers += len(answer_set)

    return num_answers

def day6_part2(puzzleInput):
    # each group contains x number of people with answers
    # count how many questions in a group was answered by ALL members

    # split groups from each other
    groups = list(puzzleInput.split("\n\n"))
    # remove newlines from passport strings
    num_answers = 0
    for idx, group_answers in enumerate(groups):
        # group answers join them together as string
        print("Group: " + " " + str(idx+1))
        answers_list = group_answers.split("\n")
        print(answers_list)

    return num_answers

if __name__ == "__main__":
    result = day6_part2(readPuzzleInputAsString("puzzleInput/day6_test.txt"))
    print(result)