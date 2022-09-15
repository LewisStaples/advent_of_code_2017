# adventOfCode 2017 day 01
# https://adventofcode.com/2017/day/01


num_pairs = 0

# Reading input from the input file
input_filename='input_sample0.txt'
print(f'\nUsing input file: {input_filename}')
with open(input_filename) as f:
    in_string = f.readline().rstrip()
# Parsing input file   
if len(in_string) < 51:
    print(f'Input: {in_string}\n')
else:
    print()

for i1 in range(len(in_string)):
    i2 = (i1 + 1) % len(in_string)
    
    if in_string[i1] == in_string[i2]:
        num_pairs += int(in_string[i1])

print(f'The answer to part A is {num_pairs}\n')

