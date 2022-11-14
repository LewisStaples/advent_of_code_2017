# adventOfCode 2017 day 10
# https://adventofcode.com/2017/day/10


def get_sparse_hash(input_str_proc):
    sparse_hash = []
    current_position = 0
    skip_length = 0

    for i in range(256):
        sparse_hash.append(len(sparse_hash))


    # if len(sparse_hash) < 20:
    #     print(f'circular list: {sparse_hash}')
    # print()

    # Perform 64 rounds.  The end result will be the sparse hash
    for dummy_counter in range(64):
        for loop_counter, length in enumerate(input_str_proc):
            # reverse the two indices
            i = current_position
            j = (current_position + length - 1) % len(sparse_hash)
            for loop_counter in range(length // 2):
                temp = sparse_hash[i]
                sparse_hash[i] = sparse_hash[j]
                sparse_hash[j] = temp
                i = (i + 1) % len(sparse_hash)
                j = (j - 1) % len(sparse_hash)

            if loop_counter != len(input_str_proc) - 1:
                current_position += length + skip_length
                current_position %= len(sparse_hash)
                skip_length += 1

    return sparse_hash


def input_processing(in_string):
    ret_val = []
    for ch in in_string:
        ret_val.append(ord(ch))
    ret_val.extend([17, 31, 73, 47, 23])
    return ret_val

def get_dense_hash(sparse_hash):
    dense_hash = []
    while len(sparse_hash) > 0:
        next_dense_hash_ele = 0
        for i in range(16):
            next_dense_hash_ele ^= sparse_hash.pop(0)
        dense_hash.append(next_dense_hash_ele)
    return dense_hash

def get_knox_hash_hex(dense_hash):
    knox_hash_hex = ''
    while len(dense_hash) > 0:
        knox_hash_hex += (hex(dense_hash.pop(0))[2:]).zfill(2)
    return knox_hash_hex

def get_knox_hash_bin(knox_hash_hex):
    knox_hash_bin = ''
    for ch in knox_hash_hex:
        int_repr = int(ch, 16)
        bin_repr = bin(int_repr)
        knox_hash_bin += bin_repr[2:].zfill(4)
    return knox_hash_bin

# Reading input from the input file
input_filename='input_sample0.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    input_str = f.readline().rstrip()
print(f'input string: {input_str}')



def test_input_processing():
    assert input_processing('1,2,3') == [49,44,50,44,51,17,31,73,47,23]

def test_get_dense_hash():
    assert get_dense_hash([65,27,9,1,4,3,40,50,91,7,6,0,2,5,68,22]) == [64]

def test_get_knox_hash_hex():
    assert get_knox_hash_hex([64, 7, 255]) == '4007ff'

def test_get_knox_hash_bin():
    assert get_knox_hash_bin('0') == '0000'
    assert get_knox_hash_bin('1') == '0001'
    assert get_knox_hash_bin('e') == '1110'
    assert get_knox_hash_bin('f') == '1111'
    assert get_knox_hash_bin('a0c20170') == '10100000110000100000000101110000'

