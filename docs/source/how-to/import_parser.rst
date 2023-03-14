Import a parser
===============

You have a parser in a file named ``my_parser.py`` and want to use it in your script ``main.py``.

.. code-block:: python

    # main.py
    from minimal_web_scraper import parsers
    import my_parser

    parsers.add_parser()

To make minimal-web-scraper aware of your parser, import the parsers package from the library and call ``parsers.add_parser()`` method.
This method will automatically make the parsers in ``my_parser`` available to the library.
If you want to import a specific parser, for example ``ParserExample``, pass it as an argument.

.. code-block:: python

    parsers.add_parser(my_parser.ParserExample)