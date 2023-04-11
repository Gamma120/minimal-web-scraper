minimal-web-scraper
===================

Objectif
--------

This example project scrapes informations from this website: https://books.toscrape.com/.
We want to collect the name of the products on that site, their price and availability to display them in a table.

The project name for this example is ``my_first_scraper``, feel free to replace this by your own project name.

.. note::

    This tutorial will not explain how to use BeautifulSoup, see `BeautifulSoup documentation <https://beautiful-soup-4.readthedocs.io/en/latest/#making-the-soup>`_.

Parsers
-------

The file ``parser_example.py`` hosts the code of our parsers.

The purpose of this function is to grab the informations we want from the page and to pack it in a dictionary we can easily manipulate.

This is the minimal required in a parser from the library.

.. code-block:: python

    from minimal_web_scraper.parsers import BaseParser

    class Parser(BaseParser):
        scope_urls = []

        @classmethod
        def parse(cls, html_content, encoding):
            return []


In our case, the parser parses the data from https://books.toscrape.com/, so it is our ``scope_urls``.

.. code-block:: python
    :emphasize-lines: 4

    from minimal_web_scraper.parsers import BaseParser

    class Parser(BaseParser):
        scope_urls = ["https://books.toscrape.com"] 

        @classmethod
        def parse(cls, html_content, encoding):
            return []

The ``parser`` method receives a ``html_content`` as an argument. It is the text file that contains the informations we want to extract.
To easily navigate in this file, we use the secrets ingredients: `BeautifulSoup <bs4_>`_ and `re <https://docs.python.org/3/library/re.html>`_.
It will do most of the work for us.

.. code-block:: python
    :emphasize-lines: 1,2,11

    from bs4 import BeautifulSoup
    import re

    from minimal_web_scraper.parsers import BaseParser

    class Parser(BaseParser):
        scope_urls = ["https://books.toscrape.com"]

        @classmethod
        def parse(cls, html_content, encoding):
            soup = BeautifulSoup(html_content, "html.parser", from_encoding=encoding)
            return []

The page https://books.toscrape.com/ contains multiple books. BeautifulSoup give us a list ``books``.
Each element ``book`` of this list contains informations on one book. In a ``for loop``, we create a dictionary ``item`` that contains the informations we want to return.

.. code-block:: python
    :emphasize-lines: 11,13-25

    from bs4 import BeautifulSoup
    import re

    from minimal_web_scraper.parsers import BaseParser

    class Parser(BaseParser):
        scope_urls = ["https://books.toscrape.com"] 

        @classmethod
        def parse(cls, html_content, encoding):
            scraped_items = []
            soup = BeautifulSoup(html_content, "html.parser", from_encoding=encoding)
            books = soup.find_all("article", class_="product_pod")

            for book in books:
                item = {
                    "name": None,
                    "url": None,
                    "availability": None,
                    "img_url": None,
                    "price": None,
                }
                scraped_items.append(item)

            return scraped_items


We extract the informations we want.

.. code-block:: python
    :emphasize-lines: 7,24-28

    from bs4 import BeautifulSoup
    import re

    from minimal_web_scraper.parsers import BaseParser

    class Parser(BaseParser):
        base_url = "https://books.toscrape.com/"
        scope_urls = ["https://books.toscrape.com"] 

        @classmethod
        def parse(cls, html_content, encoding):
            scraped_items = []
            soup = BeautifulSoup(html_content, "html.parser", from_encoding=encoding)
            books = soup.find_all("article", class_="product_pod")

            for book in books:
                item = {
                    "name": None,
                    "url": None,
                    "availability": None,
                    "img_url": None,
                    "price": None,
                }
                item["name"] = book.h3.a["title"]
                item["url"] = cls.base_url + book.h3.a["href"]
                item["availability"] = book.find("p", class_="availability").get_text()
                item["img_url"] = cls.base_url + book.img["src"]
                item["price"] = book.find("p", class_="price_color").get_text()
                scraped_items.append(item)

            return scraped_items


Optionally, we format the data:

.. code-block:: python
    :emphasize-lines: 30-34

    from bs4 import BeautifulSoup
    import re

    from minimal_web_scraper.parsers import BaseParser

    class Parser(BaseParser):
        base_url = "https://books.toscrape.com/"
        scope_urls = ["https://books.toscrape.com"] 

        @classmethod
        def parse(cls, html_content, encoding):
            scraped_items = []
            soup = BeautifulSoup(html_content, "html.parser", from_encoding=encoding)
            books = soup.find_all("article", class_="product_pod")

            for book in books:
                item = {
                    "name": None,
                    "url": None,
                    "availability": None,
                    "img_url": None,
                    "price": None,
                }
                item["name"] = book.h3.a["title"]
                item["url"] = cls.base_url + book.h3.a["href"]
                item["availability"] = book.find("p", class_="availability").get_text()
                item["img_url"] = cls.base_url + book.img["src"]
                item["price"] = book.find("p", class_="price_color").get_text()

                if item["price"]:
                    item["price"] = float(item["price"][2:])
                if item["availability"]:
                    matched = re.search("(In stock|Out of stock)", item["availability"])
                    item["availability"] = matched[0]

                scraped_items.append(item)

            return scraped_items


Here what it looks like at the end:

.. code-block:: python

    from bs4 import BeautifulSoup
    import re

    from minimal_web_scraper.parsers import BaseParser

    class Parser(BaseParser):
        base_url = "https://books.toscrape.com/"
        scope_urls = ["https://books.toscrape.com"]

        @classmethod
        def parse(cls, html_content, encoding):
            scraped_items = []
            soup = BeautifulSoup(html_content, "html.parser", from_encoding=encoding)
            books = soup.find_all("article", class_="product_pod")

            for book in books:
                item = {
                    "name": None,
                    "url": None,
                    "availability": None,
                    "img_url": None,
                    "price": None,
                }
                item["name"] = book.h3.a["title"]
                item["url"] = cls.base_url + book.h3.a["href"]
                item["availability"] = book.find("p", class_="availability").get_text()
                item["img_url"] = cls.base_url + book.img["src"]
                item["price"] = book.find("p", class_="price_color").get_text()

                if item["price"]:
                    item["price"] = float(item["price"][2:])
                if item["availability"]:
                    matched = re.search("(In stock|Out of stock)", item["availability"])
                    item["availability"] = matched[0]

                scraped_items.append(item)

            return scraped_items

Scraper
-------

The file ``main.py`` hosts the script that call the library and the parser.

.. include:: ../../../example/example.py
    :code: python


Execution
---------

Now the project structure is:

.. code-block::

    my_first_scraper
    |
    |- main.py
    |- parser_example.py
    |- venv

Head back to the terminal, we need to install the libraries we used.

.. code-block:: console

    (venv)$ pip install bs4 pandas

Then, we can finally run our program:

.. code-block:: console

    (venv)$ python main.py


Here is the result:

.. code-block:: console

                                        name  price
    0                   A Light in the Attic  51.77
    1                     Tipping the Velvet  53.74
    2                             Soumission  50.10
    3                          Sharp Objects  47.82
    4  Sapiens: A Brief History of Humankind  54.23

    
Next
----

Now that you have a working parser, you can try to write a new one for single products pages of the same site (`example <https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html>`_).
If you need help, you can check a possible answer at the `Github repository <parser-example_>`_.


.. _bs4: https://beautiful-soup-4.readthedocs.io/en/latest/
.. _parser-example: https://github.com/Gamma120/minimal-web-scraper/blob/main/example/parser_example.py
