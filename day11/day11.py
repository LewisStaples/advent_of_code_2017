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


def get_path_from_input(in_string, display):
    path = [np.array([0,0])]
    if display:
        print(f'Initial position: {path[0]}')
    for this_step in in_string.split(','):
        path.append(path[-1] + steps[this_step])
        if display:
            print(f'{this_step}: {path[-1]}')
    return path


def get_distances_to_coordinates(path):
    ret_val = []
    path_points = {tuple(x) for x in path[1:-1]}

    if np.array_equal(np.array([0,0]), path[-1]):
        ret_val.append(0)
    dist_traversed = 0
    distances_found = {(0,0): 0}
    while True:
        for dist in [key for key, val in distances_found.items() if val == dist_traversed]:
            for new_step in steps.values():
                new_dist = np.array(dist) + new_step
                if tuple(new_dist) not in distances_found:
                    if np.array_equal(new_dist, path[-1]):
                        ret_val.append(dist_traversed + 1)
                    distances_found[tuple(new_dist)] = dist_traversed + 1
        # See if the last point has already been found
        if len(ret_val) > 0:
            # Check if remaining points have been found
            if len(path_points.difference(set(distances_found.keys()))) == 0:
                ret_val.append(dist_traversed + 1)
                return ret_val
        dist_traversed += 1

    
def solve_day11(input_filename, display = False):
    in_string = get_input_line(input_filename, display)
    path = get_path_from_input(in_string, display)
    return get_distances_to_coordinates(path)

solutions = solve_day11('input.txt')
print(f"The answer to part A is: {solutions[0]}")
print(f"The answer to part B is: {solutions[1]}")


def test_one():
    solutions = solve_day11('input_sample0.txt', display = True)
    assert solutions[0] == 3

def test_two():
    solutions = solve_day11('input_sample1.txt', display = True)
    assert solutions[0] == 0 

def test_three():
    solutions = solve_day11('input_sample2.txt', display = True)
    assert solutions[0] == 2 

def test_four():
    solutions = solve_day11('input_sample3.txt', display = True)
    assert solutions[0] == 3
