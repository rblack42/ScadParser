import tatsu
from pprint import pprint
from scadparser.ScadSemantics import ScadSemantics

def test():
    g = open('scadparser/ebnf/scad.ebnf').read()
    parser = tatsu.compile(g)
    code = open('scad/model.scad').read()
    ast = parser.parse(code, start='start', semantics=ScadSemantics())
    pprint(ast)

if __name__ == '__main__':
    test()
