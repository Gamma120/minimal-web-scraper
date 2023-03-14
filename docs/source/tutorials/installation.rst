Installation
============

This will guide you through the installation of Python and set up of your project environment.
If you already have Python on your machine and know how to use a virtual environment,
you can skip to `Download the library`_.

The project name for this example is ``my_first_scraper``, feel free to replace this by your own project name.


Python
------

Check Python version
^^^^^^^^^^^^^^^^^^^^

Before installing Python, you may want to verify that it is not already installed. Most of the Linux distributions come with Python.

.. tabs::

    .. group-tab:: Windows

        .. code-block:: console
            
            > py --version

    .. tab:: Linux

        .. code-block:: console
        
            $ python --version

If Python is installed, the command should returns something like ``Python 3.10`` or a higher version of Python.
You can skip to `Virtual environment`_, else read the next paragraph.


Python Installation
^^^^^^^^^^^^^^^^^^^

Alternative guide: 


Windows
"""""""

Officials guides for Windows:

- Installation: https://docs.python.org/3/using/windows.html#installation-steps
- Invoke from the command line : https://docs.python.org/3/using/windows.html#from-the-command-line

Download the Python `Windows installer <https://www.python.org/downloads/windows/>`_ for your system and follow its instructions.
I recommand you to check the box ``Add Python to PATH``, to make Python available in the command line.


Linux
"""""

If your distribution is not represented here, use its package manager.

.. tabs::
    
    .. group-tab:: Debian/Ubuntu

        .. code-block:: console
        
            $ apt update
            $ sudo apt install python
        
    .. group-tab:: Fedora
        
        .. code-block:: console

            $ dnf check-update
            $ sudo dnf install python

You can choose which version to install by adding it number after. For example, installing Python 3.11 on Debian:

.. code-block:: console

    $ sudo apt install python3.11

Verify that python is installed by running the command in `Check Python version`_


Project creation
----------------

To create the project folder:

.. code-block:: console

    $ mkdir my_first_scraper
    $ cd my_first_scraper


Virtual environment
^^^^^^^^^^^^^^^^^^^

Official documentation of ``venv``: https://docs.python.org/3/library/venv.html.

It is recommended to use a virtual environment to manage dependencies:

.. tabs::

    .. group-tab:: Windows

        .. code-block:: console
    
            > py -m venv venv
    
    .. group-tab:: Linux

        .. code-block:: console

            $ python -m venv venv


minimal-web-scraper installation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Now your project directory should be:

.. code-block::

    my_first_scraper
    |
    - venv

.. _tuto-activate-env:


Activation of the environement
""""""""""""""""""""""""""""""

In a terminal, activate the newly created virtual environment with:

.. tabs::

    .. group-tab:: Windows

        .. code-block:: console
    
            > venv\Script\activate.bat
    
    .. group-tab:: Linux

        .. code-block:: console

            $ source venv/bin/activate

You should see now, a ``(venv)`` has been append before the prompt of your command line.
And the following command should return:

.. tabs::

    .. group-tab:: Windows

        .. code-block:: console

            (venv)> which python
            <path/to/your/project>\my_first_scraper\venv\Script\python

    .. group-tab:: Linux

        .. code-block:: console

            (venv)$ which python
            <path/to/your/project>/my_first_scraper/venv/bin/python

If the path returned is not of this shape, reiterate the command from :ref:`tuto-activate-env`


Download the library
""""""""""""""""""""

To use the library, we need first to download it. For that, the standard tool is ``pip``:

.. code-block:: console

    (venv)$ pip install git+https://github.com/Gamma120/minimal-web-scraper.git

If ``pip`` don't throw an error, the library is installed and available to use in your project.


.. note::
    Dependencies


    Those are the libraries that minimal-web-scraper uses to work:

    |requires-dist|

    They are automatically downloaded and installed with minimal-web-scraper.


.. note::
    The library is not published on Pypi_, this is why we use the github repository URL. See `VCS support`_ on pip documentation.


Next
----

Next, you will see how to use the library to create your first scraper.

.. _Pypi: https://pypi.org/
.. _VCS support: https://pip.pypa.io/en/stable/topics/vcs-support/
