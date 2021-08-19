ScadParser (v0.1.1)
####################
:Author:    Roie R. Black
:Email: roie.black@gmail.com
:Docs:      https://rblack42.github.io/ScadParser

..  start-badges

.. list-table::
    :stub-columns: 1

    * - tests
      - | |github| |travis| |appveyor| |coverage|

    * - package
      - | |version| |wheel| |supported-versions| |commits-since| |status|



.. |github| image:: https://github.com/rblack42/Rscadparser/actions/workflows/python-app.yml/badge.svg
    :alt: Github Workflows
    :target: https://github.com/rblack42/ScadParser

.. |travis| image:: https://travis-ci.com/rblack42/RScadParser.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.com/rblack42/math-magik

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/pevivsa6n5adw5lw?svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/rblack42/ScadParser


.. |coverage| image:: https://coveralls.io/repos/github/rblack42/ScadParser/badge.svg?branch=master
    :target: https://coveralls.io/github/rblack42/ScadParser?branch=master
    :alt: Code Coverage"

.. |requires| image:: https://requires.io/github/rblack42/ScadParser/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/rblack42/ScadParser/requirements/?branch=master

.. |version| image:: https://img.shields.io/pypi/v/scadparser.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/scadparser

.. |wheel| image:: https://img.shields.io/pypi/wheel/scadparser.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/scadparser

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/Rscadparser.svg
    :alt: Supported versions
    :target: https://pypi.org/project/scadparser

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/scadparser.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/scadparser

.. |status| image:: https://img.shields.io/pypi/status/scadparser
    :alt: development status
    :target: https://pypi.org/project/scadparser

.. |commits-since| image:: https://img.shields.io/github/commits-since/rblack42/ScadParser/v0.1.1.svg
    :alt: Commits since latest release
    :target: https://github.com/rblack42/ScadParser/compare/v0.1.1...master
.. end-badges

This project supports the *Math-Magik* project which uses *OpenSCAD* to design
model airplanes. The purpose of the parser developed here is to process the
*OpenSCAD* design files in order to facilitate performing an analysis on the
proposed design. Specifically, that processing seeks to predict the estimated
weight and center of gravity of the model, two parameters that are important in
getting a model to actually fly!

The initial goal of this project is not necessarily to be a complete parser for
all kinds of *OpenSCAD* code. Rather, it focuses on the kind of code used in
*Math-Magik* projects.

More details on the parent project can be found at
https://rblack42.github.io/math-magik

If you are interested in assisting with the development of this project, or
need help with anything found here, please contact me by email. I welcome
questions and ideas for extending this project.





