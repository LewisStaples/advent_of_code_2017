# adventOfCode 2017 day 17
# https://adventofcode.com/2017/day/17


circ_buffer = [0]
current_index = 0

input_filename = 'input.txt'
with open(input_filename) as f:
    steps_advanced = int(f.readline().rstrip())
print(f'\nUsing input file: {input_filename} with steps_advanced: {steps_advanced}')

for i in range(1, 50000001):
    current_index = (current_index + steps_advanced) % (i) + 1
    if current_index == 1:
        circ_buffer.append(i)

print(f'\nThe answer to part B is : {circ_buffer[-1]}\n')


