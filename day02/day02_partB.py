# adventOfCode 2017 day 02
# https://adventofcode.com/2017/day/02


sum = 0

# Reading input from the input file
input_filename='input_sample1.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        in_list = in_string.split()
        in_list = [int(x) for x in in_list]

        # try this
        # https://docs.python.org/3/library/bisect.html#searching-sorted-lists
        
        in_list.sort(reverse=True)
        # print(in_list)

        evenly_div_pair_not_found = True
        while evenly_div_pair_not_found:
            smallest_val = in_list.pop()
            smallest_val_mult = smallest_val
            while len(in_list) > 0:
                if smallest_val_mult in in_list:  # Plan to replace with a faster search, given that it's a sorted list
                    # something else
                    # print(f'{smallest_val_mult} is evenly divisible by {smallest_val}')
                    # print(f'  and the multiple is {smallest_val_mult // smallest_val}')

                    sum += smallest_val_mult // smallest_val
                    evenly_div_pair_not_found = False
                    break
                # print(f'{smallest_val_mult} is not evenly divisible by {smallest_val}')
                smallest_val_mult += smallest_val

            # print(in_list)
            # print()
            dummy = 123

print(f'The answer to part B is {sum}')

