import pytest

@pytest.mark.parametrize('t,e', [
    ('123.45', "123.45"),
    ('-123.0', "-123.0"),
    ('123.45e02', "123.45e02"),
    ('123.0e-2', "123.0e-2")
])
def test_reals(scadparser, t, e):
    ast = scadparser.parse(t, start="real")
    assert str(ast) == e
