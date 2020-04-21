import random
import string

def random_string(string_length=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(string_length))

def check_palindrome(input_string):
    # print(f'input_string: {input_string}')
    for i in range(0, int(len(input_string)/2)):
        # print(f'comparing {input_string[i]} and {input_string[-(i + 1)]}')
        if input_string[i] != input_string[-(i+1)]:
            # print(f'FALSE')
            return False

    # print(f'TRUE')
    return True 

def find_longest_palindrome_str(input_string):
    input_string_counts = {}
    longest_string = ''
    longest_string_candidate = ''

    for i, letter_start in enumerate(input_string):
        longest_string_candidate = ''
        left_index = i
        right_index = i
        while left_index >= 0 and right_index < len(input_string):
            longest_string_candidate = input_string[left_index: right_index + 1]
            if check_palindrome(longest_string_candidate):
                # print(f'longest_string_candidate: {longest_string_candidate}')
                if len(longest_string_candidate) > len(longest_string):
                    longest_string = longest_string_candidate 
            else:
                break

            left_index-=1
            right_index+=1

        # special case for even length strings with double middle letter
        if i < len(input_string) - 1 and input_string[i] == input_string[i+1]:
            longest_string_candidate = ''
            left_index = i
            right_index = i + 1
            while left_index >= 0 and right_index < len(input_string):
                longest_string_candidate = input_string[left_index: right_index + 1]
                if check_palindrome(longest_string_candidate):
                    # print(f'longest_string_candidate: {longest_string_candidate}')
                    if len(longest_string_candidate) > len(longest_string):
                        longest_string = longest_string_candidate 
                else:
                    break
    
                left_index-=1
                right_index+=1

            
    return longest_string


str = random_string(string_length=20000)
# print(f'str: {str}')
longest_str = find_longest_palindrome_str(str)
print(f'longest_str: {longest_str}')

