# adventOfCode 2017 day 8
# https://adventofcode.com/2017/day/8


import operator

class Register:
    def __init__(self):
        # index: register's name (alphabetical string), value: value of register (int)
        self.register_storage = dict() 

    def get_value(self, string_input):
        # If it's an int value, return the int value
        try:
            ret_val = int(string_input)
            return ret_val
        except ValueError:
            # The exception happened because its not an int.
            pass

        # If the register is previously known, return the known value
        if string_input in self.register_storage:
            return self.register_storage[string_input]

        # Since the register isn't previously known, fill-in and return 0
        self.register_storage[string_input] = 0
        return 0

    def set_value(self, index, new_int):
        self.register_storage[index] = new_int

    def parse_input(self, in_string):
        operation, condition = in_string.split(' if ')

        # Parse the condition
        value1, op_str, value2 = condition.split()
        value1, value2 = (self.get_value(x) for x in (value1, value2))
        ops = {'>': operator.gt,
            '<': operator.lt,
            '>=': operator.ge,
            '<=': operator.le,
            '==': operator.eq,
            '!=': operator.ne}
        if not ops[op_str](value1, value2):
            # If the condition is False, stop parsing input
            return

        # Anytime this point is reached condition must be True, thus perform operation
        register_str, op_str, value = operation.split()
        value = self.get_value(value)
        if op_str == 'inc':
            self.set_value(register_str, self.get_value(register_str) + value)
        elif op_str == 'dec':
            self.set_value(register_str, self.get_value(register_str) - value)

the_register = Register()
# Reading input from the input file
input_filename='input_sample0.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        the_register.parse_input(in_string)

print(f'\nThe answer is: {max(the_register.register_storage.values())}\n')

