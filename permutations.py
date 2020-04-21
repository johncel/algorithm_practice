word = ['s', 'a', 'l', 'y']

selected = {}
perms = []

def word_depth_dive(word, word_can, depth):
    print(f'depth {depth}')
    if depth < len(word):
        for letter in range(0, len(word)):
            if letter not in word_can[0:depth]:
                word_can[depth] = letter
                print(f'work_can {word_can}')
                word_depth_dive(word, list(word_can), depth+1)
    if depth == len(word):
        # sorted_word = list(word)
        # sorted_word_can = list(word_can)
        # sorted_word.sort()
        # sorted_word_can.sort()
        # print(f'adding perm {word_can} word.sort():{sorted_word} word_can.sort():{sorted_word_can}')
        # if sorted_word == sorted_word_can:
        #     perms.append(word_can)
        new_word = list(word)
        for i in range(0, len(word)):
            letter = word_can[i]
            new_word[i] = word[letter]
        perms.append(new_word)
        return

word_can  = [x for x in range(0, len(word))]
word_depth_dive(word, word_can, 0)

print(perms)
print(f'there are {len(perms)} permutations')
