import pytest

@pytest.mark.parametrize('t,e', [
    ('-123.4', "{'float': '-123.4'}"),
    ('123', "{'int': '123'}")
])
def test_number(scadparser, t, e):
    ast = scadparser.parse(t, start="number")
    assert str(ast) == e

@pytest.mark.parametrize('t,e', [
    ('abcd', "{'id': 'abcd'}"),
    ('_abcd', "{'id': '_abcd'}"),
    ('_abcd11', "{'id': '_abcd11'}"),
    ('_0', "{'id': '_0'}"),
])
def test_identifiers(scadparser, t, e):
    ast = scadparser.parse(t, start="identifier")
    assert str(ast) == e

@pytest.mark.parametrize('t,e', [
    ('include <../test.scad>', "{'file': '../test.scad'}"),
])
def test_includes(scadparser, t, e):
    ast = scadparser.parse(t, start="include")
    assert str(ast) == e
