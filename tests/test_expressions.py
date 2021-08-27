import pytest
import tatsu


@pytest.mark.parametrize('t, e', [
    ('1+2', "{'left': {'int': '1'}, 'op': '+', 'right': {'int': '2'}}"),
    ('1*2', "{'left': {'int': '1'}, 'op': '*', 'right': {'int': '2'}}"),
    ('1.0+2*3', "{'left': {'float': '1.0'}, 'op': '+', 'right': {'left': {'int': '2'}, 'op': '*', 'right': {'int': '3'}}}")
])
def test_expressions(scadparser, t, e):
    ast = scadparser.parse(t, start='expression')
    assert str(ast) == e

