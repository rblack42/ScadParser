import pytest

@pytest.mark.parametrize('t,e', [
    ('123', "123"),
    ('-123', "-123"),
    ('123e02', "123e02"),
    ('123e-2', "123e-2")
])
def test_number(scadparser, t, e):
    ast = scadparser.parse(t, start="integer")
    assert str(ast) == e
