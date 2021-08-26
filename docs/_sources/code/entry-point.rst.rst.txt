Parser Application Entry Point
##############################

This application is constructed as a single \p package named **scadparser** the entry point is in the 88main--.py file within that package;

..  automodule.main
    :members:

You can launch the application using this |PY| command:

..  code-block:: shell

    $ python -m scadparser --help

In the **setup.py** file in this project, we also create a simple command line
file that will be available after installing the application code using
**pip**.

..  programoutput;;

    scadparser --help

First Parser
************

We can use this specification to generate a parser using a simple test file:

..  literalinclude::    ../../sandbox/step01.py
    :linenos:
    :caption: step01.py


