# Configuration file for the Sphinx documentation builder.
# See https://www.sphinx-doc.org/en/master/usage/configuration.html

project = "ExtraBar"
copyright = "2026, ExtraBar"
author = "ExtraBar"

# Add extensions here if you need them (e.g. myst_parser for .md support)
extensions = []

# Root document (main page)
root_doc = "index"

# Exclude build artifacts
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# Furo theme - modern, readable, with dark mode
html_theme = "furo"

# Static files (images, CSS, etc.)
html_static_path = ["_static"]

# Logo
html_logo = "_static/logo.png"

# Theme customization with brand colors (Black #000000, Purple #5B5DE7)
html_theme_options = {
    # Light mode colors
    "light_css_variables": {
        "color-brand-primary": "#5B5DE7",
        "color-brand-content": "#5B5DE7",
        "color-sidebar-background": "#000000",
        "color-sidebar-search-background": "#1a1a1a",
        "color-sidebar-text": "#ffffff",
        "color-sidebar-link-text": "#ffffff",
        "color-sidebar-item-background--hover": "#5B5DE7",
        "color-sidebar-caption-text": "#9d9daa",
    },
    # Dark mode colors
    "dark_css_variables": {
        "color-brand-primary": "#5B5DE7",
        "color-brand-content": "#8385eb",
        "color-sidebar-background": "#000000",
        "color-sidebar-search-background": "#1a1a1a",
        "color-sidebar-text": "#ffffff",
        "color-sidebar-link-text": "#ffffff",
        "color-sidebar-item-background--hover": "#5B5DE7",
        "color-sidebar-caption-text": "#9d9daa",
    },
}

# Custom CSS for additional styling
html_css_files = ['custom.css']
