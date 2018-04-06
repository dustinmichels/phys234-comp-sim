"""
Key function defintions from RW01.ipynb
Author(s): Dustin Michels
"""

import math
import itertools
import numpy as np
import matplotlib.pyplot as plt


def steps(n):
    """Return np.array with n "steps" (either +1 or -1)"""
    return 2 * np.random.randint(0, 2, n) - 1


def x_values(n):
    """Return list of positions at each of n steps"""
    return list(itertools.accumulate(steps(n)))


def plot_walk(n):
    """Plot position at each of n steps"""
    pos = [0] + x_values(n)  # add 0 to start of list
    t = np.arange(0, n+1)    # enumerate steps from 0 to n
    plt.plot(t, pos)
    plt.ylabel('x')
    plt.xlabel('steps')
    return plt
