# adventOfCode 2017 day 3
# https://adventofcode.com/2017/day/3

def get_manh_dist(location_number):
    # Function requires location_number be an integer greater than one.
    #
    # Determine which layer the value is on.
    # I am defining layer # as "length" of a side
    # ("length" is the count of numbers along a single side)
    # 1 is layer 1, 2-9 are layer 3, 10-25 are layer 5, etc.
    # each layer of length L has 2*L + 2*(L-2) = 4*L - 4, for L>2

    if location_number < 2:
        raise ValueError(f'Can only compute Manh. Distance for 2 or greater (not {location_number})')
    layer_num = 1
    layer_value_range = [1,1]
    while True:
        layer_num += 2
        layer_value_range[0] = layer_value_range[1] + 1
        layer_value_range[1] += 4 * layer_num - 4

        if location_number in range(layer_value_range[0], layer_value_range[1]+ 1):
            square_number = (location_number - layer_value_range[0]) % (layer_num - 1)
            axis_dist = abs( square_number - (layer_num // 2 - 1) )

            print(f'man_dist: {axis_dist + layer_num // 2}\n')
            return axis_dist + layer_num // 2



print()
while True:
    value_str = input('Enter puzzle input (non-int to end): ')

    if value_str.isdigit():
        value = int(value_str)
        if value < 2:
            print('Values must be 2 or greater ... try again!')
            continue
        get_manh_dist(value)
    else:
        print('Not an integer ... closing')
        break
print()
