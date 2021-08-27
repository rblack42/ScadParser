import tatsu
from pprint import pprint


def test():
    g = open('scadparser/ebnf/scad.ebnf').read()
    parser = tatsu.compile(g)
    code = open('scad/constraints.scad').read()
    ast = parser.parse(code, start='start')
    pprint(ast)

if __name__ == '__main__':
    test()
