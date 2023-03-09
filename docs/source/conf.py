# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here.
from pathlib import Path
import sys
from importlib import metadata

sys.path.insert(0, Path(__file__).parents[2].resolve().as_posix())


# -- Project information -----------------------------------------------------

project = "minimal-web-scraper"
project_metadata = metadata.metadata(project)

author = project_metadata["author"]
email = project_metadata["author-email"]
version = project_metadata["version"]
copyright = f"2023, {author}"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx_tabs.tabs",
]

templates_path = ["_templates"]


# -- Options for HTML output -------------------------------------------------

html_theme = "furo"
html_static_path = ["_static"]

# Global replacements

python_version = project_metadata["requires-python"]
requires = metadata.requires(project)
if requires:
    requires_str = ", ".join(r for r in requires)

rst_prolog = f"""
.. |python-version| replace:: **{python_version}**
.. |requires-dist| replace:: {requires_str}
.. |email| replace:: {email}
"""
