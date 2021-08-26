TatSu Parser Development
########################

To generate a parser for the |OSC| language using TatSu_, we need to start off
by writing a language specification using a variation of EBNF_.

Here is our starting point:

..  literalinclude::    ../scadparser/ebnf/scad01.ebnf
    :linenos:
    :caption: scad.ebnf

Here, we define a name for the language *grammar*, and set up the geberated
parser to allow (and skip) C++ style comments. The only rule found in this
startup file defines an integer number as a sequence of digits, possibly
allowing for an exponent using the scientific stype notation. The pattenr shown
here is a standard one using *regular expressions* in |PY|.

..  note::

    In order to assist in producing this documentation, I am numbering versions
    of the ebnf- we produce and use in tests. In normal application
    development, we simple add lines to a single 88scad.ebnf fle and ditch the
    numbers.

Here is a simple test showing how we use this grammar and generate a parser for our extremely simple language:

..  literalinclude::    ../sandbox/step01.py
    :linenos:
    :caption:   sandbox/step01.py

..  note::

    I created a **sandbox** directory in this project just for simple tests

Let's run this and see what we get:

..  command-output:: python sandbox/step01.py
    :cwd: ../

The output of this run is a simple string, which is the "code" we passed to the
parser. Looks like it worked.

PyTest Testing
**************

With a working parser, we really should test it more extensively. For that, we
will use PyTest_.

Here is a test that uses a feature of PyTest_ that **parametrizes** (yes it is
misspelled) a test. Also, I created a **scad.ebnf** file which will be our real
|OSC| language specification.

..  literalinclude::    ../tests/test_integers.py
    :linenos:
    :caption: tests/test_integers.py

In this test, the **t** and **e** parameters mean "string to test", and
"expected result" respectively. PyTest_ uses the list of string pairs to run
the test multiple times, once for each pair. This let's you create several
tests in a simple way. The **start** parameter tells the parser what rule in
the specification grammar to use to begin processing.

This test also relies on a setup file that creates a parser for each test:

..  literalinclude::    ../tests/conftest.py
    :linenos:
    :caption: tests/conftest.py

The parser is passed to the test function as the first parameter.



Let's see if this works:

.. command-output::    pytest tests/test_integers.py
    :cwd:   ../

Now, we have a much better testing setup, which we will use as we proceed

Adding Real Numbers
*******************

Now that we can process integers, let's add a rul that accepts real numbers as
well. This one is similar to the 8integer8 rule, bu it allows a decimal point;

..  literalinclude::    ../scadparser/ebnf/scad02.ebnf
    :linenos:
    :caption:   scadparser/ebnf/scad02.ebnf

Instead of building another test code, we will just add a new test:

..  literalinclude::    ../tests/test_reals.py
    :linenos:
    :caption: tests/test_reals.py

Now we can run this test as well:

..  command-output::    pytest tests/test_reals.py
    :cwd:   ../

Looks like we are making progress.

..  note::

    In normal development, running pytest will run all tests found in the
    **test** directory. I am limiting the test run to just a sngle test for
    this documentation.

Identifiers
***********

We will be naming things in our design work, and |OSC| has some rules on names.

..  literalinclude::    ../scadparser/ebnf/scad.ebnf
    :lines: 15-18

This new rule allows names that start with a dollar sign, but those names are reserved for internal work by |OSC|. Some strange names are allowed as well, as we will see in our next test code:

..  literalinclude::    ../tests/test_identifiers.py
    :linenos:
    :caption: tests/test_identifiers.py

I am going to omit the test run (it works!)


w that we have a start on our parser, let's move on to something more interesting: *expressions*!

