# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Test'
copyright = '2026, Manfred'
author = 'Manfred'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
     "sphinx_multiversion",
]

templates_path = ['_templates']
exclude_patterns = []
locale_dirs = ['locale/']
gettext_compact = False



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

html_sidebars = {
    '**': [
        'versions.html',
    ]
}

import os
try:
    from babel import Locale
except ImportError:
    Locale = None

locale_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'locale')

def get_language_name(code):
    if Locale:
        try:
            return Locale.parse(code).get_display_name(code).capitalize()
        except Exception:
            pass
    return code.upper()

dynamic_languages = [('en', get_language_name('en'))]

if os.path.exists(locale_dir):
    for code in os.listdir(locale_dir):
        if os.path.isdir(os.path.join(locale_dir, code)) and code != 'en':
            dynamic_languages.append((code, get_language_name(code)))

html_context = {
    'supported_languages': dynamic_languages
}

smv_tag_whitelist = r'^.*$'
smv_branch_whitelist = r'^(18\.0|19\.0|main)$'
smv_remote_whitelist = r'^.*$'
