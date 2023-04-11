Choose the scope_urls
=====================

``scope_urls`` is a mandatory attribute of parsers classes. It is essential to set it up correctly to make the library work as expected.

``scope_urls`` is used by the library to choose which parser to call to parse an URL.

When ``scrape`` function is called, it will select the parser that match the given URL.

Example
-------

In the `Github repository <parser-example_>`_, there are two parsers.

.. code-block:: python
    
    class BooksParser(BaseParser):

        scope_urls = [
            "https://books.toscrape.com",
            "https://books.toscrape.com/catalogue/category/book_1/index.html",
            "https://books.toscrape.com/catalogue/category/books/{category}/index.html",
        ]


The following URLs will be parsed by ``BooksParser``:

- ``https://books.toscrape.com/``
- ``https://books.toscrape.com/catalogue/category/book_1/index.html``
- any URL matching ``https://books.toscrape.com/catalogue/category/books/{category}/index.html`` like ``https://books.toscrape.com/catalogue/category/books/travel_2/index.html`` 

.. code-block:: python

    class BookParser(BaseParser):

        scope_urls = ["https://books.toscrape.com/catalogue/{book-name}/index.html"]

The following URLs will be parsed by ``BookParser``:

- any URL matching ``https://books.toscrape.com/catalogue/{book-name}/index.html`` like ``https://books.toscrape.com/catalogue/the-secret-garden_413/index.html``




.. _parser-example: https://github.com/Gamma120/minimal-web-scraper/blob/main/example/parser_example.py