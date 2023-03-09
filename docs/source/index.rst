.. _topics-index:

###########################################
minimal-web-scraper |version| documentation
###########################################

**minimal-web-scraper** is a Python library that provides you the tools to **scrape data from the web**.
The library supports Python |python-version|.

.. note::
   Please be aware of the legal implication of scraping information from internet: https://en.wikipedia.org/wiki/Web_scraping#Legal_issues


Quick Start
===========

Here is a small script that demonstrate how to use the library.
Notice that the library doesn't not provide any `parser <https://en.wikipedia.org/wiki/Parsing#Parser>`_.
See the `example <repo-example_>`_ at the Github repository for a working scraper.

.. include:: ../../example/example.py
    :code: python


.. note::
   This project is in development state and the author doesn't guarantee the stability of its API.


This is a really small library, if you need a comprehensive and proven web scraper in your favorite language, check out `Scrapy`_ framework.


Get started
===========

Check out :doc:`tutorials/index` for a step-by-step instructions to set up a project using minimal-web-scraper.

.. toctree::
   :maxdepth: 2

   tutorials/index


How-to guides
=============

Check out :doc:`how-to/index` for specific guides on the library.

.. toctree::
   :maxdepth: 2

   how-to/index



API
===

.. toctree::
   :maxdepth: 2

   api

More
====

.. toctree::
   :maxdepth: 2

   license
   about
   changes


.. _repo-example: https://github.com/Gamma120/minimal-web-scraper/tree/main/example
.. _Scrapy: https://scrapy.org/