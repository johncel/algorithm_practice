def reverse_string(the_str):
    if len(the_str) == 1:
        return the_str

    return the_str[-1] + reverse_string(the_str[:-1])


the_str = 'sally'
orig_str = str(the_str)
reverse_str = reverse_string(the_str)

print(f'orig_str: {orig_str} the_str:{the_str} reverse_str:{reverse_str}')

