# Configuration file for the Sphinx documentation builder.
# See https://www.sphinx-doc.org/en/master/usage/configuration.html

project = "ExtraBar"
copyright = "2026, ExtraBar"
author = "ExtraBar"

# Extensions
extensions = []

# Root document (main page)
root_doc = "index"

# Exclude build artifacts
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# Furo theme
html_theme = "furo"

# Static files (images, CSS, etc.)
html_static_path = ["_static"]

# Logo
html_logo = "_static/logo.png"

# Minimal customization - just brand color
html_theme_options = {
    "light_css_variables": {
        "color-brand-primary": "#5B5DE7",
        "color-brand-content": "#5B5DE7",
    },
    "dark_css_variables": {
        "color-brand-primary": "#8385eb",
        "color-brand-content": "#8385eb",
    },
}

# Custom CSS
html_css_files = ['custom.css']
