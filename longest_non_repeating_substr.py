import random
import string

def random_string(string_length=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(string_length))

def find_longest_non_repeating_str(input_string):
    input_string_counts = {}
    longest_string = ''
    longest_string_candidate = ''

    for i, letter_start in enumerate(input_string):
        input_string_counts = {}
        longest_string_candidate = ''
        for j, letter_end in enumerate(input_string[i:]):
            if letter_end in input_string_counts: # we busted
                break

            longest_string_candidate += letter_end
            input_string_counts[letter_end] = 1

            print(f'longest_string_candidate: {longest_string_candidate}')
                
            if len(longest_string_candidate) >= len(longest_string):
                longest_string = longest_string_candidate

    return longest_string


print(f'str: {str}')
str = random_string(string_length=200)
longest_str = find_longest_non_repeating_str(str)
print(f'longest_str: {longest_str}')

