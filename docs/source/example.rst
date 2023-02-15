Example
=======

First, you need to write the parser that will be used by the library.
For this example, `BeautifulSoup <bs4_>`_ is the library used to parse the HTML.

Parsers
-------

These are parsers of https://books.toscrape.com/ and individual product page (`example <product-page_>`_):

.. include:: ../../example/parser_example.py
    :code: python


Script
------

Then, import them in your script:

.. include:: ../../example/example.py
    :code: python


Execution
---------

Finally, run in terminal:

.. code-block:: console

    $ python example.py


The result should look like:

.. code-block:: text

                                        name  ...  price
    0                   A Light in the Attic  ...  51.77
    1                     Tipping the Velvet  ...  53.74
    2                             Soumission  ...  50.10
    3                          Sharp Objects  ...  47.82
    4  Sapiens: A Brief History of Humankind  ...  54.23

    [5 rows x 5 columns]

Find those `examples <repo-example_>`_ on the Github repository.

.. _repo-example: https://github.com/Gamma120/minimal-web-scraper/tree/main/example
.. _bs4: https://beautiful-soup-4.readthedocs.io/en/latest/
.. _product-page: https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html