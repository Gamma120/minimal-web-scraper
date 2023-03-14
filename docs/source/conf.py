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
    "sphinx.ext.coverage",
    "sphinx_tabs.tabs",
    "sphinx_copybutton",
    "autoapi.extension",
]

templates_path = ["_templates"]


# -- Options for HTML output -------------------------------------------------

html_theme = "furo"
html_static_path = ["_static"]
html_css_files = ["css/custom.css"]


# -- Options for the coverage extension --------------------------------------

coverage_show_missing_items = True


# -- autoapi configuration ---------------------------------------------------


autoapi_type = "python"
autoapi_dirs = ["../../src"]
autoapi_template_dir = "_templates/autoapi"
autodoc_typehints = "signature"
autoapi_options = [
    "members",
    "undoc-members",
    "show-inheritance",
    "show-module-summary",
    "imported-members",
]

# autoapi_keep_files = True

# -- custom auto_summary() macro ---------------------------------------------
# from https://bylr.info/articles/2022/05/10/api-doc-with-sphinx-autoapi/


def contains(seq, item):
    """Jinja2 custom test to check existence in a container.
    Example of use:
    {% set class_methods = methods|selectattr("properties", "contains", "classmethod") %}
    Related doc: https://jinja.palletsprojects.com/en/3.1.x/api/#custom-tests
    """
    return item in seq


def prepare_jinja_env(jinja_env) -> None:
    """Add `contains` custom test to Jinja environment."""
    jinja_env.tests["contains"] = contains


autoapi_prepare_jinja_env = prepare_jinja_env


def skip_member(app, what, name, obj, skip, options):
    # skip submodules to only display API
    if what == "module":
        skip = True
    return skip


def setup(sphinx):
    sphinx.connect("autoapi-skip-member", skip_member)


# -- Global replacements -----------------------------------------------------

python_version = project_metadata["requires-python"]
requires = metadata.requires(project)
if requires:
    requires_str = ", ".join(r for r in requires)

rst_prolog = f"""
.. |python-version| replace:: **{python_version}**
.. |requires-dist| replace:: {requires_str}
.. |email| replace:: {email}
.. role:: summarylabel
"""
