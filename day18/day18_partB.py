# adventOfCode 2017 day 18
# https://adventofcode.com/2017/day/18

import sys
import asyncio


class Program:
    message_queue = dict()
    def __init__(self, program_ID):
        assert isinstance(program_ID, int)
        self.PROGRAM_ID = program_ID
        self.registers = {'p': self.PROGRAM_ID}
        self.count_sent = 0
        Program.message_queue[self.PROGRAM_ID] = []

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
        If register the_string is not initially in use, 
        set register the_string to zero.
        If, alternatively, register the_string has a known value,
        then leave it as is.
        '''
        if the_string not in self.registers:
            self.registers[the_string] = 0

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
        self.count_sent += 1
        Program.message_queue[self.PROGRAM_ID].append(params[0])

    async def rcv(self, params):
        while len(Program.message_queue[(self.PROGRAM_ID + 1) % 2]) == 0:
            await asyncio.sleep(1)

        # print(f'Count of messages sent by program 1 (answer to B): {self.count_sent}')
        # sys.exit('Program exiting successfully')

    async def run(self, input_lines):
        line_number = 0
        while line_number < len(input_lines):
            params = input_lines[line_number].split(' ')
            if params[0] == 'jgz':
                if self.get_value(params[1]) > 0:
                    line_number += self.get_value(params[2])
                else:
                    line_number += 1
                continue
            elif params[0] == 'rcv':
                await self.rcv(params[1:])
            command = getattr(self, params[0])
            command(params[1:])
            line_number += 1

def get_assembly_code(input_filename):
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
            print(f'(Note: lines {max_i + 2} through {i+1} will not be displayed)')
    print()
    return ret_val

async def solve_day18(input_filename):
    program_0 = Program(0)
    program_1 = Program(1)
    input_lines = get_assembly_code(input_filename)
    await program_0.run(input_lines)
    await program_1.run(input_lines)


if __name__ == "__main__":
    asyncio.run(solve_day18('input.txt'))


# await solve_day18('input.txt')
# 
# if __name__ == "__main__":
#     asyncio.run(main())
