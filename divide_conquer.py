from random import random
import itertools
import time
# import numpy as np
# import networkx as nx
# import matplotlib.pyplot as plt

def find_closest_pair(P):
    P.sort()
    print(f'P:{P}')

    def _fcp(P):
        n = len(P)
        mid_point = int(n/2)
        mid_point_val = P[mid_point]
        # print(f'P:{P}')
        if n < 3:
            min_dist = abs(P[1] - P[0])
            for pair in list(itertools.permutations(P)):
                if pair[0] == pair[1]:
                    continue
                # print(f'lookin at pair: {pair}')
                min_dist = min(abs(pair[0] - pair[1]), min_dist)
            return min_dist
        min_dist_l = _fcp(P[0:mid_point])
        min_dist_r = _fcp(P[mid_point:])

        d = min(min_dist_l, min_dist_r)
        print(f'min_dist before strip: {d}')
        i = mid_point
        strip = []
        while i >= 0:
            if abs(P[i] - mid_point_val) < d:
                strip.append(P[i])
            else:
                break
            i = i - 1
        i = mid_point
        while i < n:
            if abs(P[i] - mid_point_val) < d:
                strip.append(P[i])
            else:
                break
            i = i + 1

        min_dist = d
        for pair in list(itertools.permutations(strip)):
            if pair[0] == pair[1]:
                continue
            # print(f'lookin at pair: {pair}')
            min_dist = min(abs(pair[0] - pair[1]), min_dist)
        print(f'min_dist after strip: {min_dist} strip:{strip}')
        if min_dist != d:
            print(f'WE ALL MUST STRIP')
        return min_dist
            
    # print(f'P:{P}')

    return _fcp(P)


# P = (np.random.rand(1024)*10000000).astype(int)
P = []
for i in range(0, 1024):
    P.append(int(random()*10000000))


min_dist = find_closest_pair(P)

print(f'min_dist: {min_dist}')



