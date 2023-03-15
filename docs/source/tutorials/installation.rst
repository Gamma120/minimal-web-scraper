Installation
============

This will guide you through the installation of Python and set up of your project environment.
If you already have Python on your machine and know how to use a virtual environment,
you can skip to `Download the library`_.

The project name for this example is ``my_first_scraper``, feel free to replace this by your own project name.


Git
---

You will also need to install `Git`_ for this tutorial.

Check Git version
^^^^^^^^^^^^^^^^^

Before installing Git, you you may want to verify that it is not already installed. Most of the Linux distributions come with GIt.

Open a terminal:

.. code-block::

    $ git --version

If Git is installed, the command should returns something like ``git version X.X.X``.
You can skip to `Python`_, else read the next paragraph.


Git Installation
^^^^^^^^^^^^^^^^

Official guide: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git

Windows
"""""""

The official site to download Git : https://git-scm.com/download/win.

Follow the instruction of the installer and verify the installation by running the command at `Check Git version`_.

Linux
"""""

Execute the following commands:

.. tabs::

    .. group-tab:: Debian/Ubuntu

        .. code-block::

            $ sudo apt update
            $ sudo apt install git
    
    .. group-tab:: Fedora

        .. code-block::

            $ dnf check-update
            $ sudo dnf install git
  
Verify the installation by running the command at `Check Git version`_.


Python
------

Check Python version
^^^^^^^^^^^^^^^^^^^^

Before installing Python, you may want to verify that it is not already installed. Most of the Linux distributions come with Python.

Open a terminal:

.. code-block:: console
        
    $ python --version

If Python is installed, the command should returns something like ``Python 3.10`` or a higher version of Python.
You can skip to `Project creation`_, else read the next paragraph.


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
        
            $ sudo apt update
            $ sudo apt install python3
        
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

.. code-block:: console

    $ python -m venv venv


Now your project directory should be:

.. code-block::

    my_first_scraper
    |
    - venv


minimal-web-scraper installation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Activation of the environement
""""""""""""""""""""""""""""""

In a terminal, activate the newly created virtual environment with:

.. _activate_env:

.. tabs::

    .. group-tab:: Windows cmd

        .. code-block:: console
    
            $ venv\Scripts\activate.bat


    .. group-tab:: Windows PowerShell

        .. code-block:: console
    
            $ venv\Scripts\Activate.ps1

    .. group-tab:: Linux

        .. code-block:: console

            $ source venv/bin/activate

You should see now, a ``(venv)`` has been append before the prompt of your command line.

.. note::

    PowerShell can throw you an error. See `about Execution policies <https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-7.3>`_.

Execute the following command (there is no equivalent in cmd):

.. tabs::

    .. group-tab:: Windows PowerShell

        .. code-block:: console

            (venv)$ Get-Command python

    .. group-tab:: Linux

        .. code-block:: console

            (venv)$ which python

If the path returned is not in the project sub-directory, reiterate the command from `above <activate_env_>`_.


Download the library
""""""""""""""""""""

To use the library, we need to download it. For that, the standard tool is ``pip``:

.. code-block:: console

    (venv)$ pip install git+https://github.com/Gamma120/minimal-web-scraper.git

Verify the library is installed:

.. code-block::

    (venv)$ pip list

``minimal-web-scraper`` must be in the list returned.


Next
----

Next, you will see how to use the library to create your first scraper.

.. _Git: https://git-scm.com/
