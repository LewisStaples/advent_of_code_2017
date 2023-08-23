#!/usr/bin/env python3

# adventOfCode 2017 day 21
# https://adventofcode.com/2017/day/21


def get_input(input_filename):
    # Reading input from the input file
    print(f'\nUsing input file: {input_filename}\n')
    with open(input_filename) as f:
        # Pull in each line from the input file
        for in_string in f:
            in_string = in_string.rstrip()
            print(in_string)
    print()
    
def solve_problem(input_filename):
    the_input = get_input(input_filename)


solve_problem('input.txt')

# def test_sample_0():
#     solve_problem('input_sample0.txt')




