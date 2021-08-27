import pytest
import tatsu


@pytest.mark.parametrize('t, e', [
    ('include <constraints.scad>', "{'file': 'constraints.scad'}"),
])
def test_includes(scadparser, t, e):
    ast = scadparser.parse(t, start='fileinclude')
    assert str(ast) == e

