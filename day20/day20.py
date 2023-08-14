#!/usr/bin/env python3

# adventOfCode 2017 day 20
# https://adventofcode.com/2017/day/20


class Axis:
    def __init__(self, init_p, init_v, init_a):
        self.INIT_P = init_p
        self.INIT_V = init_v
        self.INIT_A = init_a


class Particle:
    def __init__(self, in_string):
        p_string, remainder_string = in_string.split('v')
        v_string, a_string = remainder_string.split('a')
        # p_string = p_string.replace('p=', '')
        # p_string = p_string.replace('<', '')
        # p_string = p_string.replace('>', '')
        self.axes = list()


def get_input(input_filename):
    the_particles = list()
    # Reading input from the input file
    print(f'\nUsing input file: {input_filename}\n')
    with open(input_filename) as f:
        # Pull in each line from the input file
        for in_string in f:
            in_string = in_string.rstrip()
            print(in_string)
            the_particles.append(Particle(in_string))
    print()
    
def solve_problem(input_filename):
    the_input = get_input(input_filename)



solve_problem('input_sample0.txt')

# def test_sample_0():
#     solve_problem('input_sample0.txt')

