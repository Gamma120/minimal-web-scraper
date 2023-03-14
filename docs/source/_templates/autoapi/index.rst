API Reference
=============

This page contains auto-generated API reference documentation [#f1]_.

.. toctree::
   :titlesonly:

   {% for page in pages %}
   {% if page.top_level_object and page.display %}
   {{ page.include_path }}
   {% endif %}
   {% endfor %}

.. [#f1] Created with `sphinx-autoapi <https://github.com/readthedocs/sphinx-autoapi>`_ and `templates from bylr.info tutorial <https://bylr.info/articles/2022/05/10/api-doc-with-sphinx-autoapi/>`_