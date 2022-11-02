# adventOfCode 2017 day 7
# https://adventofcode.com/2017/day/7


# Note to self:  this program disregards all program weights
# My expectation is that part B / part 2 will require use of those weights,
# which will probably require a complete reworking of the data structures
# used, but that is not required to solve this part.
potential_bottom_pgms = set()
pgms_that_cannot_be_on_bottom = set()

# Reading input from the input file
input_filename='input.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        if '->' not in in_string:
            continue
        lhs, rhs = in_string.split(' -> ')
        potential_bottom_pgms.add(lhs.split()[0])
        for ele in rhs.split(", "):
            pgms_that_cannot_be_on_bottom.add(ele)

print(f'The answer to part A is: {potential_bottom_pgms.difference(pgms_that_cannot_be_on_bottom)}\n')

