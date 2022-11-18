# adventOfCode 2017 day 16
# https://adventofcode.com/2017/day/16


import copy

def spin(program_line, dance_move_parameter_line):
    ret_val = ''
    spin_count = int(dance_move_parameter_line)
    for i in range(spin_count):
        ch = program_line[-1]
        program_line = program_line[:-1]
        ret_val = ch + ret_val
    for ch in program_line:
        ret_val = ret_val + ch
    return ret_val

def exchange(program_line, dance_move_parameter_line):
    ret_val = ''
    index_0, index_1 = map(lambda x: int(x), dance_move_parameter_line.split('/'))
    ch_0 = copy.deepcopy(program_line[index_0])
    ch_1 = copy.deepcopy(program_line[index_1])
    for ch in program_line:
        if ch == ch_0:
            ret_val += ch_1
        elif ch == ch_1:
            ret_val += ch_0
        else:
            ret_val += ch
    return ret_val

def partner(program_line, dance_move_parameter_line):
    program_0, program_1 = dance_move_parameter_line.split('/')
    return exchange(program_line, f'{program_line.index(program_0)}/{program_line.index(program_1)}')

def get_input_line(input_filename, display):
    print(f'\nUsing input file: {input_filename}\n')
    with open(input_filename) as f:
        in_string = f.readline().rstrip()
    if display:
        print(f'The input is: {in_string}\n')
    return in_string

def get_initial_program_line(initial_length):
    ret_val = ''
    for i in range(initial_length):
        ret_val += chr(ord('a') + i)
    return ret_val

def make_move(program_line, dance_move):
    dance_move_functions = {'s':'spin', 'x':'exchange', 'p':'partner'}
    dance_move_function_name = dance_move_functions[dance_move[0]]
    return globals()[dance_move_function_name](program_line, dance_move[1:])

def discover_loop(program_lines, dance_moves):
    while True:
        for dance_move in dance_moves:
            new_program_line = make_move(program_lines[-1], dance_move)
            # If it could lead to an infinite loop
            # (been seen before at any multiple of number of commands)
            # use this ....  len(dance_moves)
            for i in range(-len(dance_moves), -1 * len(program_lines) - 1, -len(dance_moves)):
                if program_lines[i] == new_program_line:
                    return {
                        'starting_index_of_first_repeat': len(program_lines) + i,
                        'end_index_of_first_repeat__plus_one': len(program_lines), 
                        }
            program_lines.append(new_program_line)

def solve_day16(input_filename, initial_length, display):
    in_string = get_input_line(input_filename, display)
    program_lines = [get_initial_program_line(initial_length)]
    dance_moves = []
    for dance_move in in_string.split(','):
        dance_moves.append(dance_move)
    for dance_move in dance_moves:
        if display:
            print(f'{dance_move}: {program_lines[-1]} => ', end='')
        program_lines.append(make_move(program_lines[-1], dance_move))
        if display:
            print(program_lines[-1])
            print()
    print('The result (to part A) is ', end='')
    print(program_lines[-1])

    loop_info = discover_loop(program_lines, dance_moves)

    print(f'The result (to part B) is: ', end='')
    print(program_lines[(len(dance_moves) * 1000000000) % (loop_info['end_index_of_first_repeat__plus_one'] - loop_info['starting_index_of_first_repeat'])])
solve_day16('input_sample0.txt', 5, True)
# solve_day16('input.txt', 16, False)
print()

def test_get_input_line():
    assert get_input_line('input_sample0.txt', False) == 's1,x3/4,pe/b'

def test_get_initial_program_line():
    assert get_initial_program_line(3) == 'abc'
    assert get_initial_program_line(5) == 'abcde'

def test_spin():
    assert spin('abcde', 3) == 'cdeab'

def test_exchange():
    assert exchange('abcde', '0/2') == 'cbade'

def test_partner():
    assert partner('abcde', 'a/c') == 'cbade'
    assert partner('abcde', 'a/e') == 'ebcda'



