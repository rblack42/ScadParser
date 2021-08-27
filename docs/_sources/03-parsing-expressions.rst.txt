Parsing Expressions
###################

So fat, the rules we have set up just define basic *tokens*. We have not
created any rules the control how those tokens can be arranged. Parsing
mathematical expressions is going to cure that!

Here is a rule set that defines an *expression*

..	literalinclude::	../scadparser/ebnf/scad.ebnf
	:lines:	28-67
	:caption:	scadparser/ebnf/scad.ebnf

This set of rules shows some new features of TatSu_. The **left:expression**
notation will cause TatSu_ to generate something called an |AST| which the
parser is building as it parses. Basically, this *AST* details the rules
followed to either accept or reject the input chink of code we process.

There is one more rule in this set, one that is important:

..	literalinclude::	../scadparser/ebnf/scad.ebnf
	:lines:	17-21
	:caption:	scadparser/ebnf/scad.ebnf

The order of these options is important. We need to try tp process a *real*
number first, so parsing captures the decimal point. If we tried the *integer*
option first, the leading **1** would be accepted and the rest would not be
recognized as a valid construct.

For our expression testing, all we need to know is that TatSu_ is going to
produce a |PY| dictionary showing the expression structure. Standard things
like operator precedence are handled by these rules.

..  literalinclude:: ../tests/test_expressions.py
    :linenos:
    :caption: tests/test_expressions.py

This test is complicated by the need to specify the |PY| dictionary the parser
will produce.


