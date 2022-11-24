# Helper program to determine what characters are in the input files.
# The input has letters, and these characters:  space, pipe, minus/dash, plus
all_chars = set() 

# Reading input from the input file
input_filename='input_sample0.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip('\n')
        print(in_string)
        all_chars.update(list(in_string))
print()

print('All non-letter characters:')
for ch in all_chars:
    if not ch.isalpha():
        print(f'"{ch}"    ', end='')
print()
print()

print('All letter characters:')
for ch in all_chars:
    if ch.isalpha():
        print(f'"{ch}"    ', end='')
print()
print()

