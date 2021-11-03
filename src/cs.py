import argparse
import math
import matplotlib.pyplot as plt
import numpy as np

# cs.py - Graph mathematical equations and functions

def main():
    parser = argparse.ArgumentParser(description='Executable file for Labs')
    parser.add_argument('input' , type=str, help='File path to some input.csv')
    parser.add_argument('range' , type=tuple, help='File path to some input.csv')
    parser.add_argument('n'   , type=int, help='File path to some input.csv')

    args = parser.parse_args()

    inp         = args.input
    beg, end    = args.range
    n           = args.n

    x = np.linspace(beg, end, n)

    fn = eval(inp)

    fig, ax = plt.subplots()
    ax.plot(x, fn)
    plt.show()
