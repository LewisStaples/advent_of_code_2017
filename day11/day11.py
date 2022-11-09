# adventOfCode 2017 day 11
# https://adventofcode.com/2017/day/11

import numpy as np


# This defines the compass directions used in the coordinates.
# (Note that these coordinates are not cartesian coordinates)
compass_directions = {
    'east':np.array([1,0]), 
    'west':np.array([-1,0]), 
    'north':np.array([0,1]), 
    'south':np.array([0,-1])
    }

# This maps each input step string to the directions traversed
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
    return ret_val


def get_distance_to_coordinates(coords):
    if np.array_equal((0,0), coords):
        return 0
    dist_traversed = 0
    distances_found = {(0,0): 0}
    while True:
        for dist in [key for key, val in distances_found.items() if val == dist_traversed]:
            for new_step in steps.values():
                new_dist = np.array(dist) + new_step
                if tuple(new_dist) not in distances_found:
                    if np.array_equal(new_dist, coords):
                        print(f'Answer: {dist_traversed + 1}')
                        return dist_traversed + 1
                    distances_found[tuple(new_dist)] = dist_traversed + 1

        dist_traversed += 1

    
def solve_day11(input_filename, display = False):
    in_string = get_input_line(input_filename, display)
    coords = get_coordinates_from_input(in_string, display)
    return get_distance_to_coordinates(coords)


print(f"The answer to part A is: {solve_day11('input.txt')}")

def test_one():
    assert 3 == solve_day11('input_sample0.txt', display = True)

def test_two():
    assert 0 == solve_day11('input_sample1.txt', display = True)

def test_three():
    assert 2 == solve_day11('input_sample2.txt', display = True)

def test_four():
    assert 3 == solve_day11('input_sample3.txt', display = True)
