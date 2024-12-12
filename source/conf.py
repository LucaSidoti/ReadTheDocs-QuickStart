# Configuration file for the Sphinx documentation builder.
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
project = 'Sphinx to Read the Docs: Complete Guide'
copyright = '2024, Luca Sidoti'
author = 'Luca Sidoti'
release = '1.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx_rtd_theme',
    'sphinx_copybutton',
    'sphinx_code_tabs',
    'sphinx_new_tab_link',
    'sphinx_togglebutton'
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    'logo_only': False,
    'collapse_navigation': False,
    'sticky_navigation': True,
    'includehidden': True,
    'navigation_depth': 4,
    'titles_only': False
}

html_static_path = ['_static']
html_css_files = ['custom.css']
