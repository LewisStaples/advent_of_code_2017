# adventOfCode 2017 day 15
# https://adventofcode.com/2017/day/15


import numpy as np

generators = np.array([None, None])
judge_count = 0

# Reading input from the input file
input_filename='input.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    generators[0] = int(f.readline().rstrip().split(' starts with ')[1])
    generators[1] = int(f.readline().rstrip().split(' starts with ')[1])
for i in range(40000000):   
    generators = np.multiply(generators, np.array([16807, 48271]))
    generators = np.mod(generators, 2147483647)
    if bin(generators[0])[-16:] == bin(generators[1])[-16:]:
        judge_count += 1
print(f'total (part A answer): {judge_count}\n')

