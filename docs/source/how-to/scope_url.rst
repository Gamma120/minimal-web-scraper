Choose the scope_url
====================

``scope_url`` is a mandatory attribut of parsers classes. It is essential to set it up correctly to make the library work as expected.


``scope_url`` is used by the library to choose which parser to call to parse an url.

When ``scrape`` function is called, it will select the parser that match the given url.

Example
-------

In the `Github repository <parser-example_>`_, there are two parsers.

- ``BooksParser`` is a parser with a ``scope_url`` books.toscrape.com/
- ``BookParser`` is a parser with a ``scope_url`` books.toscrape.com/catalogue/

So:

- ``scrape("https://books.toscrape.com/")`` will call ``BooksParser`` to parse
- ``scrape("https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html")`` will call ``BookParser`` to parse
- ``scrape("https://books.toscrape.com/catalogue/category/books/humor_30/index.html")`` will call... ``BookParser``, oh... ``BooksParser`` should be the answer. It's a **bug** and I will rework this. 

.. _parser-example: https://github.com/Gamma120/minimal-web-scraper/blob/main/example/parser_example.py