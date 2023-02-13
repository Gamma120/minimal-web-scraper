Installation
============

This will guides you through the installation of Python and set up of your project environment.
If you already have Python on your machine and know the usage of a virtual environment,
you can skip to `Install minimal-web-scraper`_. 


Python
------

The library supports Python |python-version|. To install Python see the official guide:
https://wiki.python.org/moin/BeginnersGuide/Download


Dependencies
------------

Those are the libraries that minimal-web-scraper uses to work:

|requires-dist|

They will be automaticaly downloaded and installed with minimal-web-scraper.

.. _requests: https://requests.readthedocs.io/en/latest/


Virtual Environments
--------------------

Virtuals Environment allows you to isolate your dependencies per project.
So, you can work with multiples versions of Python and libraries on the same computer.
Since Python 3.3, ``venv`` is a built-in module to create such environments.

.. code-block:: console 

    $ python -m venv </path/to/new/virtual/environment>


Official documentation of ``venv``: https://docs.python.org/3/library/venv.html.


Install minimal-web-scraper
---------------------------

In your project environment, use your package manager to install the library:

.. code-block:: console

    (venv)$ pip install git+https://github.com/Gamma120/minimal-web-scraper.git
    
.. note::
    The library is not published on Pypi_, this is why we use the github repository url. See `VCS support`_ on pip documentation.

.. _Pypi: https://pypi.org/
.. _VCS support: https://pip.pypa.io/en/stable/topics/vcs-support/
