# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'KE3060 (KE3061)英文--V02'
copyright = '2025, momo'
author = 'momo'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["myst_parser","sphinx_copybutton"]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

...
html_theme = "sphinx_book_theme"
#html_static_path = ['_static']

html_theme_options = {
    "repository_url": "https://github.com/mm0616/KE3060-KE3061-EN---V02.git",
    "use_repository_button": True,
}

html_logo = "path/to/myimage.png"

html_title = "My site title"