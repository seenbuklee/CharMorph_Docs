# Configuration file for the Sphinx documentation builder.

# -- Project information
import os
import sys

sys.path.insert(0, os.path.abspath("_themes"))


project = 'CharMorph'
copyright = '2022, Upliner'
author = 'Hopefullyidontgetbanned'

release = '0.2'
version = '0.2.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx_autorun',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinxawesome_theme'
html_theme_path = ["_themes"]
exclude_patterns = ["_themes"]

# -- Options for EPUB output
epub_show_urls = 'footnote'
