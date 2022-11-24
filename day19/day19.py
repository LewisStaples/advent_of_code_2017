# adventOfCode 2017 day 19
# https://adventofcode.com/2017/day/19


import numpy as np


def load_input(input_filename):
    '''
    Load input text(graph) into memory
    '''
    input_text = []
    start_location = None
    print(f'\nUsing input file: {input_filename}\n')
    with open(input_filename) as f:
        # Pull in each line from the input file
        for i, in_string in enumerate(f):
            in_string = in_string.rstrip('\n')
            for j, ch in enumerate(in_string):
                if i == 0:
                    input_text.append([])
                    if ch == '|':
                        start_location = j
                input_text[j].append(ch)
            if len(in_string) < 20:
                print(in_string)
    print()

    # Surround the input_text with spaces on all sides
    # (Therefore a space will indicate a boundary)
    if set(input_text[0]) != {' '}:
        print('ALERT! More cushioning needed!')
    if set(input_text[-1]) != {' '}:
        print('ALERT! More cushioning needed!')
    for i, ch_array in enumerate(input_text):
        if ch_array[-1] != ' ':
            input_text[i].append(' ')

    return input_text, start_location

def swap(np_array_two_ele):
    '''
    Swap values at indices 0 and 1
    '''
    temp = np_array_two_ele[1]
    np_array_two_ele[1] = np_array_two_ele[0]
    np_array_two_ele[0] = temp

def get_char(pointer, input_text):
	return input_text[pointer['location'][0]][pointer['location'][1]]


def convert_text_to_graph(input_text, start_location):
    # The below could be expanded into a data structure of vertices and edges
    # (depending on what the requirements of part B/2 are)
    ret_val = {
        'vertices': []
    }

    pointer = {
        'location': np.array([start_location, 0]),
        'direction': np.array([0,1])
    }

    while get_char(pointer, input_text) != ' ':
        if get_char(pointer, input_text) == '+':
            swap(pointer['direction'])
            pointer['location'] += pointer['direction']
            if get_char(pointer, input_text) == ' ':
                pointer['direction'] *= -1
                # modify location by twice direction (once back to the "+" and then once to where it should have gone)
                pointer['location'] += 2 * pointer['direction']
        else:
            pointer['location'] += pointer['direction']

        if get_char(pointer, input_text).isalpha():
            ret_val['vertices'].append(get_char(pointer, input_text))
    return ret_val

def solve_problem(input_filename):
    input_text, start_location = load_input(input_filename)
    the_graph = convert_text_to_graph(input_text, start_location)
    print('The letters on the path are (soln. to part A):  ',end='')
    print(''.join(the_graph['vertices']))
    print()


solve_problem('input_sample0.txt')



