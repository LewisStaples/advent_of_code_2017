# adventOfCode 2017 day 18
# https://adventofcode.com/2017/day/18

import sys


class Tablet:
    def __init__(self):
        self.registers = dict()
        self.last_sound = None

    def get_value(self, value):
        # If int, return it
        if isinstance(value, int):
            return value
        # If a known register, return the value
        if value in self.registers:
            return self.registers[value]
        # If a string representing a number, return it after converting to an int
        try:
            return int(value)
        except ValueError:
            raise ValueError(f'Bad value: {value}')

    def check_valid_reg_name(self, the_string):
        '''
        Verify that the_string has a valid name for a register
        '''
        assert len(the_string) == 1
        assert the_string.isalpha()

    def check_reg_name_in_use(self, the_string):
        '''
        Verify that register the_string is in use
        '''
        assert the_string in self.registers

    def set(self, params):
        self.check_valid_reg_name(params[0])
        self.registers[params[0]] = self.get_value(params[1])

    def add(self, params):
        self.check_valid_reg_name(params[0])
        self.check_reg_name_in_use(params[0])
        self.registers[params[0]] += self.get_value(params[1])

    def mul(self, params):
        self.check_valid_reg_name(params[0])
        self.check_reg_name_in_use(params[0])
        self.registers[params[0]] *= self.get_value(params[1])

    def mod(self, params):
        self.check_valid_reg_name(params[0])
        self.check_reg_name_in_use(params[0])
        self.registers[params[0]] %= self.get_value(params[1])

    def snd(self, params):
        self.last_sound = self.get_value(params[0])

    def rcv(self, params):
        print(f'First recovered sound frequency: {self.last_sound}\n')
        sys.exit('Program exiting successfully')


def get_tablet(input_filename):
    ret_val = []
    print(f'\nUsing input file: {input_filename}\n')
    with open(input_filename) as f:
        max_i = 9
        # Pull in each line from the input file
        for i, in_string in enumerate(f):
            in_string = in_string.rstrip()
            if i <= max_i:
                print(in_string)
            ret_val.append(in_string)
        if i > max_i:
            print(f'(Note: lines {max_i + 2} through {i+1} have been cut off)')
    print()
    return ret_val

def solve_day18(input_filename):
    the_tablet = Tablet()
    input_lines = get_tablet(input_filename)
    line_number = 0
    while line_number < len(input_lines):
        params = input_lines[line_number].split(' ')
        if params[0] == 'jgz':
            if the_tablet.get_value(params[1]) > 0:
                line_number += the_tablet.get_value(params[2])
            else:
                line_number += 1
            continue
        command = getattr(the_tablet, params[0])
        command(params[1:])
        line_number += 1

solve_day18('input_sample0.txt')
