# Configuration file for the Sphinx documentation builder.
# See https://www.sphinx-doc.org/en/master/usage/configuration.html

project = "ExtraBar"
copyright = "2026, ExtraBar"
author = "ExtraBar"

# Title shown in sidebar (overrides default "project documentation")
html_title = "ExtraBar<br>Docs"

# Extensions
extensions = []

# Root document (main page)
root_doc = "index"

# Exclude build artifacts
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# Furo theme (using all defaults)
html_theme = "furo"

# Static files (images, CSS, etc.)
html_static_path = ["_static"]

# Logo
html_logo = "_static/logo.png"

# Custom CSS for logo size
html_css_files = ['custom.css']
