#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
import os
import requests
import sys
from lxml import etree

input_formats = ['asciimath', 'latex', 'mathml']
output_formats = ['latex', 'mathml']


def mathml2latex_yarosh(equation):
    """ MathML to LaTeX conversion with XSLT from Vasil Yaroshevich """
    script_base_path = os.path.dirname(os.path.realpath(__file__))
    xslt_file = os.path.join(script_base_path, 'xsl_yarosh', 'mmltex.xsl')
    dom = etree.fromstring(equation)
    xslt = etree.parse(xslt_file)
    transform = etree.XSLT(xslt)
    newdom = transform(dom)
    return unicode(newdom)


def _call_mathml_cloud(equation, mathtype):
    """ the HTTP POST to MathMLCloud server """
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


def asciilatex2mathml_cloud(equation, iformat):
    """ Get MathML from MathMLCloud converter """
    #    resp = requests.post('https://api.mathmlcloud.org/equation',{'math': equation,'mathType':'TeX','mml':'true', 'svg':'true', 'png':'true', 'description':'true'})
    if iformat == 'asciimath':
        mathtype = 'AsciiMath'
    else:   # LaTeX
        mathtype = 'TeX'
    if iformat == 'mathml':
        sys.stderr.write('ERROR: unexpected mathml usage. Should not happen')
        sys.exit(3)
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
    result = 'Error: No result. Should not happen.'
    if (oformat == 'mathml'):
        result = asciilatex2mathml_cloud(equation, iformat)
    else:   # LaTeX
        if (iformat == 'mathml'):
            result = mathml2latex_yarosh(equation)
        else:  # AsciiMath
            mathml = asciilatex2mathml_cloud(equation, iformat)
            result = mathml2latex_yarosh(mathml)
    click.echo(result)


if __name__ == '__main__':
    convert()
