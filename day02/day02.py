# adventOfCode 2017 day 02
# https://adventofcode.com/2017/day/02


checksum = 0

# Reading input from the input file
input_filename='input_sample0.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        in_list = in_string.split()
        in_list = [int(x) for x in in_list]
        checksum += max(in_list) - min(in_list)

print(f'The checksum (answer to A) is {checksum}\n')


