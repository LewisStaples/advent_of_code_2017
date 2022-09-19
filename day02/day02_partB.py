# adventOfCode 2017 day 02
# https://adventofcode.com/2017/day/02


from itertools import combinations


sum_B = 0
input_filename='input_sample1.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        in_list = in_string.split()
        in_list = [int(x) for x in in_list]

        in_list.sort()

        for pair in combinations(in_list, 2):
            # Because in_list was sorted, I don't need to also check pair[0] % pair[1]
            if pair[1] % pair[0] == 0:
                sum_B += pair[1] // pair[0]
                break
            

print(f'The answer to part B is {sum_B}\n')

