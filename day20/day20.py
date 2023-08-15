#!/usr/bin/env python3

# adventOfCode 2017 day 20
# https://adventofcode.com/2017/day/20


class Axis:
    def __init__(self, input):
        (init_p, init_v, init_a) = input
        self.INIT_P = init_p
        self.INIT_V = init_v
        self.INIT_A = init_a


class Particle:
    def __init__(self, in_string):
        p_string, remainder_string = in_string.split('v')
        v_string, a_string = remainder_string.split('a')
        self.axes = self.get_axes_from_input(p_string, v_string, a_string)

    def get_axes_from_input(self, p_string, v_string, a_string):
        p_values = self.get_values_from_string(p_string)
        v_values = self.get_values_from_string(v_string)
        a_values = self.get_values_from_string(a_string)
        ret_val = list()
        for item in zip(p_values, v_values, a_values):
            ret_val.append(Axis(item))
        return ret_val

    def get_values_from_string(self, in_string):
        in_string = in_string[in_string.index('<')+1:]
        in_string = in_string.replace('>', '')
        value_list = in_string.split(',')
        value_list = [int(ele) for ele in value_list if ele != ' '] 
        return value_list

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
    return the_particles
    
def solve_problem(input_filename):
    the_input = get_input(input_filename)



solve_problem('input_sample0.txt')

# def test_sample_0():
#     solve_problem('input_sample0.txt')

