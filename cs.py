#!/usr/bin/python

# graph.py - Graph mathematical equations and functions

import matplotlib.pyplot as plt
import numpy as np
import click

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.option('-V'   , '--version'      , 'version'     , help='Show program version'           , is_flag=True, default=False)
@click.option('-v'   , '--verbose'      , 'verbose'     , help='Display verbose output'         , is_flag=True, default=False)
@click.argument('inp', metavar='<inp>', required=True)
@click.command(options_metavar='[options]', context_settings=CONTEXT_SETTINGS)
def cli(version, verbose, inp):
    if (version):
        MAJOR, MINOR, PATCH = '0', '1', '0'
        print(f'strmanip - v{MAJOR}.{MINOR}.{PATCH}')
        return

    # create 1000 equally spaced points between -10 and 10
    x = np.linspace(-10, 10, 1000)

    # calculate the y value for each element of the x vector
    fn = eval(inp)

    fig, ax = plt.subplots()
    ax.plot(x, fn)
    plt.show()


if __name__ == '__main__':
    cli()
