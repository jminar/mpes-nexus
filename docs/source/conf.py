# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

import sys, os, datetime

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'mpes-nexus'
author = 'Tommaso Pincelli, R. Patrick Xian, Maciej Dendzik, Laurenz Rettig, Ralph Ernstorfer'
copyright = u'2018-{}, {}'.format(datetime.datetime.now().year, author)
description = u'NeXus format for multidimensional photoemission spectroscopy'

# The full version, including alpha/beta/rc tags
# version = u'unknown NXDL version'
# release = u'unknown NXDL release'
# nxdl_version = open('../../NXDL_VERSION').read().strip()
# if nxdl_version is not None:
#     version = nxdl_version.split('.')[0]
#     release = nxdl_version


# -- General configuration ---------------------------------------------------

# https://github.com/nexusformat/definitions/issues/659#issuecomment-577438319
needs_sphinx = '2.3'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'alabaster'
html_theme = 'sphinxdoc'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = []

html_sidebars = {
    '**': [
        'localtoc.html', 
        'relations.html', 
        'sourcelink.html', 
        'searchbox.html', 
        'google_search.html'
    ],
}

# Output file base name for HTML help builder.
htmlhelp_basename = 'MPESNeXusdoc'

# -- Options for Latex output -------------------------------------------------
latex_elements = {
    'maxlistdepth':7, # some application definitions are deeply nested
}
