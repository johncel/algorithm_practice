W = 10

N = 4

v = [10, 40, 30, 50]
w = [5,   4,  6,  3]


def maximize_knapsack_value(W, v, w):
    max_value = 0
    max_value_key = ()

    max_value_lookup = {} 
    max_value_weight_lookup = {}

    def mkv_inner(i_remaining):
        # print(f'mkv_inner i_remaining: {i_remaining}')
        key = tuple(i_remaining)
        if key in max_value_lookup:
            return max_value_lookup[key], max_value_weight_lookup[key]

        total_weight = 0
        total_value = 0
        for i in i_remaining:
            total_weight += w[i]
        for i in i_remaining:
            total_value += v[i]

        if total_weight <= W:
            max_value_lookup[key] = total_value
            max_value_weight_lookup[key] = total_weight

            nonlocal max_value
            nonlocal max_value_key
            if total_value > max_value:
                max_value = total_value
                max_value_key = key

            return total_value, total_weight


        # print(f'i_remaining: {i_remaining}')
        for i in i_remaining:
            new_i_remaining = list(i_remaining)
            # print(f' before remove {new_i_remaining}')
            new_i_remaining.remove(i)
            # print(f' after remove {new_i_remaining}')
            mkv_inner(new_i_remaining)


    i_remaining = list(range(0, N))
    mkv_inner(i_remaining)

    return max_value, max_value_key


max_value, max_value_key = maximize_knapsack_value(W, v, w)

print(f'max_value: {max_value} max_value_key:{max_value_key}')
for i in max_value_key:
    print(f'item   value:{v[i]} weight:{w[i]}')
