from random import random
# import itertools
# import time
import numpy as np
# import networkx as nx
import matplotlib.pyplot as plt

def beta(x, a, b):
    return x**(a - 1) * (1 - x)**(b - 1)

def update_beta(a, b, samples):
    a = a + sum(samples)
    b = b + len(samples) - sum(samples)

    return a, b

def plot_beta(a, b, lw=1):
    # x**(a - 1) * (1 - x)**(b - 1)
    dx = 0.01
    X = np.arange(0, 1, dx)
    y = [beta(x, a, b) for x in X]
    print(y)
    line, = plt.plot(X, y / sum(y), lw=lw)

beta_a = 2.0
beta_b = 2.0

plot_beta(beta_a, beta_b)

# sample some stuff
N = 1000
samples = [random() * 0.5 + 0.25 for n in range(0,N)]
print(f'samples: {samples}')
# samples = [0.5 for n in range(0,N)]

beta_a, beta_b = update_beta(beta_a, beta_b, samples)

plot_beta(beta_a, beta_b, lw=2)

plt.show()
