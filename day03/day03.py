
from re import L


def get_coords(location_number):
    # Determine which layer the value is on.
    # I am defining layer # as "length" of a side
    # ("length" is the count of numbers along a single side)
    # 1 is layer 1, 2-9 are layer 3, 10-25 are layer 5, etc.
    # each layer of length L has 2*L + 2*(L-2) = 4*L - 4, for L>2
    
    layer_num = 1
    layer_value_range = [1,1]
    while True:
        layer_num += 2
        layer_value_range[0] = layer_value_range[1] + 1
        layer_value_range[1] += 4 * layer_num - 4

        # print(layer_value_range)

        if location_number in range(layer_value_range[0], layer_value_range[1]+ 1):
            print(layer_num)
            print(layer_value_range)
            break



    return [1,2]

print()
while True:
    # non-int input triggers a ValueError, which ends it
    value_str = input('Enter puzzle input (non-int to end): ')

    # # force only a single input
    # break

    if value_str.isdigit():
        value = int(value_str)
        coords = get_coords(value)
    else:
        break
    dummy = 123

print()
