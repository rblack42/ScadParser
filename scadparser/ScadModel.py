from __future__ import annotations

import os
import tatsu
from tatsu.ast import AST

symbol_table = {}

def store(id, val):
    print(f"Store: {id}: {val}")
    if 'int' in val:
        v = int(val['int'])
    elif 'float' in val:
        v = float(val['float'])
    else:
        v = -1
    symbol_table[id] = v


def lookup(id):
    if not id in symbol_table:
        return id
    else:
        return symbol_table[id]


class ScadSemantics(object):

    def file_include(self, ast):
        print("Processing include file")
        print("CWD" + str(os.getcwd()))
        grammar = open('scadparser/scad.ebnf').read()
        incfile = os.path.join('scad', ast.file)
        prog = open(incfile).read()
        parser = tatsu.compile(grammar)
        ast = parser.parse(prog,
            trace=False, colorize=True, semantics=ScadSemantics())
        print("COmpleted processing include file")
        return ast

    def int(self, ast):
        return int(ast)

    def fract(self, ast):
        return float(ast)

    def identifier(self, ast):
        val = lookup(ast)
        if type(val) == str:
            val = 0
        print(f"LOOK: {ast} -> {val}")
        return lookup(ast)

    def declaration(self, ast):
        store(ast.id, ast.value)
        return ast

    def addition(self, ast):
        return ast.left + ast.right

    def subtraction(self, ast):
        return ast.left - ast.right

    def multiplication(self, ast):
        print(f"MUL: {ast.left} * {ast.right}")
        return ast.left * ast.right

    def division(self, ast):
        return ast.left / ast.right

    def number(self, ast):
        if 'int' in ast:
            return int(ast['int'])
        if 'float' in ast:
            return float(ast['float'])
        return ast


