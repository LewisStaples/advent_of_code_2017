# adventOfCode 2017 day 12
# https://adventofcode.com/2017/day/12


import copy

# Reading input from the input file
def get_pipe_info(input_filename, display):
    ret_val = dict()
    print(f'\nUsing input file: {input_filename}')
    with open(input_filename) as f:
        for in_string in f:
            in_string = in_string.rstrip()
            this_pipe, other_pipes = in_string.split(' <-> ')
            this_pipe = int(this_pipe)
            other_pipes = other_pipes.split(', ')
            other_pipes  = {int(x) for x in other_pipes}
            ret_val[this_pipe] = other_pipes
            if display:
                print(in_string)
    return ret_val

def solve_day12(input_filename, display):
    pipe_info = get_pipe_info(input_filename, display)
    all_program_groups = [{0}]
    next_programs = copy.deepcopy(pipe_info[0])
    del pipe_info[0]
    while True:
        while len(next_programs) > 0:
            the_next_program = next_programs.pop()
            if the_next_program not in all_program_groups[-1]:
                all_program_groups[-1].add(the_next_program)
                next_programs.update(pipe_info[the_next_program])
                del pipe_info[the_next_program]
        if len(pipe_info) == 0:
            break
        program_new_group, next_programs = pipe_info.popitem()
        all_program_groups.append({program_new_group})
    print(f'The size of the program group (answer to A) is {len(all_program_groups[0])}')
    print(f'The total count of program groups (answer to B) is: {len(all_program_groups)}')


solve_day12('input_sample0.txt', True)
print('------------------------------------------------')
solve_day12('input.txt', False)
print()
