# adventOfCode 2017 day 04
# https://adventofcode.com/2017/day/4


def is_valid(in_string):
    word_series = set()
    for word in in_string.split(' '):
        if word in word_series:
            return False
        word_series.add(word)
    return True

valid_count = 0

# Reading input from the input file
input_filename='input_sample0.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        if is_valid(in_string):
            valid_count += 1
print(f'The count of valid passphrases is {valid_count}\n')


