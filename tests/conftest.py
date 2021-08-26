import pytest
import sys
import tatsu

GRAMMAR = "scadparser/ebnf/scad.ebnf"


@pytest.fixture(scope="function")
def scadparser():
    g = None
    try:
        f = open(GRAMMAR)
    except IOError:
        print("Grammar file cannot be opened:", GRAMMAR)
        sys.exit(1)
    else:
        with f:
            g = f.read()
    model = tatsu.compile(g)
    yield model

