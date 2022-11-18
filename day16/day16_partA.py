# adventOfCode 2017 day 16
# https://adventofcode.com/2017/day/16


def spin(program_line, dance_move_parameter_line):
    spin_count = int(dance_move_parameter_line)
    for i in range(spin_count):
        ch = program_line.pop()
        program_line.insert(0, ch)
    return program_line

def exchange(program_line, dance_move_parameter_line):
    index_0, index_1 = map(lambda x: int(x), dance_move_parameter_line.split('/'))
    program_line[index_0], program_line[index_1] = program_line[index_1], program_line[index_0]
    return program_line

def partner(program_line, dance_move_parameter_line):
    program_0, program_1 = dance_move_parameter_line.split('/')
    exchange(program_line, f'{program_line.index(program_0)}/{program_line.index(program_1)}')
    return program_line

def get_input_line(input_filename, display):
    print(f'\nUsing input file: {input_filename}\n')
    with open(input_filename) as f:
        in_string = f.readline().rstrip()
    if display:
        print(f'The input is: {in_string}\n')
    return in_string

def get_initial_program_line(initial_length):
    ret_val = []
    for i in range(initial_length):
        ret_val.append(chr(ord('a') + i))
    return ret_val

def make_move(program_line, dance_move):
    dance_move_functions = {'s':'spin', 'x':'exchange', 'p':'partner'}
    dance_move_function_name = dance_move_functions[dance_move[0]]
    return globals()[dance_move_function_name](program_line, dance_move[1:])

def solve_day16(input_filename, initial_length, display):
    in_string = get_input_line(input_filename, display)
    program_line = get_initial_program_line(initial_length)
    for dance_move in in_string.split(','):
        if display:
            print(f'{dance_move}: {program_line} => ', end='')
        program_line = make_move(program_line, dance_move)
        if display:
            print(program_line)
            print()
    
    print('The result (to part A) is ', end='')
    print(''.join(program_line))

solve_day16('input_sample0.txt', 5, True)
# solve_day16('input.txt', 16, False)
print()

def test_get_input_line():
    assert get_input_line('input_sample0.txt', False) == 's1,x3/4,pe/b'

def test_get_initial_program_line():
    assert get_initial_program_line(3) == ['a', 'b', 'c'] # 'abc'
    assert get_initial_program_line(5) == ['a', 'b', 'c', 'd', 'e'] # 'abcde'

def test_spin():
    assert spin(['a', 'b', 'c', 'd', 'e'], '3') == ['c', 'd', 'e', 'a', 'b'] # 'cdeab'

def test_exchange():
    assert exchange(['a', 'b', 'c', 'd', 'e'], '0/2') == ['c', 'b', 'a', 'd', 'e']

def test_partner():
    assert partner(['a', 'b', 'c', 'd', 'e'], 'a/c') == ['c', 'b', 'a', 'd', 'e']
    assert partner(['a', 'b', 'c', 'd', 'e'], 'a/e') == ['e', 'b', 'c', 'd', 'a']
