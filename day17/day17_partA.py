# adventOfCode 2017 day 17
# https://adventofcode.com/2017/day/17


circ_buffer = [0]
current_index = 0

input_filename = 'input_sample0.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    steps_advanced = int(f.readline().rstrip())
if steps_advanced == 3:
    display = True
else:
    display = False

# display = False
for i in range(1, 20):
# for i in range(1, 2018):
    current_index = (current_index + steps_advanced) % (len(circ_buffer))
    circ_buffer.insert((current_index + 1) % (1 + len(circ_buffer)), i)
    current_index = (current_index + 1) % len(circ_buffer)
    if display:
        print(circ_buffer, end='')
        print(f'  ---  {circ_buffer[current_index]} is at current position')

print(f'\nThe answer to part A is : {circ_buffer[(current_index + 1) % len(circ_buffer)]}\n')


