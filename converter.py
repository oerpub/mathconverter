#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
import sys

input_formats = ['asciimath', 'latex', 'mathml']
output_formats = ['latex', 'mathml']

@click.command()
@click.option('--equation', prompt='Equation', help='Equation to convert')
@click.option('--iformat', type=click.Choice(input_formats), prompt='Input Format', help='Equation input format')
@click.option('--oformat', type=click.Choice(output_formats), prompt='Output Format', help='Equation output format')
def convert(equation, iformat, oformat):
    if (iformat == oformat):
        print "Nothing to convert here. Input and output format are the same!"
        sys.exit(1)
    click.echo('Equation %s!' % equation)

if __name__ == '__main__':
    convert()
