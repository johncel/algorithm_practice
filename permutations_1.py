# word = ['s', 'a', 'l', 'y']
word = ['s', 'a', 'l', 'y', 's', 't', 'r']

selected = {}
perms = []

def factorial(n):
    if n == 2:
        return 2

    return n * factorial(n-1)

def word_depth_dive(word, whats_left, word_can, depth):
    print(f'depth {depth}')
    if len(whats_left) > 0:
        for i,letter in enumerate(whats_left):
            word_can[depth] = letter
            t_whats_left = list(whats_left[0:i])
            if i < len(whats_left) - 1:
                t_whats_left += whats_left[i+1:]
            print(f'work_can {word_can}')
            word_depth_dive(word, t_whats_left, list(word_can), depth+1)
    else:
        perms.append(word_can)
        return

word_can = list(word)
word_depth_dive(word, word, word_can, 0)

print(perms)
print(f'there are {len(perms)} permutations')
print(f'there should be {factorial(len(word))}')
