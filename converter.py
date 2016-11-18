#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click

math_formats = ['asciimath', 'latex', 'mathml']


@click.command()
@click.option('--equation', prompt='Equation', help='Equation to convert')
@click.option('--iformat', type=click.Choice(math_formats), prompt='Input Format', help='Equation input format')
@click.option('--oformat', type=click.Choice(math_formats), prompt='Output Format', help='Equation output format')
def convert(equation, iformat, oformat):
    click.echo('Equation %s!' % equation)

if __name__ == '__main__':
    convert()
