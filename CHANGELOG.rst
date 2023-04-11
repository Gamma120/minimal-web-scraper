The format is inspired by `Keep a Changelog`_ and others Python projects.
This project adheres to `Semantic Versioning`_.

.. _`Keep a Changelog`: https://keepachangelog.com/en/1.0.0/
.. _`Semantic Versioning`: https://semver.org/spec/v2.0.0.html


Here is a template for a section of the changelog.

.. code-block:: text

    version
    -------

    Release date

    Deprecations
    ^^^^^^^^^^^^

    On-coming discontinuations on the support of Python versions, dependencies or features.

    Removed
    ^^^^^^^

    Effective discontinuations on the support of Python versions, dependencies or features.

    Improvements
    ^^^^^^^^^^^^

    Changes on the code that add or change functionalities.

    Dependencies
    ^^^^^^^^^^^^

    Changes on the dependencies requested.

    Bug fixes
    ^^^^^^^^^

    Changes that resolve bugs.

    Documentation
    ^^^^^^^^^^^^^

    Changes on the documentation or none logic files (README, CHANGELOG...).

    Quality assurance
    ^^^^^^^^^^^^^^^^^

    Changes on CI, tools or code that improve the quality of the code.


0.1.1
-----

2023-04-11

Bug fixes
^^^^^^^^^

- change :func:`minimal_web_scraper.parsers.utils.find_parser` to enable better matching patterns
- change imports in ``__init__.py`` files to have import suggestions


0.1
---

2023-03-17

- First release of the project.
