# Configuration file for the Sphinx documentation builder.
import os
import sys
import django

# Setting up the Django environment for the script to run.

sys.path.insert(0, os.path.abspath('../'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pollsproject.settings')


django.setup()

needs_sphinx = '3.0'

project = 'polls'
copyright = '2023, kopano'
author = 'kopano'
release = '00.00.01'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
