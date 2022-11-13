# adventOfCode 2017 day 13
# https://adventofcode.com/2017/day/13


def get_curr_depth(elap_time, range):
    # known:  range:2,period:2; range:3,period:4, range:4,period:6
    period = (range - 1) * 2
    # Taking elap_time % period simplifies things
    elap_time %= period
    # Formula for return value depends on relation of elap_time to range
    if elap_time < range:
        return elap_time
    else:
        return period - elap_time

layer__depth_to_range = dict()

# Reading input from the input file
input_filename='input_sample0.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        print(in_string)
        k, v = in_string.split(': ')
        layer__depth_to_range[int(k)] = int(v)


def test_get_curr_depth():
    # Consider a layer with a depth of two
    assert get_curr_depth(0, 2) == 0
    assert get_curr_depth(1, 2) == 1
    assert get_curr_depth(2, 2) == 0
    assert get_curr_depth(3, 2) == 1
    assert get_curr_depth(4, 2) == 0

    # Consider a layer with a depth of four
    assert get_curr_depth(0, 4) == 0
    assert get_curr_depth(1, 4) == 1
    assert get_curr_depth(2, 4) == 2
    assert get_curr_depth(3, 4) == 3
    assert get_curr_depth(4, 4) == 2
    assert get_curr_depth(5, 4) == 1
    assert get_curr_depth(6, 4) == 0

    # Consider a layer with a depth of eight
    assert get_curr_depth(0, 8) == 0
    assert get_curr_depth(1, 8) == 1
    assert get_curr_depth(2, 8) == 2
    assert get_curr_depth(3, 8) == 3
    assert get_curr_depth(4, 8) == 4
    assert get_curr_depth(5, 8) == 5
    assert get_curr_depth(6, 8) == 6
    assert get_curr_depth(7, 8) == 7
    assert get_curr_depth(8, 8) == 6
    assert get_curr_depth(9, 8) == 5
    assert get_curr_depth(10, 8) == 4
    assert get_curr_depth(11, 8) == 3
    assert get_curr_depth(12, 8) == 2
    assert get_curr_depth(13, 8) == 1
    assert get_curr_depth(14, 8) == 0
