#!/usr/bin/env python3

# adventOfCode 2017 day 20
# https://adventofcode.com/2017/day/20


class Particle:
    def __init__(self, in_string):
        p_string, remainder_string = in_string.split('v')
        v_string, a_string = remainder_string.split('a')

        self.p_values = self.get_values_from_string(p_string)
        self.v_values = self.get_values_from_string(v_string)
        self.a_values = self.get_values_from_string(a_string)

    def get_values_from_string(self, in_string):
        in_string = in_string[in_string.index('<')+1:]
        in_string = in_string.replace('>', '')
        value_list = in_string.split(',')
        value_list = [int(ele) for ele in value_list if ele != ' '] 
        return value_list

def get_input(input_filename):
    # the_particles = list()
    the_particles = dict()
    # Reading input from the input file
    print(f'\nUsing input file: {input_filename}\n')
    with open(input_filename) as f:
        # Pull in each line from the input file
        for particle_number, in_string in enumerate(f):
            in_string = in_string.rstrip()
            print(in_string)
            # the_particles.append(Particle(in_string))
            particle_number_label = f'particle # {particle_number}'
            the_particles[particle_number_label] = Particle(in_string)
    print()
    return the_particles


def get_sum_abs(in_list):
    ret_val = 0
    for ele in in_list:
        ret_val += abs(ele)
    return ret_val


def get_smallest_particle_number(the_particles):
    smallest_seen_values = {
        'a' : {'value' : float('inf'), 'particle_number' : 0}, 
        'v' : {'value' : float('inf'), 'particle_number' : 0}, 
        'p' : {'value' : float('inf'), 'particle_number' : 0}
        }
    
    for particle_number_label, the_particle in the_particles.items():
        particle_number_int = int(particle_number_label[11:])
        dummy = 123
        for variable in smallest_seen_values:
            values_member_str = variable + '_values'
            new_value = get_sum_abs(getattr(the_particle, values_member_str))
            if smallest_seen_values[variable]['value'] is None:
                pass
            elif new_value == smallest_seen_values[variable]['value']:
                smallest_seen_values[variable]['value'] = None
            elif new_value < smallest_seen_values[variable]['value']:
                smallest_seen_values[variable]['value'] = new_value
                smallest_seen_values[variable]['particle_number'] = particle_number_int


            dummy = 123

    dummy = 123
    for variable, value__paricle_number in smallest_seen_values.items():
        if value__paricle_number['value'] is None:
            continue
        
        return value__paricle_number['particle_number']
    
        # # Loop through axes
        # for i in range(len(the_particle.a_values)):
        #     dummy = 123
            
# bar = getattr(foo, 'bar')
# result = bar()

        # Develop lists of pointers to the greatest abs value of a_values axes by going from one particle to the next one
        # If a tie is needed, go to v_values and then p_values.
    
    # return whichever particle is closest to <0,0,0> in the long term

def solve_problem(input_filename):
    the_particles = get_input(input_filename)
    smallest_particle_number = get_smallest_particle_number(the_particles)

    print(f'Answer: {smallest_particle_number}\n')

    # axis_values_0_1_2 = get_axis_values_0_1_2(the_particles)
    # the_coefficients = get_coefficients(the_particles, axis_values_0_1_2)



solve_problem('input.txt')

# def test_sample_0():
#     solve_problem('input_sample0.txt')

