# adventOfCode 2017 day 7
# https://adventofcode.com/2017/day/7


from statistics import mean, mode
import sys


def traverse_tower(parent):
    child_sums_list = list()
    for child in programs[parent][1]:
        child_sums_list.append(sum(traverse_tower(child)))
    if len(child_sums_list) > 0:
        most_common_sum = mode(child_sums_list)
        if most_common_sum != mean(child_sums_list):
            # Determine which sum is wrong
            working_variable = set(child_sums_list)
            working_variable.remove(mode(child_sums_list))
            sum_wrong_weight = working_variable.pop()

            for child in programs[parent][1]:
                ttc = traverse_tower(child)
                if sum(ttc) == sum_wrong_weight:
                    print(f'The answer to part B is: {ttc[1] + most_common_sum - sum_wrong_weight}\n')
                    sys.exit('Program has completed successfully')



    return sum(child_sums_list), programs[parent][0]

potential_bottom_pgms = set()
pgms_that_cannot_be_on_bottom = set()
programs = dict()

# Reading input from the input file
input_filename='input.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        program_name, in_string = in_string.split(' (')
        program_wt, in_string = in_string.split(')')
        program_wt = int(program_wt)

        # Handle information to the right of -> (if used)
        descendants = set()
        if '->' in in_string:
            potential_bottom_pgms.add(program_name)
            dummy_not_used, in_string = in_string.split(' -> ')
            for ele in in_string.split(", "):
                descendants.add(ele)
                pgms_that_cannot_be_on_bottom.add(ele)

        programs[program_name] = (program_wt, descendants)
bottom = potential_bottom_pgms.difference(pgms_that_cannot_be_on_bottom).pop()
print(f'The answer to part A is: {bottom}\n')

traverse_tower(bottom)


