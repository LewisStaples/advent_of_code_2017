# adventOfCode 2017 day 01
# https://adventofcode.com/2017/day/01


num_pairs_a = 0
num_pairs_b = 0

# Reading input from the input file
input_filename='input_sample4.txt'
print(f'\nUsing input file: {input_filename}')
with open(input_filename) as f:
    in_string = f.readline().rstrip()
# Parsing input file   
if len(in_string) < 51:
    print(f'Input: {in_string}\n')
else:
    print()

for i1 in range(len(in_string)):
    i2a = (i1 + int(len(in_string)+1)) % len(in_string)
    i2b = (i1 + int(len(in_string)/2)) % len(in_string)

    if in_string[i1] == in_string[i2a]:
        num_pairs_a += int(in_string[i1])
    if in_string[i1] == in_string[i2b]:
        num_pairs_b += int(in_string[i1])

print(f'The answer to part B is {num_pairs_a}')
print(f'The answer to part B is {num_pairs_b}\n')

