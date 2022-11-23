# adventOfCode 2017 day 19
# https://adventofcode.com/2017/day/19


import numpy as np

# POTENTIAL ALTERNATIVE FOR SINGLE LINE INPUT FILES ....

def load_input(input_filename):
    '''
    Load input text(graph) into memory
    '''
    input_text = []
    print(f'\nUsing input file: {input_filename}\n')
    with open(input_filename) as f:
        # Pull in each line from the input file
        for in_string in f:
            in_string = in_string.rstrip('\n')
            input_text.append(list(in_string))
            print(in_string)
    print()
    return input_text

def convert_text_to_graph(input_text):
    ret_val = {
        'vertices': []
    }

    pointer = {
        'location': np.array([input_text[0].index('|'), 0]),
        'direction': np.array([0,1])
    }

    # while True:
    while input_text[pointer['location'][0]][pointer['location'][1]] != '+':
        pointer['location'] += pointer['direction']
    return ret_val

def solve_problem(input_filename):
    input_text = load_input(input_filename)
    the_graph = convert_text_to_graph(input_text)

solve_problem('input_sample0.txt')



