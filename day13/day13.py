# adventOfCode 2017 day 13
# https://adventofcode.com/2017/day/13


def get_curr_height(elap_time, range):
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
print(f'\nUsing input file: {input_filename}')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        print(in_string)
        k, v = in_string.split(': ')
        layer__depth_to_range[int(k)] = int(v)
    print()

# Part A
severity = 0
for depth in range(max(layer__depth_to_range.keys()) + 1):
    try:
        if 0 == get_curr_height(depth, layer__depth_to_range[depth]):
            severity += depth * layer__depth_to_range[depth]
    except KeyError:
        pass
print(f'The total severity (part A) is {severity}\n')

# Part B
def try_this_delay():
    for depth in range(max(layer__depth_to_range.keys()) + 1):
        try:
            if 0 == get_curr_height(depth + delay, layer__depth_to_range[depth]):
                # The delay is not enough
                return False
        except KeyError:
            pass
    
    return True

delay = -1
while True:
    delay += 1
    if try_this_delay():
        break

print(f'The smallest value of delay that leads to a journey without getting caught (part B) is {delay}\n')

def test_get_curr_height():
    # Consider a layer with a range of two
    assert get_curr_height(0, 2) == 0
    assert get_curr_height(1, 2) == 1
    assert get_curr_height(2, 2) == 0
    assert get_curr_height(3, 2) == 1
    assert get_curr_height(4, 2) == 0

    # Consider a layer with a range of three
    assert get_curr_height(0, 3) == 0
    assert get_curr_height(1, 3) == 1
    assert get_curr_height(2, 3) == 2
    assert get_curr_height(3, 3) == 1
    assert get_curr_height(4, 3) == 0

    # Consider a layer with a range of four
    assert get_curr_height(0, 4) == 0
    assert get_curr_height(1, 4) == 1
    assert get_curr_height(2, 4) == 2
    assert get_curr_height(3, 4) == 3
    assert get_curr_height(4, 4) == 2
    assert get_curr_height(5, 4) == 1
    assert get_curr_height(6, 4) == 0

    # Consider a layer with a range of eight
    assert get_curr_height(0, 8) == 0
    assert get_curr_height(1, 8) == 1
    assert get_curr_height(2, 8) == 2
    assert get_curr_height(3, 8) == 3
    assert get_curr_height(4, 8) == 4
    assert get_curr_height(5, 8) == 5
    assert get_curr_height(6, 8) == 6
    assert get_curr_height(7, 8) == 7
    assert get_curr_height(8, 8) == 6
    assert get_curr_height(9, 8) == 5
    assert get_curr_height(10, 8) == 4
    assert get_curr_height(11, 8) == 3
    assert get_curr_height(12, 8) == 2
    assert get_curr_height(13, 8) == 1
    assert get_curr_height(14, 8) == 0
