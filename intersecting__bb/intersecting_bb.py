from random import random
# import itertools
# import time
import numpy as np
# import networkx as nx
# import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection


def random_rect():
    x_left = random()
    x_right = x_left + random()
    y_top = random()
    y_bottom = y_top + random()

    return [(x_left, y_top), (x_right, y_top), (x_right, y_bottom), (x_left, y_bottom)]

def draw_rect(patches, rect):
    poly = np.array(rect)
    polygon = Polygon(poly, True)
    patches.append(polygon)
    

fig, ax = plt.subplots()
patches = []
num_polygons = 2
num_sides = 4

rects = []
rects.append(random_rect())
rects.append(random_rect())

draw_rect(patches, rects[0])
draw_rect(patches, rects[1])

# determine if they intersect

num_left = 0
num_right = 0
num_above = 0
num_below = 0
for vertex_0 in rects[0]:
    for vertex_1 in rects[1]:
        if vertex_0[0] < vertex_1[0]:
            num_left = num_left + 1
        else:
            num_right = num_right + 1
        if vertex_0[1] < vertex_1[1]:
            num_below = num_below + 1
        else:
            num_above = num_above + 1
    
print(f' num_left: {num_left} num_right:{num_right}')
print(f' num_above: {num_above} num_below:{num_below}')

if num_left == 0 or num_right == 0 or num_above == 0 or num_below == 0:
    print(f' no intersection')
else:
    print(f' YES intersection')

p = PatchCollection(patches, cmap=matplotlib.cm.jet, alpha=0.4)

colors = 100*np.random.rand(len(patches))
p.set_array(np.array(colors))

ax.add_collection(p)

plt.show()
