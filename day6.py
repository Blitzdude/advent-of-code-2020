# https://adventofcode.com/2020/day/6

from libs.common import readPuzzleInputAsString

def day6(puzzleInput):

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

if __name__ == "__main__":
    result = day6(readPuzzleInputAsString("puzzleInput/day6.txt"))
    print(result)
    pass