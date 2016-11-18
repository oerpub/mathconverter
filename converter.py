#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
import requests
import sys

input_formats = ['asciimath', 'latex', 'mathml']
output_formats = ['latex', 'mathml']


def mathml2latex_yarosh(equation):
    pass


def _call_mathml_cloud(equation, mathtype):
    try:
        resp = requests.post('https://api.mathmlcloud.org/equation',
                             {'math': equation, 'mathType': mathtype, 'mml': 'true', 'description': 'true'})
        data = resp.json()
        try:
            mathml = data['components'][0]['source']
            return mathml
        except IndexError:
            # bug in MathML Cloud. It sometimes returns 200 but no result
            # (bummer).
            return 'null'
    except Exception, err:
        sys.stderr.write('MathML Cloud ERROR: %sn' % str(err))
        sys.exit(2)


def mathmlcloud2mathml(equation, iformat):
    #    resp = requests.post('https://api.mathmlcloud.org/equation',{'math': equation,'mathType':'TeX','mml':'true', 'svg':'true', 'png':'true', 'description':'true'})
    mathtype = 'TeX'
    if iformat == 'asciimath':
        mathtype = 'AsciiMath'
    elif iformat == 'mathml':
        mathtype = 'mml'
    # try x times to get MathML cloud result:
    for i in range(1, 5):
        # print "Attempt calling MathML Cloud Server: {}".format(i)
        mathml = _call_mathml_cloud(equation, mathtype)
        if mathml != 'null':
            break
    if mathml == 'null':
        sys.stderr.write('ERROR: MathML Cloud Server does not give a result.')
        sys.exit(2)
    return mathml


@click.command()
@click.option('--equation', prompt='Equation', help='Equation to convert')
@click.option('--iformat', type=click.Choice(input_formats), prompt='Input Format', help='Equation input format')
@click.option('--oformat', type=click.Choice(output_formats), prompt='Output Format', help='Equation output format')
def convert(equation, iformat, oformat):
    print
    if (iformat == oformat):
        sys.stderr.write(
            'Nothing to convert here. Input and output format are the same!')
        sys.exit(1)
    if (oformat == 'mathml'):
        result = mathmlcloud2mathml(equation, iformat)
        click.echo(result)
    else:
        print "t.b.a."


if __name__ == '__main__':
    convert()
