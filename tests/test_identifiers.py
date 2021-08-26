import pytest

@pytest.mark.parametrize('t,e', [
    ('a', "a"),
    ('_0', "_0"),
    ('max_span', "max_span"),
])
def test_number(scadparser, t, e):
    ast = scadparser.parse(t, start="identifier")
    assert str(ast) == e
