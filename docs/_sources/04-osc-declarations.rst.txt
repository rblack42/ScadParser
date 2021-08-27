|OSC| Declarations
##################

Our first real job in building something that will help in analyzing a model
design is to teach our parser to handle |OSC| variable declarations. These have
a simple form:

..	code-block:: text

	name = value ;

The rule that provides this new grammar form is simple  as well:

..	literalinclude::	../scadparser/ebnf/scad.ebnf
	:lines: 67-73
	:caption: scadparser/ebnf/scad.ebnf

There is a new notation in this rule. The **~** symbol tells TatSu_ to continue
processing this rule from this point on, even if it fails. This just helps
speed up parsing by eliminating additional tests to find alternatives that
might work. Once we see that *equal* sign, we know this should be a
*declaration* and we are telling TatSu_ that here.

Once again, the parser will be building a |PY| dictionary for this part of the
**AST**. Our tests need to check these dictionary strings, as we did for
*expressions*

..	literalinclude::	../tests/test_declarations.py
	:linenos:
	:caption:	tests/test_declarations.py

Obviously, we could have a more complex *expression* on the right hand side of the equal sign, but we have already tested that.

Parsing a Real |OSC| File
*************************

We have almost enough to begin processing real |OSC| code files. To to that we
need a top-level rule that begins our parsing. Traditionally, this rule is
named **start** and it is placed at the top of our EBNF_ file.

..	literalinclude::	../scadparser/ebnf/scad.ebnf
	:lines: 67-73
	:caption: scadparser/ebnf/scad.ebnf

There are a few more rules here, which will be needed in our next section.

Here is a piece of code that will read a real |OSC| data file and parse the
contents.

.. literalinclude::    ../sandbox/step02.py
   :linenos:
   :caption:   sandbox/step02.py

Here is our test |OSC| file:

.. literalinclude::    ../scad/constraints.scad
   :linenos:
   :caption:   scad/constraints.scad

And, this is the result of running that code:

..  command-output::    python sandbox/step02.py
    :cwd: ../

The final output is a list of the declarations found in the
**constraints.scad** data file.
