Create a parser
===============

The most common way is to create a file dedicated to the parser or parsers.

Here is the skeleton of a parser compatible with the library:

.. code-block:: python
    
    from minimal_web_scraper import BaseParser

    class ExampleParser(BaseParser):
        scope_url = ""

        @classmethod
        def parse(cls, html_content, encoding):
            return []

- The parser **must** inherit from the ``BaseParser`` class from the library.
- It **must** contain ``scope_url`` variable and a ``parse`` method.
- ``parse`` method **must** be a ``@classmethod`` and return a list of dictionary elements.

The recommended tools to write the ``parse`` method are the ``BeautifulSoup`` and ``re`` libraries.
But any library parsing HTML formatted string could be used.


To see working parsers, check out the `Github repository <parser-example_>`_.

.. _parser-example: https://github.com/Gamma120/minimal-web-scraper/blob/main/example/parser_example.py
