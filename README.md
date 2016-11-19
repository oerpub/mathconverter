#Converter for AsciiMath, LaTeX & MathML equations

Converts from AsciiMath, LaTeX, MathML to LaTeX, MathML

utilizes MathMLCloud (for MathML output) and XSL transforms (for LaTeX output).

(Optional):
```
virtualenv env
. env/bin/activate
```

Install:
```
pip install -r requirements.txt
```

## Usage:

```
./converter.py --help
```

### Example

```
$ ./converter.py --equation "x^2" --iformat asciimath --oformat mathml

<math xmlns="http://www.w3.org/1998/Math/MathML" alttext="x squared">
  <mstyle displaystyle="true">
    <msup>
      <mi>x</mi>
      <mn>2</mn>
    </msup>
  </mstyle>
</math>
```

### Background information

* `xsl_yarosh` by [Vasil Yaroshevich](http://www.raleigh.ru/MathML/mmltex/). Contains XSLT 1 transformation from MathML to LaTeX
* `xsl_transpect` by [transpect.io](https://github.com/transpect/mml2tex). Contains XSLT 2 transformations from MathML to LaTeX (not used currently)