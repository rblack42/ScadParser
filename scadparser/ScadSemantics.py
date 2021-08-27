import os
import tatsu

class ScadSemantics(object):

    def fileinclude(self, ast):
        g = open('scadparser/ebnf/scad.ebnf').read()
        incfile = os.path.join('scad', ast.file)
        prog = open(incfile).read()
        parser = tatsu.compile(g)
        ast = parser.parse(prog,
            start='start', semantics=ScadSemantics())
        return ast
