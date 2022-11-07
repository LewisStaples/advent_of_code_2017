# adventOfCode 2017 day 10
# https://adventofcode.com/2017/day/10


# Reading input from the input file
input_filename='input.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    length_list = f.readline().rstrip().split(',')
   
circ_list = []
current_position = 0
skip_length = 0

circ_list_len = 5 if len(length_list) == 4 else 256
for i in range(circ_list_len):
    circ_list.append(len(circ_list))
length_list = [int(x) for x in length_list]

print(f'input list of lengths: {length_list}')
if len(circ_list) < 20:
    print(f'circular list: {circ_list}')
print()

for length in length_list:
    # reverse the two indices
    i = current_position
    j = (current_position + length - 1) % circ_list_len
    for loop_counter in range(length // 2):
        temp = circ_list[i]
        circ_list[i] = circ_list[j]
        circ_list[j] = temp
        i = (i + 1) % circ_list_len
        j = (j - 1) % circ_list_len

    current_position += length + skip_length
    current_position %= circ_list_len
    skip_length += 1

print(f'The answer to part A is {circ_list[0] * circ_list[1]}\n')

