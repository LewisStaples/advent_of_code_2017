# adventOfCode 2017 day 5
# https://adventofcode.com/2017/day/5


# Reading input from the input file (copy to jump_offsets)
input_filename='input_sample0.txt'
print(f'\nUsing input file: {input_filename}\n')
jump_offsets = []
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        jump_offsets.append(int(in_string))
del in_string, input_filename, f
# End of input

# Jump through jump_offsets
step_count = -1
current_jump_index = 0
while True:
    step_count += 1
    try:
        jump_length = jump_offsets[current_jump_index]
    except IndexError:
        break
    jump_offsets[current_jump_index] += 1
    current_jump_index += jump_length

        
print(f'The number of steps (answer to part A) is {step_count}\n')

