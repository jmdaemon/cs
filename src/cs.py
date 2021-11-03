#!/usr/bin/python

# graph.py - Graph mathematical equations and functions

import matplotlib.pyplot as plt
import math
import numpy as np
import argparse
# import click
# import argh


# CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

# @click.option('-V'   , '--version'      , 'version'     , help='Show program version'           , is_flag=True, default=False)
# @click.option('-v'   , '--verbose'      , 'verbose'     , help='Display verbose output'         , is_flag=True, default=False)
# @click.argument('inp', metavar='<inp>', required=True)
# @click.command(options_metavar='[options]', context_settings=CONTEXT_SETTINGS)
# def cli(version, verbose, inp):
# def main(inp, beg=-10, end=10, n=1000, version=False, verbose=False):
def main():
    parser = argparse.ArgumentParser(description='Executable file for Labs')
    parser.add_argument('input' , type=str, help='File path to some input.csv')
    parser.add_argument('range' , type=tuple, help='File path to some input.csv')
    parser.add_argument('n'   , type=int, help='File path to some input.csv')

    args = parser.parse_args()

    inp         = args.input
    beg, end    = args.range
    n           = args.n

    # if (version):
        # MAJOR, MINOR, PATCH = '0', '0', '1'
        # print(f'strmanip - v{MAJOR}.{MINOR}.{PATCH}')
        # return

    # create 1000 equally spaced points between -10 and 10
    # x = np.linspace(-10, 10, 1000)
    x = np.linspace(beg, end, n)

    # calculate the y value for each element of the x vector
    fn = eval(inp)
    # fn = exec(inp)

    fig, ax = plt.subplots()
    ax.plot(x, fn)
    plt.show()


# if __name__ == '__main__':
    # cli()

# argh.dispatch_command(main)
