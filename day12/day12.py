# adventOfCode 2017 day 12
# https://adventofcode.com/2017/day/12


# FOR MULTILINE FILES .....
# Reading input from the input file
def get_pipe_info(input_filename, display):
    ret_val = dict()
    # if display:
    print(f'\nUsing input file: {input_filename}')
    with open(input_filename) as f:
        # Pull in each line from the input file
        for in_string in f:
            in_string = in_string.rstrip()
            this_pipe, other_pipes = in_string.split(' <-> ')
            this_pipe = int(this_pipe)
            other_pipes = other_pipes.split(', ')
            other_pipes  = {int(x) for x in other_pipes}
            ret_val[this_pipe] = other_pipes
            if display:
                print(in_string)
    # if display:
        # print()
    return ret_val

def solve_day12(input_filename, display):
    pipe_info = get_pipe_info(input_filename, display)
    
    program_group = {0}
    next_programs = pipe_info[0]
    
    while len(next_programs) > 0:
        the_next_program = next_programs.pop()
        if the_next_program not in program_group:
            program_group.add(the_next_program)
            next_programs.update(pipe_info[the_next_program])
    print(f'The size of the program group (answer to A) is {len(program_group)}\n')
    return len(program_group)

solve_day12('input_sample0.txt', True)
solve_day12('input.txt', False)

