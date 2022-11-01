# adventOfCode 2017 day 16
# https://adventofcode.com/2017/day/16


def redistribute(memory_banks):
    max_bank = max(memory_banks)
    max_bank_index = memory_banks.index(max_bank)
    memory_banks[max_bank_index] = 0
    bank_indices_with_another_block = set()
    for i in range(max_bank % len(memory_banks)):
        bank_indices_with_another_block.add((i + max_bank_index + 1) % len(memory_banks))
    for i in range(len(memory_banks)):
        memory_banks[i] += max_bank//len(memory_banks)
        if i in bank_indices_with_another_block:
            memory_banks[i] += 1
    return memory_banks

# Reading input from the input file
input_filename='input.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    in_string = f.readline().rstrip()
   
memory_banks = [int(x) for x in in_string.split()]
hash_all_memory_banks = {hash(tuple(memory_banks)): 0}
redist_cycle_count = 0

while True:
    redist_cycle_count += 1
    memory_banks = redistribute(memory_banks)
    hash_current_memory_banks = hash(tuple(memory_banks))
    if hash_current_memory_banks not in hash_all_memory_banks:
        # hash_all_memory_banks.add(hash_current_memory_banks)
        hash_all_memory_banks[hash_current_memory_banks] = redist_cycle_count
    else:
        # This configuration has been seen before
        break

print(f'The answer to part A is: {redist_cycle_count}')
print(f'The answer to part B is: {redist_cycle_count - hash_all_memory_banks[hash_current_memory_banks]}\n')
