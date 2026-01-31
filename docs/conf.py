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

# Read the Docs theme
html_theme = "sphinx_rtd_theme"

# Static files (images, CSS, etc.)
html_static_path = ["_static"]

# Logo
html_logo = "_static/logo.png"

# Theme customization options
html_theme_options = {
    'logo_only': False,              # Set True to hide project name next to logo
    'display_version': True,
    'style_nav_header_background': '#000000',
}

# Custom CSS for brand colors
html_css_files = ['custom.css']
