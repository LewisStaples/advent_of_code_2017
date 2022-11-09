# adventOfCode 2017 day 11
# https://adventofcode.com/2017/day/11

import numpy as np


# This program has defined a coordinate system to identify all tiles.
# The below notes define how the input characters are represented in the coordinates.
# n alone will be treated as +2 in the vertical direction
# n before w or e will be treated as +1 in the vertical direction
# s alone will be treated as -2 in the vertical direction
# s before w or e will be treated as -1 in the vertical direction
# w after n or s will be treated as -1 in the horizontal direction
# e after n or s will be treated as +1 in the horizontal direction
# 
# This defines the compass directions used in the coordinates.
# (Note that these coordinates are not cartesian coordinates)
compass_directions = {
    'east':np.array([1,0]), 
    'west':np.array([-1,0]), 
    'north':np.array([0,1]), 
    'south':np.array([0,-1])
    }

steps = {
    'n': 2 * compass_directions['north'],
    'ne': compass_directions['north'] + compass_directions['east'],
    'se': compass_directions['south'] + compass_directions['east'],
    's': 2 * compass_directions['south'],
    'sw': compass_directions['south'] + compass_directions['west'],
    'nw': compass_directions['north'] + compass_directions['west'],
 }




def get_input_line(input_filename, display):
    with open(input_filename) as f:
        in_string = f.readline().rstrip()
    if display:
        print(f'\nUsing input file: {input_filename}\n')
        print(f'The input is: {in_string}\n')
    return in_string


def get_coordinates_from_input(in_string, display):
    ret_val = np.array([0,0])
    if display:
        print(f'Initial position: {ret_val}')
    for this_step in in_string.split(','):
        ret_val += steps[this_step]
        if display:
            print(f'{this_step}: {ret_val}')


def solve_day11(input_filename, display = False):
    in_string = get_input_line(input_filename, display)
    get_coordinates_from_input(in_string, display)


# solve_day11('input.txt')

def test_one():
    solve_day11('input_sample0.txt', display = True)

def test_two():
    solve_day11('input_sample1.txt', display = True)

def test_three():
    solve_day11('input_sample2.txt', display = True)

def test_four():
    solve_day11('input_sample3.txt', display = True)
