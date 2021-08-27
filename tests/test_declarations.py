import pytest
import tatsu


@pytest.mark.parametrize('t, e', [
    ('A = 2;', "{'id': 'A', 'value': {'int': '2'}}"),
    ('A = B;', "{'id': 'A', 'value': 'B'}"),
])
def test_declarations(scadparser, t, e):
    ast = scadparser.parse(t, start='declaration')
    assert str(ast) == e

