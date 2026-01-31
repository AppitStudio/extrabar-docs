# Configuration file for the Sphinx documentation builder.
# See https://www.sphinx-doc.org/en/master/usage/configuration.html

project = "extrabar-docs"
copyright = "2026"
author = "extrabar"

# Add extensions here if you need them (e.g. myst_parser for .md support)
extensions = []

# Root document (main page)
root_doc = "index"

# Exclude build artifacts
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# Read the Docs theme (built-in on RTD, no extra install needed)
html_theme = "sphinx_rtd_theme"
