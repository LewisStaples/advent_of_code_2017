# adventOfCode 20xy day 9
# https://adventofcode.com/20xy/day/9


# Display data to user only if the data isn't too large
def conditional_data_display(label_str, data_str):
    # The length used below can be adjusted by the programmer
    if len(data_str) < 50:
        print(f'{label_str}: {data_str}')
    
def perform_cancels(in_string):
    # Handle canceled characters 
    # Within garbage any character after ! is ignored.
    # This will implemented by removing the ! and its subsequent character
    string_i = -1
    while True:
        string_i = in_string.find('<', string_i + 1)
        if string_i == -1:
            break
        while True:
            if in_string[string_i] in ['>', '!']:
                if in_string[string_i] == '>':
                    break
                # Remove two chars (the ! and the next one)
                in_string = in_string[:string_i] + in_string[string_i + 2:]
                string_i -= 1
            string_i += 1
    return in_string

def process_garbage(in_string):
    ret_str = ''
    ret_count = 0
    string_i = 0
    while string_i < len(in_string):
        if in_string[string_i] == '>':
            index_lt = in_string.index('<')
            ret_count += max((string_i - index_lt - 1), 0)
            in_string = in_string[:index_lt] + in_string[string_i + 1:]
            string_i -= (string_i - index_lt)
            
        string_i += 1
    
    ret_str += in_string
    return ret_str, ret_count

# This assumes that perform_cancels and process_garbage have already been run
def get_score(in_string):
    ret_val = 0
    string_i = 0
    brace_level = 0
    while string_i < len(in_string):
        if in_string[string_i] == '{':
            brace_level += 1
        elif in_string[string_i] == '}' and brace_level > 0:
            ret_val += brace_level
            brace_level -= 1
        string_i += 1
    return ret_val


def get_results(in_string):
    in_string = perform_cancels(in_string)
    conditional_data_display('After cancelling', in_string)

    in_string, garbage_count = process_garbage(in_string)
    conditional_data_display('After processing garbage', in_string)

    return get_score(in_string), garbage_count

# Reading input from the input file
input_filename='input_sample1.txt' # 'input_sample1.txt' is the input for part 2/B, whereas 'input_sample0.txt' is input for part 1/A
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        conditional_data_display('Input', in_string)
        the_results = get_results(in_string)

        print(f'\nThe total score is {the_results[0]}')
        print(f'The count of non-canceled characters within the garbage is {the_results[1]}\n\n')


def test_cancel():
    # Given samples
    assert perform_cancels('<{!>}>') == '<{}>'
    assert perform_cancels('<!!>') == '<>'
    assert perform_cancels('<!!!>>') == '<>'
    assert perform_cancels('<{o"i!a,<{i<a>') == '<{o"i,<{i<a>'

    # My own sample
    assert perform_cancels('!<!!!>>') == '!<>'

