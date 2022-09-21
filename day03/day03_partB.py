# adventOfCode 2017 day 3
# https://adventofcode.com/2017/day/3

from math import cos, pi, sin
import sys

class SquareGrid:
    def __init__(self):
        self.values = dict()
        self.delta_list = [(-1,-1), (-1,0), (-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

    def populate_cell(self, coords):
        new_value = 0

        for delta in self.delta_list:
            adjacent_cell = list()
            adjacent_cell.append(coords[0] + delta[0])
            adjacent_cell.append(coords[1] + delta[1])
            adjacent_cell = tuple(adjacent_cell)
            if adjacent_cell in self.values:
                new_value += self.values[adjacent_cell]
        
        self.values[coords] = new_value
        return new_value


    def populate_grid(self, value):
        self.values.clear()

        coords = [0,0]
        self.values[tuple(coords)] = 1
        
        i = 0

        while True:
            displacement_mag = (i + 2) // 2
            displacement_unit_hor = round(cos(i * pi / 2))
            displacement_unit_vert = round(sin(i * pi / 2))

            for j in range(displacement_mag):
                coords[0] += displacement_unit_hor
                coords[1] += displacement_unit_vert
                new_value = self.populate_cell(tuple(coords))
                if new_value > value:
                    self.display()
                    print(f'The answer to part B is {new_value}, as it is the first value larger than {value}')
                    sys.exit('Exiting')
            i += 1

    def display(self):
        if len(self.values) == 0:
            print('[Values is empty]')
        if len(self.values) > 25:
            print('[Values too large to print !!! ]')
            return
        for coords, value in self.values.items():
            print (f'Position: {coords}, Value: {value}')
        print()


print()
the_grid = SquareGrid()
the_grid.populate_grid(800)  # 800 leads to calculating the given sample (ungraded) data



