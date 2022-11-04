# adventOfCode 20xy day 9
# https://adventofcode.com/20xy/day/9


def perform_cancels(in_string):
    # Handle canceled characters 
    # Within garbage any character after ! is ignored.
    # This will implemented by removing the ! and its subsequent character
    string_i = -1
    while True:
        string_i = in_string.find('<', string_i + 1)
        if string_i == -1:
            break
        while True:
            if in_string[string_i] in ['>', '!']:
                if in_string[string_i] == '>':
                    break
                # Remove two chars
                in_string = in_string[0:string_i] + in_string[string_i + 2:]
                string_i -= 1
            string_i += 1

    return in_string

def get_score(in_string):
    in_string = perform_cancels(in_string)

    return 42

# Reading input from the input file
input_filename='input_sample0.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        print(f'Input:  {in_string}')
        print(f'Result: {get_score(in_string)}\n')
print()


def test_cancel():
    assert perform_cancels('<{!>}>') == '<{}>'
    assert perform_cancels('<!!>') == '<>'
    assert perform_cancels('<!!!>>') == '<>'
    assert perform_cancels('<{o"i!a,<{i<a>') == '<{o"i,<{i<a>'

