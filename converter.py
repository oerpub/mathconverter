#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
import requests
import sys

input_formats = ['asciimath', 'latex', 'mathml']
output_formats = ['latex', 'mathml']


def mathml2latex_yarosh(equation):
    pass


def mathmlcloud2mathml(equation, iformat):
    #    resp = requests.post('https://api.mathmlcloud.org/equation',{'math': equation,'mathType':'TeX','mml':'true', 'svg':'true', 'png':'true', 'description':'true'})
    mathtype = 'TeX'
    if iformat == 'asciimath':
        mathtype = 'AsciiMath'
    elif iformat == 'mathml':
        mathtype = 'mml'
    try:
        resp = requests.post('https://api.mathmlcloud.org/equation',
                             {'math': equation, 'mathType': mathtype, 'mml': 'true', 'description': 'true'})
        print resp
        print resp.text
        print ''
        data = resp.json()
        mathml = data['components'][0]['source']
        return mathml
    except Exception, err:
        sys.stderr.write('CONVERT ERROR: %sn' % str(err))
        sys.exit(2)

@click.command()
@click.option('--equation', prompt='Equation', help='Equation to convert')
@click.option('--iformat', type=click.Choice(input_formats), prompt='Input Format', help='Equation input format')
@click.option('--oformat', type=click.Choice(output_formats), prompt='Output Format', help='Equation output format')
def convert(equation, iformat, oformat):
    if (iformat == oformat):
        print "Nothing to convert here. Input and output format are the same!"
        sys.exit(1)
    # click.echo('Equation %s' % equation)
    print ''
    print mathmlcloud2mathml('x*2', 'asciimath')

if __name__ == '__main__':
    convert()
