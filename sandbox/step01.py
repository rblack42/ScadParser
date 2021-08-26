import tatsu
from pprint import pprint


def test():
    g = open('scadparser/ebnf/scad01.ebnf').read()
    parser = tatsu.compile(g)
    ast = parser.parse('123')
    pprint(ast)

if __name__ == '__main__':
    test()
