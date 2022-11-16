# adventOfCode 2017 day 15
# https://adventofcode.com/2017/day/15


import numpy as np

factor = np.array([16807, 48271], dtype=np.int64)
divisor = 2147483647
def try_value(generators, index):
    ret_val = np.multiply(generators[index], factor[index])
    ret_val = np.mod(ret_val, divisor)
    return ret_val

def next_value(generators):
    ret_val = np.array([
        try_value(generators, 0) ,
        try_value(generators, 1)
    ])
    while(ret_val[0] % 4 != 0):
        ret_val[0] = try_value(ret_val, 0)
    while(ret_val[1] % 8 != 0):
        ret_val[1] = try_value(ret_val, 1)
    return ret_val

generators = np.array([None, None])
judge_count = 0

# Reading input from the input file
input_filename='input.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    generators[0] = int(f.readline().rstrip().split(' starts with ')[1])
    generators[1] = int(f.readline().rstrip().split(' starts with ')[1])
for i in range(5000000):   
    generators = next_value(generators)
    if bin(generators[0])[-16:] == bin(generators[1])[-16:]:
        judge_count += 1
print(f'total (part B answer): {judge_count}\n')


